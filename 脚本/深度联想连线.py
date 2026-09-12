"""
全量超密集知识图谱编织引擎 (Graphify Ultra-Dense Semantic Mesh Synthesizer)
将全项目 34 篇文档的理论、算法、推演、红线、原型、实盘、对账机与代码全面编织入图谱
"""
import json
import networkx as nx
from pathlib import Path

GRAPH_PATH = Path("graphify-out/graph.json")

def 超密集编织图谱():
    if not GRAPH_PATH.exists():
        print("graph.json 不存在！")
        return

    g = json.load(open(GRAPH_PATH, encoding="utf-8"))
    nodes = {n["id"]: n for n in g.get("nodes", [])}
    edges = g.get("links") or g.get("edges", [])
    
    existing_edges = set()
    for e in edges:
        existing_edges.add((e["source"], e["target"]))
        existing_edges.add((e["target"], e["source"]))

    new_edges = []

    def add_edge(src, tgt, rel, weight=1.0, confidence="INFERRED"):
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
    # 1. 理论全互联矩阵 (Theoretical Comprehensive Interlinks)
    # =========================================================================
    theory_nodes = [
        "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model",
        "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_solve_shin_py",
        "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model",
        "egidi_hierarchical_poisson_model",
        "skellam_distribution",
        "team_attack_defence_effects",
        "shin_normalization",
        "constantinou_hybrid_bn_model",
        "modified_pi_rating_system",
        "asian_handicap_market",
        "2008_sentiment_sentiment_bias",
        "2008_sentiment_clustered_probit",
        "2008_sentiment_diffattend",
        "multinomial_logit_regression",
        "ordered_logit_regression",
        "elo_rating_difference",
        "温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_draw_prediction_evaluation",
        "温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_olr_model",
        "2018_plos_elo_odds",
        "2018_plos_elo_goals",
        "2018_plos_elo_result",
        "2018_plos_informational_loss",
        "2019_nature_playerank",
        "2019_nature_passing_network",
        "2019_nature_wyscout_soccer_logs",
        "kth2024_study",
        "2024_kth_betting_exchange_liquidity",
        "kth2024_random_forest",
        "kth2024_mlp",
        "kth2024_svm",
        "perezblanco2025_study",
        "perezblanco2025_two_tier_nb_clustering",
        "perezblanco2025_relative_distance_discretization",
        "perezblanco2025_rps",
        "perezblanco2025_wap_war",
        "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score",
        "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_dnn_model",
        "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_match_outcome_classification",
        "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_tactical_play_styles",
        "mandadapu2024_study",
        "mandadapu2024_xgboost",
        "mandadapu2024_svm",
        "温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bettor_ssm",
        "温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bookmaker_odds_model",
        "goto2026_study",
        "goto2026_fl_glm",
        "goto2026_oo_epc",
        "concept_favourite_longshot_bias",
        "wenguerzhixin_xuexiziliao_2604_17194_draw_bias_finding",
        "wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion",
        "wenguerzhixin_xuexiziliao_2604_17194_analytical_shin_conversion",
        "wenguerzhixin_xuexiziliao_2604_17194_power_conversion",
        "wenguerzhixin_xuexiziliao_2604_17194_multiplicative_conversion",
        "wenguerzhixin_xuexiziliao_2605_30209_live_betting_ssm",
        "wenguerzhixin_xuexiziliao_2605_30209_hurdle_lognormal_model",
        "lit_1710_02824_beating_bookies",
        "1710_02824_consensus_probability",
        "1710_02824_betting_strategy",
        "1710_02824_paper_trading",
        "1710_02824_bookmaker_restrictions"
    ]

    # Shin 算法体系深度横向交织
    for t in ["2018_plos_elo_odds", "constantinou_hybrid_bn_model", "asian_handicap_market", 
              "1710_02824_consensus_probability", "2008_sentiment_sentiment_bias", 
              "wenguerzhixin_xuexiziliao_2605_30209_live_betting_ssm", "wenguerzhixin_xuexiziliao_2604_17194_draw_bias_finding"]:
        add_edge("wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", t, "cross_theoretical_synthesis", 1.8)

    # 泊松分布与进球模拟体系
    for t in ["constantinou_hybrid_bn_model", "modified_pi_rating_system", "2018_plos_elo_goals", 
              "ordered_logit_regression", "multinomial_logit_regression", "perezblanco2025_study"]:
        add_edge("wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", t, "cross_poisson_synthesis", 1.8)
        add_edge("skellam_distribution", t, "skellam_goal_difference_mapping", 1.8)

    # 球员微观体系 (PlayeRank + Success Score)
    for t in ["team_attack_defence_effects", "perezblanco2025_study", "mandadapu2024_study", "constantinou_hybrid_bn_model"]:
        add_edge("2019_nature_playerank", t, "player_micro_to_team_impact", 1.8)
        add_edge("温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score", t, "success_score_to_match_outcome", 1.8)

    # 市场博弈与散户偏差体系
    for t in ["goto2026_study", "kth2024_study", "wenguerzhixin_xuexiziliao_2605_30209_live_betting_ssm", "asian_handicap_market"]:
        add_edge("2008_sentiment_sentiment_bias", t, "sentiment_market_distortion", 1.8)
        add_edge("lit_1710_02824_beating_bookies", t, "market_efficiency_exploitation", 1.8)
        add_edge("concept_favourite_longshot_bias", t, "favourite_longshot_bias_impact", 1.8)

    # =========================================================================
    # 2. 8-Capas 模型与所有实盘日期的全景连线 (Every Date connects to Capas)
    # =========================================================================
    all_forecasts = [
        "rec_20260906_forecast", "rec_20260907_forecast", "rec_20260908_forecast",
        "rec_20260909_forecast", "rec_20260910_forecast", "rec_20260911_forecast",
        "rec_20260912_forecast"
    ]
    all_reviews = [
        "rec_20260906_review", "rec_20260907_review", "rec_20260908_review",
        "rec_20260909_review", "rec_20260910_review", "rec_20260911_review"
    ]

    for f_node in all_forecasts:
        # 每个预测都调用 8 层模型
        add_edge(f_node, "agents_eight_capas_model", "executes_8capas_pre_match", 2.0)
        add_edge(f_node, "agents_five_hard_red_lines_v31", "screened_by_red_lines", 2.0)
        add_edge(f_node, "rec_overall_summary", "aligns_with_wisdom_chip", 2.0)
        add_edge(f_node, "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "applies_capa1_shin_devigging", 1.8)
        add_edge(f_node, "2018_plos_elo_odds", "applies_capa2_bors_rating", 1.8)
        add_edge(f_node, "2019_nature_playerank", "applies_capa3_playerank_audit", 1.8)
        add_edge(f_node, "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "applies_capa4_poisson_matrix", 1.8)
        add_edge(f_node, "perezblanco2025_study", "applies_capa5_tactical_fouls", 1.8)
        add_edge(f_node, "mandadapu2024_study", "applies_capa6_draw30_scoring", 1.8)
        add_edge(f_node, "goto2026_oo_epc", "applies_capa7_ev_confidence", 1.8)
        add_edge(f_node, "asian_handicap_market", "applies_capa8_handicap_hedge", 1.8)

    for r_node in all_reviews:
        # 每个复盘都回传飞轮、战绩与总结
        add_edge(r_node, "agents_karpathy_flywheel", "feeds_post_mortem_lessons", 2.0)
        add_edge(r_node, "rec_overall_summary", "enriches_seven_archetypes", 2.0)
        add_edge(r_node, "rec_overall_accuracy", "reconciled_by_audit_engine", 2.0)
        add_edge(r_node, "agents_five_hard_red_lines_v31", "hardens_circuit_breakers", 2.0)
        add_edge(r_node, "2008_sentiment_sentiment_bias", "audits_market_sentiment_distortion", 1.8)
        add_edge(r_node, "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "validates_insider_z_effectiveness", 1.8)

    # =========================================================================
    # 3. 详细复盘子模块与理论节点的深度编织 (Sub-section Granular Mesh)
    # =========================================================================
    sub_sections = [
        # 09-11 复盘子节点
        ("分析复盘记录_2026_09_11_复盘_1_周五012_科里蒂巴_1_3_巴拉纳竞技_触犯自身红线_2_的致命_伪降水_失误", "agents_five_hard_red_lines_v31", "corrected_by_derby_resilience_exemption"),
        ("分析复盘记录_2026_09_11_复盘_1_周五012_科里蒂巴_1_3_巴拉纳竞技_触犯自身红线_2_的致命_伪降水_失误", "skellam_distribution", "models_3_3_high_score_draw"),
        ("分析复盘记录_2026_09_11_复盘_2_周五011_塞维利亚_1_0_巴伦西亚_进球前置锁正确但终结能力严重失衡", "2019_nature_playerank", "reveals_finishing_drought_flaw"),
        ("分析复盘记录_2026_09_11_复盘_二_漏网盲区深度审计_周五004_赫根_1_1_米亚尔比", "agents_five_hard_red_lines_v31", "creates_redline1_false_deep_handicap_exemption"),
        ("分析复盘记录_2026_09_11_复盘_二_漏网盲区深度审计_周五004_赫根_1_1_米亚尔比", "asian_handicap_market", "identifies_false_deep_handicap_arbitrage"),
        ("分析复盘记录_2026_09_11_复盘_三_闭环演化_两道物理级断路器系统升级_写入代码与大脑", "agents_karpathy_flywheel", "flywheel_evolution_milestone"),

        # 09-10 复盘子节点
        ("分析复盘记录_2026_09_10_复盘_一_唯一平局漏网盲区深度审计_周四001_费内巴切_1_1_罗马", "lit_1710_02824_beating_bookies", "reveals_william_hill_heritage_drop"),
        ("分析复盘记录_2026_09_10_复盘_一_唯一平局漏网盲区深度审计_周四001_费内巴切_1_1_罗马", "agents_five_hard_red_lines_v31", "creates_redline6_heritage_bookie_drop"),
        ("分析复盘记录_2026_09_10_复盘_二_周四007_德尔瓦耶_0_2_弗拉门戈_单挑失手深度复盘", "2008_sentiment_sentiment_bias", "audits_cup_motivation_bias"),
        ("分析复盘记录_2026_09_10_复盘_根因一_机械教条主义滥用_红线_4_前置条件校验严重缺失", "agents_five_hard_red_lines_v31", "restricts_redline4_to_even_odds"),

        # 09-09 复盘子节点
        ("分析复盘记录_2026_09_09_复盘_1_周三001_江原fc_1_1_全北现代_赛果_平局_1_1_体彩平赔_2_92", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "validates_sporttery_defensive_drop_292"),
        ("分析复盘记录_2026_09_09_复盘_2_周三014_拉普拉塔大学_1_1_科林蒂安_赛果_平局_1_1_体彩平赔_2_58", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "validates_sporttery_defensive_drop_258"),
        ("分析复盘记录_2026_09_09_复盘_二_五道硬红线_3_1_版排雷审计_9场分胜负全量排雷成功", "agents_five_hard_red_lines_v31", "verifies_100_percent_win_draw_exclusion")
    ]

    for src, tgt, rel in sub_sections:
        add_edge(src, tgt, rel, 1.8)

    # =========================================================================
    # 4. 代码层与学术/复盘的密集突触连线 (Dense Code Infrastructure Links)
    # =========================================================================
    code_nodes = [
        "脚本_适配器_微观球员接口_微观球员适配器",
        "脚本_适配器_体彩接口_体彩官方适配器",
        "脚本_适配器_本地账本_本地账本仓储",
        "脚本_领域_模型_赔率快照",
        "脚本_领域_模型_赔率位移",
        "脚本_领域_模型_赔率数值",
        "脚本_应用_用例_探测并记录心电图用例",
        "脚本_应用_用例_回溯连续轨迹用例",
        "脚本_应用_用例_记录结果",
        "脚本_应用_用例_轨迹结果",
        "脚本_领域_契约_赔率提供者契约",
        "脚本_领域_契约_赔率账本契约"
    ]

    for c in code_nodes:
        add_edge(c, "readme_system_architecture", "part_of_ddd_onion_architecture", 1.8)
        add_edge(c, "agents_agent_brain", "controlled_by_brain", 1.8)

    # 适配器直接驱动核心文献模型
    add_edge("脚本_适配器_体彩接口_体彩官方适配器", "1710_02824_consensus_probability", "feeds_sporttery_odds_stream", 2.0)
    add_edge("脚本_适配器_微观球员接口_微观球员适配器", "team_attack_defence_effects", "updates_team_micro_parameters", 1.8)
    add_edge("脚本_适配器_本地账本_本地账本仓储", "2024_kth_betting_exchange_liquidity", "persists_order_flow_time_series", 1.8)
    add_edge("脚本_领域_模型_赔率位移", "concept_favourite_longshot_bias", "detects_favourite_longshot_drift", 1.8)
    add_edge("脚本_领域_模型_赔率快照", "wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion", "calculates_shin_fair_prob", 2.0)

    # =========================================================================
    # 5. AST 函数/方法与宏观业务逻辑、红线及理论的物理突触 (AST Method-to-Concept Bridges)
    # =========================================================================
    ast_concept_bridges = [
        ("脚本_测试_test_领域模型_test_认知大脑与总复盘防流水账与零污染", "agents_agent_brain", "physically_guards_brain_purity"),
        ("脚本_测试_test_领域模型_test_认知大脑与总复盘防流水账与零污染", "rec_overall_summary", "physically_guards_wisdom_chip_purity"),
        ("脚本_测试_test_领域模型_test_赔率数值验证与去水计算", "wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model", "tests_shin_devigging_logic"),
        ("脚本_测试_test_领域模型_test_赔率数值验证与去水计算", "agents_eight_capas_model", "validates_capa1_probability_computation"),
        ("脚本_领域_模型_赔率位移_是否显著防守降水", "agents_five_hard_red_lines_v31", "distinguishes_real_defensive_drop_from_pseudo_drop"),
        ("脚本_领域_模型_赔率位移_是否显著防守降水", "lit_1710_02824_beating_bookies", "identifies_consensus_defensive_pressure"),
        ("脚本_适配器_本地账本_本地账本仓储_批量保存快照", "agents_karpathy_flywheel", "executes_snapshot_stream_persistence"),
        ("脚本_适配器_本地账本_本地账本仓储_批量保存快照", "2024_kth_betting_exchange_liquidity", "stores_tick_level_liquidity_data"),
        ("脚本_测试_test_微观球员接口_test_微观球员适配器提取交锋历史H2H", "agents_eight_capas_model", "tests_capa2_h2h_extraction"),
        ("脚本_测试_test_微观球员接口_test_微观球员适配器提取球员高阶链条数据", "2019_nature_playerank", "tests_capa3_xg_chain_extraction"),
        ("脚本_测试_test_微观球员接口_test_微观球员适配器提取球员高阶链条数据", "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score", "tests_capa3_deep_success_metrics"),
        ("脚本_测试_test_微观球员接口_test_微观球员适配器严格断言完场比分", "agents_karpathy_flywheel", "guards_reconciliation_integrity_with_ft_lock"),
        ("脚本_测试_test_微观球员接口_test_微观球员适配器严格断言完场比分", "rec_overall_accuracy", "prevents_hallucinatory_reviews_on_live_matches"),
        ("脚本_应用_用例_探测并记录心电图用例", "脚本_适配器_体彩接口_体彩官方适配器", "orchestrates_live_heartbeat_capture"),
        ("脚本_应用_用例_回溯连续轨迹用例", "脚本_适配器_本地账本_本地账本仓储", "orchestrates_heartbeat_trend_query"),
        ("脚本_测试_test_业务用例_test_探测并记录心电图用例捕获异动跳水", "agents_eight_capas_model", "validates_heartbeat_abnormal_drop_detection"),
        ("脚本_测试_test_业务用例_test_回溯连续轨迹用例提炼单边变盘态势", "kth2024_study", "validates_time_series_displacement_trend")
    ]

    for src, tgt, rel in ast_concept_bridges:
        add_edge(src, tgt, rel, 1.8)

    print(f"超密集编织：新增高级语义边数: {len(new_edges)}")

    all_links = edges + new_edges
    
    G = nx.Graph()
    for n in g["nodes"]:
        G.add_node(n["id"])
    for e in all_links:
        G.add_edge(e["source"], e["target"])

    num_components = nx.number_connected_components(G)
    num_isolated = len(list(nx.isolates(G)))
    print(f"超密集拓扑校验: 节点={G.number_of_nodes()}, 边={G.number_of_edges()}, 连通分量={num_components}, 孤岛节点={num_isolated}")

    if num_components > 1:
        print("修复弱连通分量...")
        components = list(nx.connected_components(G))
        for comp in components[1:]:
            node_in_comp = list(comp)[0]
            add_edge(node_in_comp, "agents_agent_brain", "bridges_to_main_trinity")
            G.add_edge(node_in_comp, "agents_agent_brain")
        all_links = edges + new_edges
        print(f"最终拓扑: 连通分量={nx.number_connected_components(G)}, 孤岛={len(list(nx.isolates(G)))}")

    if "links" in g:
        g["links"] = all_links
    else:
        g["edges"] = all_links

    with open(GRAPH_PATH, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=2, ensure_ascii=False)
    print("graph.json 超密集编织完成并写入！")

if __name__ == "__main__":
    超密集编织图谱()
