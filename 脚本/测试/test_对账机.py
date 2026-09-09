import os
import re
import json
import pytest
from 对账机 import 刷新总对账看板, RECORD_DIR

def test_对账看板能正常聚合数据并更新总准确率文件():
    res = 刷新总对账看板()
    assert res["days"] >= 3
    assert res["total_picks"] >= 10
    assert res["hit_rate"] >= 0.25
    
    # 验证 总准确率.md 是否真实存在并更新
    acc_path = os.path.join(RECORD_DIR, "总准确率.md")
    assert os.path.exists(acc_path)
    with open(acc_path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    assert m is not None
    data = json.loads(m.group(1))
    assert data["实盘对账天数"] == res["days"]
