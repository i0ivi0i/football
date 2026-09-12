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

    def 计算赛程体能负荷(self, team_id: int, 当前比赛日期: str) -> Dict[str, Any]:
        """计算球队休赛间隔天数与体能储备衰竭度"""
        from datetime import datetime
        url = f"https://v3.football.api-sports.io/fixtures?team={team_id}&last=1"
        req = urllib.request.Request(url, headers=self._get_headers())
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())
            fixtures = data.get("response", [])
            if not fixtures:
                return {"休赛天数": 7, "体能评级": "体能储备充沛 (无近期密集赛程)"}
            上场比赛时间 = fixtures[0]["fixture"]["date"][:10]
            d1 = datetime.strptime(上场比赛时间, "%Y-%m-%d")
            d2 = datetime.strptime(当前比赛日期, "%Y-%m-%d")
            休赛天数 = (d2 - d1).days
            if 休赛天数 <= 3:
                评级 = f"体能重度透支 (休赛仅 {休赛天数} 天，双线密集作战，下半场极易保平打慢)"
            elif 休赛天数 <= 5:
                评级 = f"体能轻度疲劳 (休赛 {休赛天数} 天)"
            else:
                评级 = f"体能储备充沛 (休赛 {休赛天数} 天)"
            return {"休赛天数": 休赛天数, "体能评级": 评级, "上场比赛日": 上场比赛时间}
        except Exception as e:
            return {"休赛天数": 5, "体能评级": f"估算中性 (接口异常: {str(e)})"}

    def 提取比赛微观高阶数据(self, event_id: str) -> Dict[str, Any]:
        """从 sports-skills (Understat / ESPN) 提取 xG、射正、门将扑救与战术犯规微观指标"""
        try:
            from sports_skills import football
            stats = football.get_event_statistics(event_id=event_id)
            xg_data = football.get_event_xg(event_id=event_id)
            players = football.get_event_players_statistics(event_id=event_id)
            
            teams_stat = stats.get("data", {}).get("teams", [])
            xg_teams = xg_data.get("data", {}).get("teams", [])
            
            summary = {
                "event_id": event_id,
                "team1_xg": xg_teams[0].get("xg", 0.0) if len(xg_teams) > 0 else 0.0,
                "team2_xg": xg_teams[1].get("xg", 0.0) if len(xg_teams) > 1 else 0.0,
                "team1_saves": teams_stat[0].get("statistics", {}).get("goalkeeper_saves", "0") if len(teams_stat) > 0 else "0",
                "team2_saves": teams_stat[1].get("statistics", {}).get("goalkeeper_saves", "0") if len(teams_stat) > 1 else "0",
                "team1_fouls": teams_stat[0].get("statistics", {}).get("fouls", "0") if len(teams_stat) > 0 else "0",
                "team2_fouls": teams_stat[1].get("statistics", {}).get("fouls", "0") if len(teams_stat) > 1 else "0",
                "players_available": bool(players.get("data", {}).get("teams"))
            }
            return summary
        except Exception as e:
            return {"error": f"提取高阶数据失败: {str(e)}"}

    def 提取交锋历史H2H(self, team_id_1: str, team_id_2: str) -> Dict[str, Any]:
        """从 football-data.co.uk 提取双方历史交锋总场次、平局场次与平局基因率"""
        try:
            from sports_skills import football
            h2h = football.get_head_to_head(team_id=team_id_1, team_id_2=team_id_2)
            summary = h2h.get("data", {}).get("summary", {})
            total = summary.get("total_meetings", 0)
            draws = summary.get("draws", 0)
            return {
                "total_meetings": total,
                "draws": draws,
                "draw_rate": round(draws / total, 4) if total > 0 else 0.0,
                "team1_wins": summary.get("team1", {}).get("wins", 0),
                "team2_wins": summary.get("team2", {}).get("wins", 0)
            }
        except Exception as e:
            return {"error": f"H2H提取失败: {str(e)}", "total_meetings": 0, "draws": 0, "draw_rate": 0.0}

    def 提取球员高阶链条数据(self, event_id: str) -> Dict[str, Any]:
        """从 Understat 提取球员微观进攻链 xG Chain、xG Buildup 与关键传球数据"""
        try:
            from sports_skills import football
            players_stat = football.get_event_players_statistics(event_id=event_id)
            creators = []
            for team in players_stat.get("data", {}).get("teams", []):
                for p in team.get("players", []):
                    if p.get("xg_chain", 0) > 0.3 or p.get("key_passes", 0) >= 2:
                        creators.append({
                            "name": p.get("name"),
                            "team": team.get("team", {}).get("name"),
                            "xg": p.get("xg", 0.0),
                            "xa": p.get("xa", 0.0),
                            "xg_chain": p.get("xg_chain", 0.0),
                            "xg_buildup": p.get("xg_buildup", 0.0),
                            "key_passes": p.get("key_passes", 0)
                        })
            creators.sort(key=lambda x: x.get("xg_chain", 0), reverse=True)
            return {"event_id": event_id, "key_creators": creators}
        except Exception as e:
            return {"error": f"球员高阶链条提取失败: {str(e)}", "key_creators": []}

    def 严格校验完场比分(self, fixture_id: int) -> Dict[str, Any]:
        """强制断言比赛状态必须为 FT (Match Finished)，绝不采信滚球过程临时比分"""
        url = f"https://v3.football.api-sports.io/fixtures?id={fixture_id}"
        req = urllib.request.Request(url, headers=self._get_headers())
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())
            res = data.get("response", [])
            if not res:
                return {"status": "NOT_FOUND", "is_finished": False}
            fix = res[0]
            status = fix["fixture"]["status"]["short"]
            is_finished = status in ["FT", "AET", "PEN"]
            return {
                "fixture_id": fixture_id,
                "status": status,
                "is_finished": is_finished,
                "home_score": fix["goals"]["home"],
                "away_score": fix["goals"]["away"],
                "score_text": f"{fix['goals']['home']}:{fix['goals']['away']}" if is_finished else "未完场"
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e), "is_finished": False}



