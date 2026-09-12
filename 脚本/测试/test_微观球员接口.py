import pytest
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


