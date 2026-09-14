import json
from dataclasses import replace
from unittest.mock import MagicMock, patch
import pytest
from 领域.模型 import 赔率数值, 赔率快照, 校验攻防伤停平局资格, 校验让球明牌平局对冲资格
from 适配器.微观球员接口 import 微观球员适配器

@pytest.mark.parametrize('value', [float('nan'), float('inf'), 0, -1, 1])
def test_拒绝非法十进制赔率(value):
    with pytest.raises(ValueError):
        赔率数值(value, 3, 4)

@pytest.mark.parametrize('conceded', [0.79, 0.8, 0.81, 1.45, None])
def test_失球阈值不产生准入或否决(conceded):
    status, reason = 校验让球明牌平局对冲资格(conceded, 2.5, 2.85)
    assert status is None
    assert '待评估' in reason

@pytest.mark.parametrize('rate', [0.48, 0.59, 0.60, 0.61, 0.72, None])
def test_伤停对抗率不直接判定赛果(rate):
    status, reason = 校验攻防伤停平局资格(True, rate)
    assert status is None
    assert '待评估' in reason

def test_不同市场与不同比赛禁止计算虚假位移():
    first = 赔率快照('id', 'code', 'A vs B', 'league', 赔率数值(2, 3, 4), 1000, 0)
    for changed in [replace(first, 比赛编号='other', 记录时间戳=2000),
                    replace(first, 市场类型='hhad', 让球数='-1', 记录时间戳=2000),
                    replace(first, 记录时间戳=999)]:
        with pytest.raises(ValueError):
            changed.计算位移(first)

def test_空赛程不伪造休赛天数():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = b'{"response": []}'
    with patch('urllib.request.urlopen', return_value=response):
        assert 微观球员适配器().计算赛程体能负荷(1, '2026-09-12')['休赛天数'] is None

def test_加时完场取常规时间比分():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = json.dumps({'response': [{
        'fixture': {'status': {'short': 'AET'}}, 'goals': {'home': 2, 'away': 1},
        'score': {'fulltime': {'home': 1, 'away': 1}}
    }]}).encode()
    with patch('urllib.request.urlopen', return_value=response):
        result = 微观球员适配器().严格校验完场比分(1)
        assert result['score_text'] == '1:1'
        assert result['settlement_ready'] is True

def test_让球快照入库回读不丢失市场(tmp_path):
    from 适配器.本地账本 import 本地账本仓储
    store = 本地账本仓储(str(tmp_path / 'odds.db'))
    first = 赔率快照('id', 'code', 'A vs B', 'league', 赔率数值(2, 3, 4), 1000, 0,
                     市场类型='hhad', 让球数='-2')
    store.批量保存快照([first])
    assert store.获取最新快照('code') == first

def test_不会跨周拼接同名场次(tmp_path):
    from 适配器.本地账本 import 本地账本仓储
    store = 本地账本仓储(str(tmp_path / 'odds.db'))
    first = 赔率快照('old', 'code', 'A vs B', 'league', 赔率数值(2, 3, 4), 1000, 0)
    latest = replace(first, 比赛编号='new', 记录时间戳=2000)
    store.批量保存快照([first, latest])
    assert store.查询比赛连续轨迹('code') == [latest]

def test_旧账本迁移保持原赔率并识别让球(tmp_path):
    import sqlite3
    from 适配器.本地账本 import 本地账本仓储
    path = str(tmp_path / 'old.db')
    with sqlite3.connect(path) as conn:
        conn.execute('CREATE TABLE 赔率时序流水 (序号 INTEGER PRIMARY KEY, 比赛编号 TEXT, 竞彩场次 TEXT, 对阵名称 TEXT, 联赛名称 TEXT, 主胜赔率 REAL, 平局赔率 REAL, 客胜赔率 REAL, 记录时间戳 INTEGER, 官方浮动标记 INTEGER)')
        conn.execute("INSERT INTO 赔率时序流水 VALUES (1, 'id', 'code', 'A vs B [让球明牌-2]', 'L', 2, 3, 4, 1000, 0)")
    store = 本地账本仓储(path)
    result = store.获取最新快照('code')
    assert (result.市场类型, result.让球数, result.赔率.平局) == ('hhad', '-2', 3)
    assert 本地账本仓储(path).获取最新快照('code') == result

