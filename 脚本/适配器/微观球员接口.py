"""
DDD 适配器：API-Sports 微观球员与伤停数据管道
支持双 Key 轮换，负责拉取核心伤停、关键组织大脑与防守对抗数据
"""
import urllib.request
import json
from typing import List, Dict, Any, Optional

API_KEYS = [
    "832130dcfdadb0aac6af9e19300f74ec",
    "d3ee3cb753c07c442d7d3fd16bb6dceb"
]

class 微观球员适配器:
    def __init__(self, key_index: int = 0):
        self.key_index = key_index

    def _get_headers(self) -> Dict[str, str]:
        return {
            "x-apisports-key": API_KEYS[self.key_index % len(API_KEYS)],
            "User-Agent": "Mozilla/5.0"
        }

    def 查询比赛伤停名单(self, fixture_id: int) -> List[Dict[str, str]]:
        """获取比赛双方的核心伤停名单、缺阵原因与战术位置"""
        url = f"https://v3.football.api-sports.io/injuries?fixture={fixture_id}"
        req = urllib.request.Request(url, headers=self._get_headers())
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())
            res = []
            for item in data.get("response", []):
                res.append({
                    "球队": item["team"]["name"],
                    "球员": item["player"]["name"],
                    "原因": item["player"]["reason"],
                    "状态": item["player"]["type"]
                })
            return res
        except Exception as e:
            return [{"错误": f"伤停查询失败: {str(e)}"}]
