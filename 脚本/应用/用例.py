"""
DDD 应用层 - 业务用例编排
协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节
"""
from typing import List, Tuple
from dataclasses import dataclass, field

from 领域.模型 import 赔率快照, 赔率位移, 校验深盘冷平放行资格
from 领域.契约 import 赔率提供者契约, 赔率账本契约


@dataclass
class 记录结果:
    入库数量: int
    异常异动警报: List[赔率位移]
    关闭胜平负场次: List[赔率快照] = field(default_factory=list)


@dataclass
class 轨迹结果:
    竞彩场次: str
    采样次数: int
    累计平赔位移: float
    趋势定性: str
    历史快照列表: List[赔率快照]


class 探测并记录心电图用例:
    """业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库"""

    def __init__(self, 提供者: 赔率提供者契约, 账本: 赔率账本契约):
        self.提供者 = 提供者
        self.账本 = 账本

    def 执行(self) -> 记录结果:
        当前快照列表 = self.提供者.抓取当前快照列表()
        警报列表: List[赔率位移] = []
        关闭胜平负列表: List[赔率快照] = []

        for 当前 in 当前快照列表:
            if 当前.市场类型 == "hhad":
                关闭胜平负列表.append(当前)
            早期 = self.账本.获取最新快照(当前.竞彩场次)
            if 早期 and 当前.同一市场(早期) and 当前.记录时间戳 > 早期.记录时间戳:
                位移 = 当前.计算位移(早期)
                if 位移.是否显著防守降水() or 位移.异动信号 != "中性平稳横盘":
                    警报列表.append(位移)

        self.账本.批量保存快照(当前快照列表)
        return 记录结果(
            入库数量=len(当前快照列表),
            异常异动警报=警报列表,
            关闭胜平负场次=关闭胜平负列表
        )


class 回溯连续轨迹用例:
    """业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势"""

    def __init__(self, 账本: 赔率账本契约):
        self.账本 = 账本

    def 分析单场(self, 竞彩场次: str) -> 轨迹结果:
        记录 = self.账本.查询比赛连续轨迹(竞彩场次)
        if not 记录:
            return 轨迹结果(
                竞彩场次=竞彩场次,
                采样次数=0,
                累计平赔位移=0.0,
                趋势定性="暂无数据",
                历史快照列表=[]
            )

        最新 = max(记录, key=lambda s: s.记录时间戳)
        记录 = sorted([s for s in 记录 if s.同一市场(最新)], key=lambda s: s.记录时间戳)
        首盘 = 记录[0]
        末盘 = 记录[-1]
        累计位移 = round(末盘.赔率.平局 - 首盘.赔率.平局, 2)

        if 累计位移 < 0:
            态势 = "首末平项赔率净下降（不推断原因）"
        elif 累计位移 > 0:
            态势 = "首末平项赔率净上升（不推断原因）"
        else:
            态势 = "平稳横盘震荡"

        return 轨迹结果(
            竞彩场次=竞彩场次,
            采样次数=len(记录),
            累计平赔位移=累计位移,
            趋势定性=态势,
            历史快照列表=记录
        )


@dataclass
class 平局候选:
    快照: 赔率快照
    类型: str  # "均势平局" 或 "深盘冷平"
    去水平局概率: float
    放行理由: str


@dataclass
class 全量扫描结果:
    关盘场次: List[赔率快照] = field(default_factory=list)
    均势平局标的: List[平局候选] = field(default_factory=list)
    深盘冷评标的: List[平局候选] = field(default_factory=list)
    排除场次: List[Tuple[赔率快照, str]] = field(default_factory=list)


class 全量精算扫描用例:
    """业务用例：对输入的全量比赛快照进行全量无死角精算扫描，输出双轨平局候选与关盘场次"""

    def 扫描全量(self, 快照列表: List[赔率快照]) -> 全量扫描结果:
        关盘: List[赔率快照] = []
        均势: List[平局候选] = []
        冷平: List[平局候选] = []
        排除: List[Tuple[赔率快照, str]] = []

        for s in 快照列表:
            if s.市场类型 == "hhad":
                关盘.append(s)
                continue

            h, d, a = s.赔率.主胜, s.赔率.平局, s.赔率.客胜
            margin = (1 / h) + (1 / d) + (1 / a)
            d_prob = round((1 / d) / margin, 4)

            fav_win = min(h, a)
            if fav_win < 1.60:
                合格, 理由 = 校验深盘冷平放行资格(强方胜赔=fav_win, 平局赔率=d)
                if 合格:
                    冷平.append(平局候选(快照=s, 类型="深盘冷平", 去水平局概率=d_prob, 放行理由=理由))
                else:
                    排除.append((s, 理由))
            else:
                if 2.50 <= d <= 3.65:
                    均势.append(平局候选(快照=s, 类型="均势平局", 去水平局概率=d_prob, 放行理由=f"均势区间(平赔={d})"))
                else:
                    排除.append((s, f"平赔超出均势区间(平赔={d})"))

        return 全量扫描结果(
            关盘场次=关盘,
            均势平局标的=均势,
            深盘冷评标的=冷平,
            排除场次=排除
        )
