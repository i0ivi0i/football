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
