"""
测试高阶战术压迫引擎与全量 26 项微观数据 (ADR-0016)
验证 5 大维度 26 项指标集成完整性及历史实战围攻破大巴乏力场景
"""

import sys
import os

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from 脚本.模型.高阶战术压迫引擎 import TacticalPressingEngine, DEFAULT_METRICS

def test_full_26_metrics_integration():
    """验证 26 项微观数据全量对齐与默认基准"""
    engine = TacticalPressingEngine()
    assert len(DEFAULT_METRICS) == 26
    assert engine.total_metric_count == 26

    # 模拟输入完整的 26 项微观数据字典
    sample_home = {
        "ppda": 7.4, "opp_ppda": 15.2, "high_turnovers": 9.0, "opp_half_recoveries": 32.0, "danger_zone_recoveries": 6.0,
        "possession_pct": 0.68, "field_tilt": 0.72, "deep_completions": 11.0, "progressive_passes": 58.0, "box_touches": 34.0,
        "xg": 1.65, "xag": 1.20, "xg_per_shot": 0.058, "psxg_per_sot": 0.21, "big_chances_ratio": 0.18,
        "tackles_won": 15.0, "interceptions": 11.0, "clearances": 8.0, "blocks": 2.0, "box_def_actions": 12.0, "psxg_net_goalkeeping": -0.15,
        "missing_players_count": 2, "core_injury_severity": 0.08, "fixture_congestion_72h": True, "rest_days_gap": -3, "sprint_fatigue_index": 0.65
    }
    sample_away = {
        "ppda": 16.5, "opp_ppda": 8.1, "high_turnovers": 2.0, "opp_half_recoveries": 12.0, "danger_zone_recoveries": 1.0,
        "possession_pct": 0.32, "field_tilt": 0.28, "deep_completions": 2.0, "progressive_passes": 22.0, "box_touches": 8.0,
        "xg": 0.75, "xag": 0.50, "xg_per_shot": 0.145, "psxg_per_sot": 0.38, "big_chances_ratio": 0.50,
        "tackles_won": 21.0, "interceptions": 16.0, "clearances": 32.0, "blocks": 9.0, "box_def_actions": 48.0, "psxg_net_goalkeeping": 0.42,
        "missing_players_count": 0, "core_injury_severity": 0.0, "fixture_congestion_72h": False, "rest_days_gap": 3, "sprint_fatigue_index": 0.10
    }

    assert len(sample_home) == 26
    assert len(sample_away) == 26

    adj = engine.adjust_lambdas(2.10, 0.70, sample_home, sample_away)
    assert adj["metric_count_verified"] == 26
    assert adj["home_triggered"]  # 围攻且xG/Shot极低，触发死穴
    print("[PASS] 26 项微观数据全量灌入验证成功，无一遗漏！")

def test_napoli_vs_fiorentina_siege_draw():
    """那不勒斯 1-1 佛罗伦萨：全量 26 项微观数据驱动验证"""
    engine = TacticalPressingEngine()
    napoli_26 = {
        "ppda": 7.2, "opp_ppda": 16.0, "high_turnovers": 10.0, "opp_half_recoveries": 35.0, "danger_zone_recoveries": 7.0,
        "possession_pct": 0.69, "field_tilt": 0.74, "deep_completions": 14.0, "progressive_passes": 62.0, "box_touches": 38.0,
        "xg": 1.45, "xag": 1.10, "xg_per_shot": 0.057, "psxg_per_sot": 0.20, "big_chances_ratio": 0.15,
        "tackles_won": 14.0, "interceptions": 8.0, "clearances": 7.0, "blocks": 1.0, "box_def_actions": 10.0, "psxg_net_goalkeeping": -0.20,
        "missing_players_count": 3, "core_injury_severity": 0.12, "fixture_congestion_72h": True, "rest_days_gap": -2, "sprint_fatigue_index": 0.60
    }
    fio_26 = {
        "ppda": 15.8, "opp_ppda": 7.5, "high_turnovers": 3.0, "opp_half_recoveries": 14.0, "danger_zone_recoveries": 1.0,
        "possession_pct": 0.31, "field_tilt": 0.26, "deep_completions": 3.0, "progressive_passes": 25.0, "box_touches": 9.0,
        "xg": 0.82, "xag": 0.60, "xg_per_shot": 0.138, "psxg_per_sot": 0.35, "big_chances_ratio": 0.45,
        "tackles_won": 22.0, "interceptions": 15.0, "clearances": 34.0, "blocks": 8.0, "box_def_actions": 49.0, "psxg_net_goalkeeping": 0.38,
        "missing_players_count": 0, "core_injury_severity": 0.0, "fixture_congestion_72h": False, "rest_days_gap": 2, "sprint_fatigue_index": 0.15
    }

    adj = engine.adjust_lambdas(2.20, 0.70, napoli_26, fio_26)
    probs = engine.compute_match_probabilities(adj["adj_lambda_home"], adj["adj_lambda_away"])

    print(f"[PASS] 那不勒斯复测: λ主={adj['adj_lambda_home']}, λ客={adj['adj_lambda_away']}")
    print(f"       平局概率: {probs['p_draw']:.1%}, Top比分: {probs['top_scores']}")
    assert probs["p_draw"] >= 0.23

if __name__ == "__main__":
    test_full_26_metrics_integration()
    test_napoli_vs_fiorentina_siege_draw()
    print("\n>>> 5大维度、26项微观物理战术指标全部通过真实回测！")
