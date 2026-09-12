import pytest
import json
from unittest.mock import patch, MagicMock
from 适配器.微观球员接口 import 微观球员适配器

def test_微观球员适配器解析伤停数据():
    适配器 = 微观球员适配器()
    mock_response = {
        "response": [
            {
                "team": {"name": "Osasuna"},
                "player": {"name": "M. Gomez", "reason": "Hamstring Injury", "type": "Missing Fixture"}
            }
        ]
    }
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value.read.return_value = str(mock_response).replace("'", '"').encode("utf-8")
        mock_urlopen.return_value = mock_cm

        res = 适配器.查询比赛伤停名单(1570377)
        assert len(res) == 1
        assert res[0]["球队"] == "Osasuna"
        assert res[0]["球员"] == "M. Gomez"
        assert res[0]["原因"] == "Hamstring Injury"


def test_微观球员适配器计算体能负荷():
    适配器 = 微观球员适配器()
    mock_fixtures = {
        "response": [
            {"fixture": {"date": "2026-09-09T20:00:00+00:00"}}
        ]
    }
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value.read.return_value = str(mock_fixtures).replace("'", '"').encode("utf-8")
        mock_urlopen.return_value = mock_cm

        res = 适配器.计算赛程体能负荷(team_id=727, 当前比赛日期="2026-09-12")
        assert res["休赛天数"] == 3
        assert "体能重度透支" in res["体能评级"]


def test_微观球员适配器提取比赛微观高阶数据():
    适配器 = 微观球员适配器()
    with patch("sports_skills.football.get_event_statistics") as mock_stats, \
         patch("sports_skills.football.get_event_xg") as mock_xg, \
         patch("sports_skills.football.get_event_players_statistics") as mock_players:
        mock_stats.return_value = {
            "data": {
                "teams": [
                    {"statistics": {"goalkeeper_saves": "3", "fouls": "14"}},
                    {"statistics": {"goalkeeper_saves": "5", "fouls": "11"}}
                ]
            }
        }
        mock_xg.return_value = {
            "data": {
                "teams": [
                    {"xg": 0.95},
                    {"xg": 1.05}
                ]
            }
        }
        mock_players.return_value = {"data": {"teams": [{"players": []}]}}

        res = 适配器.提取比赛微观高阶数据("401882909")
        assert res["team1_xg"] == 0.95
        assert res["team2_xg"] == 1.05
        assert res["team1_saves"] == "3"
        assert res["team2_saves"] == "5"
        assert res["players_available"] is True


def test_微观球员适配器严格断言完场比分():
    适配器 = 微观球员适配器()
    # 模拟进行中比赛 (63分钟 1:3 临时比分，尚未完场)
    mock_live = {
        "response": [{
            "fixture": {"status": {"short": "2H", "long": "Second Half"}},
            "goals": {"home": 1, "away": 3}
        }]
    }
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value.read.return_value = json.dumps(mock_live).encode("utf-8")
        mock_urlopen.return_value = mock_cm

        res = 适配器.严格校验完场比分(1492374)
        assert res["is_finished"] is False
        assert res["score_text"] == "未完场"

    # 模拟完场比赛 (FT 3:3)
    mock_ft = {
        "response": [{
            "fixture": {"status": {"short": "FT", "long": "Match Finished"}},
            "goals": {"home": 3, "away": 3}
        }]
    }
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value.read.return_value = json.dumps(mock_ft).encode("utf-8")
        mock_urlopen.return_value = mock_cm

        res = 适配器.严格校验完场比分(1492374)
        assert res["is_finished"] is True
        assert res["score_text"] == "3:3"


def test_微观球员适配器提取交锋历史H2H():
    适配器 = 微观球员适配器()
    mock_h2h = {
        "data": {
            "summary": {
                "total_meetings": 10,
                "draws": 4,
                "team1": {"id": "359", "name": "Arsenal", "wins": 4, "goals": 14},
                "team2": {"id": "382", "name": "Man City", "wins": 2, "goals": 10}
            },
            "events": [
                {"home_score": 1, "away_score": 1, "result": "D"}
            ]
        }
    }
    with patch("sports_skills.football.get_head_to_head") as mock_get_h2h:
        mock_get_h2h.return_value = mock_h2h
        res = 适配器.提取交锋历史H2H("359", "382")
        assert res["total_meetings"] == 10
        assert res["draws"] == 4
        assert res["draw_rate"] == 0.40
        assert res["team1_wins"] == 4


def test_微观球员适配器提取球员高阶链条数据():
    适配器 = 微观球员适配器()
    mock_player_stats = {
        "data": {
            "teams": [
                {
                    "team": {"name": "Arsenal"},
                    "players": [
                        {"name": "Saka", "xg": 0.62, "xa": 0.35, "xg_chain": 0.95, "xg_buildup": 0.45, "key_passes": 3}
                    ]
                }
            ]
        }
    }
    with patch("sports_skills.football.get_event_players_statistics") as mock_stats:
        mock_stats.return_value = mock_player_stats
        res = 适配器.提取球员高阶链条数据("401882909")
        assert len(res["key_creators"]) == 1
        assert res["key_creators"][0]["name"] == "Saka"
        assert res["key_creators"][0]["xg_chain"] == 0.95




