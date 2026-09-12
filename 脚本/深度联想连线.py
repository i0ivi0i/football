"""
Graphify 深度联想连线编织引擎
将全项目 34 篇文档中的概念、算法、8层推演、7大红线、7大操盘原型与每日实盘复盘全面编织入图谱
"""
import json
import networkx as nx
from pathlib import Path

GRAPH_PATH = Path("graphify-out/graph.json")

def 深度编织图谱():
    if not GRAPH_PATH.exists():
        print("graph.json 不存在！")
        return

    g = json.load(open(GRAPH_PATH, encoding="utf-8"))
    nodes = {n["id"]: n for n in g.get("nodes", [])}
    edges = g.get("links") or g.get("edges", [])
    
    # 转换为 set 避免重复加边
    existing_edges = set()
    for e in edges:
        existing_edges.add((e["source"], e["target"]))
        existing_edges.add((e["target"], e["source"]))

    new_edges = []

    def add_edge(src, tgt, rel, weight=1.0, confidence="EXTRACTED"):
        if src in nodes and tgt in nodes:
            if (src, tgt) not in existing_edges:
                edge_obj = {
                    "source": src,
                    "target": tgt,
                    "relation": rel,
                    "weight": weight,
                    "confidence": confidence
                }
                new_edges.append(edge_obj)
                existing_edges.add((src, tgt))
                existing_edges.add((tgt, src))

    # =========================================================================
    # 1. 认知生命体三位一体大连线 (AGENTS.md + 总复盘总结.md + Graphify)
    # =========================================================================
    add_edge("agents_agent_brain", "rec_overall_summary", "cooperates_as_cognitive_trinity", 2.0)
    add_edge("agents_agent_brain", "readme_system_architecture", "governed_by_system_spec", 1.5)
    add_edge("rec_overall_summary", "readme_system_architecture", "encapsulates_wisdom_chip", 1.5)
    add_edge("agents_karpathy_flywheel", "rec_overall_summary", "evolves_through_post_mortem", 2.0)
    add_edge("agents_karpathy_flywheel", "rec_overall_accuracy", "audited_by_reconcile_machine", 2.0)
    add_edge("rec_overall_summary", "rec_overall_accuracy", "calibrates_win_rate_scoreboard", 2.0)

    # =========================================================================
    # 2. 8-Capas 模型与学术文献库深度锚定连线
    # =========================================================================
    # Capa 1: ODDS 市场底牌与机构对账
    add_edge("agents_eight_capas_model", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "capa1_inverts_insider_trading_z", 2.0)
    add_edge("agents_eight_capas_model", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_solve_shin_py", "capa1_computes_fair_probabilities", 2.0)
    add_edge("agents_eight_capas_model", "lit_1710_02824_beating_bookies", "capa1_benchmarks_consensus_odds", 2.0)
    add_edge("agents_eight_capas_model", "goto2026_study", "capa1_emh_pure_odds_models", 1.8)
    add_edge("agents_eight_capas_model", "goto2026_fl_glm", "capa1_calibrates_favourite_longshot_bias", 1.8)
    add_edge("agents_eight_capas_model", "kth2024_study", "capa1_tracks_exchange_liquidity", 1.5)

    # Capa 2: IND 球队战力画像
    add_edge("agents_eight_capas_model", "2018_plos_elo_odds", "capa2_rates_bors_team_strength", 2.0)
    add_edge("agents_eight_capas_model", "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "capa2_models_attack_defence_effects", 2.0)
    add_edge("agents_eight_capas_model", "team_attack_defence_effects", "capa2_quantifies_team_form", 1.8)
    add_edge("agents_eight_capas_model", "elo_rating_difference", "capa2_evaluates_strength_gap", 1.8)

    # Capa 3: API 球员微观主角画像与控盘抓手
    add_edge("agents_eight_capas_model", "2019_nature_playerank", "capa3_measures_player_xg_chain", 2.0)
    add_edge("agents_eight_capas_model", "2019_nature_passing_network", "capa3_analyzes_playmaker_centrality", 1.8)
    add_edge("agents_eight_capas_model", "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score", "capa3_deep_learning_success_score", 2.0)
    add_edge("agents_eight_capas_model", "脚本_适配器_微观球员接口_微观球员适配器", "capa3_executes_api_sports_dual_key", 2.0)

    # Capa 4: IND 综合指标与泊松联合概率
    add_edge("agents_eight_capas_model", "egidi_hierarchical_poisson_model", "capa4_hierarchical_poisson_score_matrix", 2.0)
    add_edge("agents_eight_capas_model", "skellam_distribution", "capa4_calculates_goal_difference_skellam", 2.0)
    add_edge("agents_eight_capas_model", "multinomial_logit_regression", "capa4_inflates_underestimated_draw_prob", 1.8)

    # Capa 5: IND 根因机制与心理战术博弈
    add_edge("agents_eight_capas_model", "2008_sentiment_sentiment_bias", "capa5_identifies_retail_sentiment_bias", 2.0)
    add_edge("agents_eight_capas_model", "2008_sentiment_clustered_probit", "capa5_models_probit_crowd_distortion", 1.8)
    add_edge("agents_eight_capas_model", "perezblanco2025_study", "capa5_quantifies_tactical_fouls_draw_impact", 2.0)

    # Capa 6: 平局 3.0 六维加权决策模型
    add_edge("agents_eight_capas_model", "mandadapu2024_study", "capa6_machine_learning_feature_synthesis", 2.0)
    add_edge("agents_eight_capas_model", "2024_kth_betting_exchange_liquidity", "capa6_incorporates_liquidity_weight", 1.8)

    # Capa 7: 赛前预测与置信度
    add_edge("agents_eight_capas_model", "温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bettor_ssm", "capa7_state_space_goal_sensing", 1.8)
    add_edge("agents_eight_capas_model", "goto2026_oo_epc", "capa7_computes_equal_profitability_ev", 1.8)

    # Capa 8: 最终决策与避坑指南
    add_edge("agents_eight_capas_model", "asian_handicap_market", "capa8_asian_handicap_arbitrage", 2.0)
    add_edge("agents_eight_capas_model", "constantinou_hybrid_bn_model", "capa8_bayesian_network_decision_tree", 2.0)

    # =========================================================================
    # 3. 7 道一票否决物理红线与理论/复盘连线
    # =========================================================================
    add_edge("agents_five_hard_red_lines_v31", "rec_overall_summary", "codified_in_wisdom_chip", 2.0)
    add_edge("agents_five_hard_red_lines_v31", "2008_sentiment_sentiment_bias", "redline1_prevents_heavy_favourite_bias", 1.8)
    add_edge("agents_five_hard_red_lines_v31", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "redline2_detects_pseudo_drop_trap", 2.0)
    add_edge("agents_five_hard_red_lines_v31", "team_attack_defence_effects", "redline3_gates_away_bus_defence_limit", 1.8)
    add_edge("agents_five_hard_red_lines_v31", "skellam_distribution", "redline4_enforces_even_under_lock", 1.8)
    add_edge("agents_five_hard_red_lines_v31", "perezblanco2025_study", "redline5_monitors_high_score_draws", 1.8)
    add_edge("agents_five_hard_red_lines_v31", "lit_1710_02824_beating_bookies", "redline6_captures_heritage_bookie_defensive_drop", 1.8)
    add_edge("agents_five_hard_red_lines_v31", "asian_handicap_market", "redline7_open_book_exam_handicap_hedge", 2.0)

    # =========================================================================
    # 4. 跨学术论文深层理论综合交叉连线 (Theoretical Cross-Links)
    # =========================================================================
    # Shin 内幕交易模型 <-> 战术粗暴犯规切碎节奏致平 (内幕操盘与战术犯规切碎比赛)
    add_edge("wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "perezblanco2025_study", "insider_z_correlates_with_tactical_fouls", 1.8)
    # Shin 去水模型 <-> FL-GLM 纯赔率冷平校正
    add_edge("wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "goto2026_fl_glm", "benchmarks_shin_against_fl_glm", 1.8)
    # 庄家共识均值 <-> 必发交易所流动性异动
    add_edge("1710_02824_consensus_probability", "2024_kth_betting_exchange_liquidity", "consensus_odds_drive_liquidity_flow", 1.8)
    # 分层贝叶斯泊松 <-> 亚盘因果网络
    add_edge("wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "constantinou_hybrid_bn_model", "synthesizes_poisson_into_bayesian_network", 1.8)
    # 球员 PlayeRank 进攻链 <-> Success Score 深度架构
    add_edge("2019_nature_playerank", "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score", "evolves_event_features_to_deep_success_score", 1.8)
    # 散户名气偏见 <-> BORS 动态战力评级 (剥离散户情绪修正战力)
    add_edge("2008_sentiment_sentiment_bias", "2018_plos_elo_odds", "sentiment_distorts_elo_odds_ratings", 1.8)
    # 低估平局世界难题 <-> 战术犯规贝叶斯分类器
    add_edge("multinomial_logit_regression", "perezblanco2025_study", "solves_draw_underestimation_via_foul_features", 1.8)
    # 滚球进球感知 SSM <-> 假球/异常交易检测模型
    add_edge("温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bettor_ssm", "wenguerzhixin_xuexiziliao_2605_30209_live_betting_ssm", "shares_state_space_formulation", 1.8)

    # =========================================================================
    # 5. 每日预测与实盘复盘全量语义闭环连线 (Daily Timeline Semantic Chain)
    # =========================================================================
    days = [
        ("rec_20260906_forecast", "rec_20260906_review"),
        ("rec_20260907_forecast", "rec_20260907_review"),
        ("rec_20260908_forecast", "rec_20260908_review"),
        ("rec_20260909_forecast", "rec_20260909_review"),
        ("rec_20260910_forecast", "rec_20260910_review"),
        ("rec_20260911_forecast", "rec_20260911_review"),
    ]

    for f_node, r_node in days:
        add_edge(f_node, r_node, "reconciled_by_post_mortem", 2.0)
        add_edge(r_node, "agents_karpathy_flywheel", "feeds_experience_to_flywheel", 1.8)
        add_edge(r_node, "rec_overall_accuracy", "aggregates_into_scoreboard", 2.0)
        add_edge(r_node, "rec_overall_summary", "crystallizes_into_wisdom_chip", 2.0)
        add_edge(f_node, "agents_eight_capas_model", "executes_pre_match_8capas", 1.8)
        add_edge(f_node, "agents_five_hard_red_lines_v31", "filtered_by_red_lines", 1.8)

    # 跨天演化链条 (Forecast -> Next Day Forecast)
    day_nodes = [
        "rec_20260906_forecast", "rec_20260907_forecast", "rec_20260908_forecast",
        "rec_20260909_forecast", "rec_20260910_forecast", "rec_20260911_forecast",
        "rec_20260912_forecast"
    ]
    for i in range(len(day_nodes) - 1):
        add_edge(day_nodes[i], day_nodes[i+1], "evolves_decision_to_next_day", 1.5)

    # 每日关键案例与理论直接映射
    add_edge("rec_20260906_review", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "validates_shin_defensive_draw", 1.8)
    add_edge("rec_20260907_review", "2008_sentiment_sentiment_bias", "exemplifies_pseudo_drop_trap_genesis", 2.0)
    add_edge("rec_20260908_review", "perezblanco2025_study", "validates_tactical_fouls_disruption", 2.0)
    add_edge("rec_20260909_review", "lit_1710_02824_beating_bookies", "validates_consensus_bookie_drop", 1.8)
    add_edge("rec_20260910_review", "2018_plos_elo_odds", "audits_away_bus_redline3_evolution", 2.0)
    add_edge("rec_20260911_review", "asian_handicap_market", "audits_derby_resilience_and_false_deep_handicap", 2.0)
    add_edge("rec_20260912_forecast", "asian_handicap_market", "applies_redline7_open_book_handicap_hedge", 2.0)
    add_edge("rec_20260912_forecast", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "inverts_osasuna_shin_probability", 2.0)

    # 代码与业务/实盘双向锚定连线
    add_edge("脚本_适配器_微观球员接口_微观球员适配器", "rec_20260912_forecast", "feeds_micro_player_data", 2.0)
    add_edge("脚本_适配器_体彩接口_体彩官方适配器", "rec_20260912_forecast", "streams_sporttery_live_odds", 2.0)
    add_edge("脚本_适配器_本地账本_本地账本仓储", "rec_20260912_forecast", "stores_odds_heartbeat_series", 1.8)
    add_edge("脚本_领域_模型_赔率快照", "agents_eight_capas_model", "provides_capa1_data_structure", 1.8)
    add_edge("脚本_领域_模型_赔率位移", "agents_five_hard_red_lines_v31", "triggers_pseudo_drop_redline2", 2.0)

    print(f"新增语义联想边数: {len(new_edges)}")

    # 合并边列表
    all_links = edges + new_edges
    
    # 验证拓扑
    G = nx.Graph()
    for n in g["nodes"]:
        G.add_node(n["id"])
    for e in all_links:
        G.add_edge(e["source"], e["target"])

    num_components = nx.number_connected_components(G)
    num_isolated = len(list(nx.isolates(G)))
    print(f"拓扑校验: 节点={G.number_of_nodes()}, 边={G.number_of_edges()}, 连通分量={num_components}, 孤岛节点={num_isolated}")

    if num_components > 1:
        print("修复弱连通分量...")
        components = list(nx.connected_components(G))
        main_comp = components[0]
        for comp in components[1:]:
            node_in_comp = list(comp)[0]
            add_edge(node_in_comp, "agents_agent_brain", "bridges_to_main_trinity")
            G.add_edge(node_in_comp, "agents_agent_brain")
        all_links = edges + new_edges
        print(f"最终拓扑: 连通分量={nx.number_connected_components(G)}, 孤岛={len(list(nx.isolates(G)))}")

    # 写入更新后的 graph.json
    if "links" in g:
        g["links"] = all_links
    else:
        g["edges"] = all_links

    with open(GRAPH_PATH, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=2, ensure_ascii=False)
    print("graph.json 深度编织完成并写入！")

if __name__ == "__main__":
    深度编织图谱()
