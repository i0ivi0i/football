"""
DDD 适配器防腐层 - 中国体彩官方 API 适配器
负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体
"""
import json
import time
import urllib.request
from typing import List, Optional

from 领域.模型 import 赔率数值, 赔率快照
from 领域.契约 import 赔率提供者契约


class 体彩官方适配器(赔率提供者契约):
    """实现赔率提供者契约，直连国家体彩中心官方网关"""

    默认端点 = "https://webapi.sporttery.cn/gateway/uniform/football/getMatchCalculatorV1.qry?channel=c"

    def __init__(self, 端点地址: str = 默认端点, 超时秒数: int = 10):
        self.端点地址 = 端点地址
        self.超时秒数 = 超时秒数

    def 抓取当前快照列表(self) -> List[赔率快照]:
        请求 = urllib.request.Request(
            self.端点地址,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(请求, timeout=self.超时秒数) as 响应:
            原始数据 = json.loads(响应.read().decode("utf-8"))
        return self.解析原始数据(原始数据)

    def 解析原始数据(self, 原始数据: dict, 自定义时间戳: Optional[int] = None) -> List[赔率快照]:
        当前时间 = 自定义时间戳 if 自定义时间戳 is not None else int(time.time())
        快照列表: List[赔率快照] = []

        比赛日列表 = 原始数据.get("value", {}).get("matchInfoList", [])
        for 比赛日 in 比赛日列表:
            for 比赛 in 比赛日.get("subMatchList", []):
                胜平负 = 比赛.get("had")
                让球盘前缀 = ""
                
                # 庄家明牌公理：若官方关闭基础胜平负 (had 为空)，强制回退捕获让球盘 (hhad)
                if not 胜平负 or not (胜平负.get("h") and 胜平负.get("d") and 胜平负.get("a")):
                    让球胜平负 = 比赛.get("hhad")
                    if 让球胜平负 and 让球胜平负.get("h") and 让球胜平负.get("d") and 让球胜平负.get("a"):
                        胜平负 = 让球胜平负
                        让球数 = 让球胜平负.get("goalLine", "")
                        让球盘前缀 = f" [让球明牌{让球数}]"
                    else:
                        continue

                主胜字串 = 胜平负.get("h")
                平局字串 = 胜平负.get("d")
                客胜字串 = 胜平负.get("a")

                if not (主胜字串 and 平局字串 and 客胜字串):
                    continue

                try:
                    主胜 = float(主胜字串)
                    平局 = float(平局字串)
                    客胜 = float(客胜字串)
                    浮动标记 = int(胜平负.get("df") or 0)
                except (ValueError, TypeError):
                    continue

                比赛编号 = str(比赛.get("matchId", ""))
                竞彩场次 = str(比赛.get("matchNumStr", ""))
                主队 = 比赛.get("homeTeamAbbName", "")
                客队 = 比赛.get("awayTeamAbbName", "")
                对阵名称 = f"{主队} vs {客队}{让球盘前缀}"
                联赛名称 = 比赛.get("leagueAbbName", "")

                快照 = 赔率快照(
                    比赛编号=比赛编号,
                    竞彩场次=竞彩场次,
                    对阵名称=对阵名称,
                    联赛名称=联赛名称,
                    赔率=赔率数值(主胜=主胜, 平局=平局, 客胜=客胜),
                    记录时间戳=当前时间,
                    官方浮动标记=浮动标记
                )
                快照列表.append(快照)

        return 快照列表