def test_图谱检查不写文件(tmp_path):
    from 深度联想连线 import 超密集编织图谱
    path = tmp_path / 'graph.json'
    path.write_text('{"nodes": [{"id":"a"}, {"id":"b"}], "links": []}', encoding='utf8')
    original = path.read_bytes()
    assert 超密集编织图谱(path)['边'] == 0
    assert path.read_bytes() == original

def test_无微观数据不变成零进球零犯规():
    with patch('sports_skills.football.get_event_statistics', return_value={}), \
         patch('sports_skills.football.get_event_xg', return_value={}), \
         patch('sports_skills.football.get_event_players_statistics', return_value={}):
        result = 微观球员适配器().提取比赛微观高阶数据('id')
        assert result['team1_xg'] is None
        assert result['team2_fouls'] is None

def test_加时缺常规比分不可结算():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = json.dumps({'response': [{
        'fixture': {'status': {'short': 'AET'}}, 'goals': {'home': 2, 'away': 1}
    }]}).encode()
    with patch('urllib.request.urlopen', return_value=response):
        result = 微观球员适配器().严格校验完场比分(1)
        assert result['is_finished'] is True
        assert result['settlement_ready'] is False
        assert result['home_score'] is None

def test_物理级防孤岛断路器_json与html全网单一连通分量零孤岛():
    import json, re
    from pathlib import Path
    from collections import defaultdict, deque

    # 1. 物理核验 graph.json
    json_path = Path("graphify-out/graph.json")
    assert json_path.exists()
    g = json.loads(json_path.read_text(encoding="utf-8"))
    nodes = {n["id"] for n in g.get("nodes", [])}
    links = g.get("links", g.get("edges", []))
    adj_json = defaultdict(set)
    for l in links:
        s, t = l["source"], l["target"]
        if s in nodes and t in nodes:
            adj_json[s].add(t)
            adj_json[t].add(s)
    visited = set()
    comps = 0
    for n in nodes:
        if n not in visited:
            comps += 1
            q = deque([n])
            visited.add(n)
            while q:
                curr = q.popleft()
                for neighbor in adj_json[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
    assert comps == 1, f"graph.json 存在 {comps} 个割裂连通分量"
    assert all(len(adj_json[n]) > 0 for n in nodes), "graph.json 存在孤岛节点"

    # 2. 物理核验 graph.html
    html_path = Path("graphify-out/graph.html")
    assert html_path.exists()
    html_text = html_path.read_text(encoding="utf-8")
    m_nodes = re.search(r'const RAW_NODES = (\[.*?\]);\s*const RAW_EDGES =', html_text, re.DOTALL)
    m_edges = re.search(r'const RAW_EDGES = (\[.*?\]);\s*const LEGEND =', html_text, re.DOTALL)
    assert m_nodes and m_edges, "graph.html 结构损坏"
    h_nodes = {n["id"] for n in json.loads(m_nodes.group(1))}
    h_edges = json.loads(m_edges.group(1))
    adj_html = defaultdict(set)
    for e in h_edges:
        u, v = e["from"], e["to"]
        if u in h_nodes and v in h_nodes:
            adj_html[u].add(v)
            adj_html[v].add(u)
    visited_h = set()
    comps_h = 0
    for n in h_nodes:
        if n not in visited_h:
            comps_h += 1
            q = deque([n])
            visited_h.add(n)
            while q:
                curr = q.popleft()
                for neighbor in adj_html[curr]:
                    if neighbor not in visited_h:
                        visited_h.add(neighbor)
                        q.append(neighbor)
    assert comps_h == 1, f"graph.html 存在 {comps_h} 个割裂连通分量"
    assert all(len(adj_html[n]) > 0 for n in h_nodes), "graph.html 存在孤岛节点"
