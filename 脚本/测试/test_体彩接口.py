import pytest
from 适配器.体彩接口 import 体彩官方适配器
from 领域.模型 import 赔率快照


def test_体彩官方适配器解析原始数据为纯净领域快照():
    伪造体彩网关报文 = {
        "value": {
            "matchInfoList": [
                {
                    "subMatchList": [
                        {
                            "matchId": 2041321,
                            "matchNumStr": "周一002",
                            "homeTeamAbbName": "赫塔费",
                            "awayTeamAbbName": "塞尔塔",
                            "leagueAbbName": "西甲",
                            "had": {
                                "h": "2.37",
                                "d": "2.58",
                                "a": "3.13",
                                "df": "-1",
                                "updateDate": "2026-09-07",
                                "updateTime": "09:44:25"
                            }
                        }
                    ]
                }
            ]
        }
    }

    适配器 = 体彩官方适配器()
    快照列表 = 适配器.解析原始数据(伪造体彩网关报文, 自定义时间戳=1700000000)

    assert len(快照列表) == 1
    快照 = 快照列表[0]
    assert 快照.比赛编号 == "2041321"
    assert 快照.竞彩场次 == "周一002"
    assert 快照.对阵名称 == "赫塔费 vs 塞尔塔"
    assert 快照.联赛名称 == "西甲"
    assert 快照.赔率.主胜 == 2.37
    assert 快照.赔率.平局 == 2.58
    assert 快照.赔率.客胜 == 3.13


def test_体彩官方适配器在基础胜平负关闭时自动捕获让球明牌():
    伪造体彩网关关闭HAD报文 = {
        "value": {
            "matchInfoList": [
                {
                    "subMatchList": [
                        {
                            "matchId": 2041432,
                            "matchNumStr": "周六030",
                            "homeTeamAbbName": "皇马",
                            "awayTeamAbbName": "巴列卡诺",
                            "leagueAbbName": "西甲",
                            "had": {},
                            "hhad": {
                                "goalLine": "-2",
                                "h": "1.72",
                                "d": "4.40",
                                "a": "3.15",
                                "df": "0",
                                "updateDate": "2026-09-12",
                                "updateTime": "12:24:51"
                            }
                        }
                    ]
                }
            ]
        }
    }

    适配器 = 体彩官方适配器()
    快照列表 = 适配器.解析原始数据(伪造体彩网关关闭HAD报文, 自定义时间戳=1789205500)

    assert len(快照列表) == 1
    快照 = 快照列表[0]
    assert 快照.竞彩场次 == "周六030"
    assert 快照.对阵名称 == "皇马 vs 巴列卡诺 [让球明牌-2]"
    assert 快照.赔率.主胜 == 1.72
    assert 快照.赔率.平局 == 4.40
    assert 快照.赔率.客胜 == 3.15
    assert 快照.官方浮动标记 == 0
    assert 快照.记录时间戳 == 1789205500


def test_体彩官方适配器安全过滤无赔率异常赛事():
    伪造未开盘报文 = {
        "value": {
            "matchInfoList": [
                {
                    "subMatchList": [
                        {
                            "matchId": 9999999,
                            "matchNumStr": "周一099",
                            "homeTeamAbbName": "测试队A",
                            "awayTeamAbbName": "测试队B",
                            "leagueAbbName": "友谊赛",
                            "had": None
                        }
                    ]
                }
            ]
        }
    }
    适配器 = 体彩官方适配器()
    快照列表 = 适配器.解析原始数据(伪造未开盘报文)
    assert len(快照列表) == 0
