import os
import tempfile
import pytest

from 领域.模型 import 赔率数值, 赔率快照
from 适配器.本地账本 import 本地账本仓储


@pytest.fixture
def 临时数据库():
    import gc
    import shutil
    临时目录 = tempfile.mkdtemp()
    账本路径 = os.path.join(临时目录, "测试账本.db")
    yield 账本路径
    gc.collect()
    try:
        shutil.rmtree(临时目录, ignore_errors=True)
    except Exception:
        pass


def test_本地账本仓储保存并检索时序轨迹(临时数据库):
    仓储 = 本地账本仓储(数据库路径=临时数据库)

    s1 = 赔率快照(
        比赛编号="2041321",
        竞彩场次="周一002",
        对阵名称="赫塔费 vs 塞尔塔",
        联赛名称="西甲",
        赔率=赔率数值(主胜=2.50, 平局=3.10, 客胜=2.90),
        记录时间戳=1000,
        官方浮动标记=0
    )
    s2 = 赔率快照(
        比赛编号="2041321",
        竞彩场次="周一002",
        对阵名称="赫塔费 vs 塞尔塔",
        联赛名称="西甲",
        赔率=赔率数值(主胜=2.37, 平局=2.58, 客胜=3.13),
        记录时间戳=2000,
        官方浮动标记=-1
    )

    仓储.批量保存快照([s1, s2])

    轨迹 = 仓储.查询比赛连续轨迹("周一002")
    assert len(轨迹) == 2
    assert 轨迹[0].赔率.平局 == 3.10
    assert 轨迹[1].赔率.平局 == 2.58

    最新 = 仓储.获取最新快照("周一002")
    assert 最新 is not None
    assert 最新.赔率.平局 == 2.58
    assert 最新.官方浮动标记 == -1


def test_本地账本仓储查询空赛事安全返回空(临时数据库):
    仓储 = 本地账本仓储(数据库路径=临时数据库)
    assert 仓储.查询比赛连续轨迹("周日999") == []
    assert 仓储.获取最新快照("周日999") is None
