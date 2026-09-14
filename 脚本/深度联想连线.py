"""
深度联想连线机 (Deep Associative Weaver)
=====================================
负责在 535 个全景知识节点之间进行高密度、严谨的跨学科语义编织：
- 24 篇顶刊学术文献（Shin 1993, Strumbelj 2014, BORS 2018, Nature PlayeRank 2019, 
  Springer 2025, KTH 2024, Giacomini 2006, Wheatcroft 2019, Dimitriadis 2021, 
  Aiyer 2023, Choe 2023, Hewamalage 2023, Macri 2025, Wilkens 2026 等）
- 8 层精算推演体系 (8-Capas)
- 7 类条件复核准则 (替代死板一票否决)
- 乔布斯极简产品思维与灵活智慧复盘
- 8 天全量赛前预测与赛后深度盲区审计报告 (2026-09-06 至 2026-09-13)
- DDD 领域模型、用例与测试守卫 AST 方法

基于 Python 原生标准库实现图连通与拓扑遍历，零外部依赖（彻底免除 networkx 依赖）。
"""

import json
from pathlib import Path
from collections import defaultdict, deque

GRAPH_PATH = Path(__file__).resolve().parent.parent / "graphify-out/graph.json"


def 计算连通分量与孤岛(node_ids, edges):
    """纯 Python 标准库实现的广度优先搜索 (BFS) 图连通性算法"""
    adj = defaultdict(set)
    for e in edges:
        s, t = e["source"], e["target"]
        if s in node_ids and t in node_ids:
            adj[s].add(t)
            adj[t].add(s)
            
    visited = set()
    components = []
    for n in node_ids:
        if n not in visited:
            comp = set()
            q = deque([n])
            visited.add(n)
            while q:
                curr = q.popleft()
                comp.add(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            components.append(comp)
            
    isolates = [n for n in node_ids if len(adj[n]) == 0]
    return components, isolates


def 超密集编织图谱(图谱路径=None, 是否落盘=None):
    """
    深度语义编织执行引擎。
    若传入自定义图谱路径且未显式指定是否落盘，则默认纯计算不写文件，保护测试隔离。
    """
    path = Path(图谱路径 or GRAPH_PATH)
    if not path.exists():
        return {"节点": 0, "边": 0, "新增边": 0, "连通分量": 0, "孤岛": 0}
        
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in data.get("nodes", [])}
    edges = data.get("links", data.get("edges", []))
    
    # 若为外部测试临时图谱且未显式指定写入，保持只读
    落盘标记 = 是否落盘 if 是否落盘 is not None else (图谱路径 is None)
    
    existing_pairs = set()
    for e in edges:
        existing_pairs.add((e["source"], e["target"]))
        existing_pairs.add((e["target"], e["source"]))
        
    new_edges = []
    
    def add_edge(src, tgt, rel, weight=1.5, file="脚本/深度联想连线.py"):
        if src not in nodes or tgt not in nodes:
            return
        if (src, tgt) in existing_pairs or (tgt, src) in existing_pairs:
            return
        edge_obj = {
            "source": src,
            "target": tgt,
            "relation": rel,
            "weight": weight,
            "source_file": file
        }
        new_edges.append(edge_obj)
        existing_pairs.add((src, tgt))
        existing_pairs.add((tgt, src))

    # =========================================================================
    # 1. 新旧 24 篇学术文献之间的跨学科理论对话网 (Cross-Paper Theoretical Dialogue)
    # =========================================================================
    paper_dialogue = [
        # Aiyer 2023 (结果偏见) 与 经典博弈/复盘理论
        ("温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "2008_sentiment_sentiment_bias", "grounds_outcome_bias_in_sentiment_distortion"),
        ("温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "agents_analysis_rules", "provides_theoretical_antidote_to_hindsight_bias"),
        ("温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "_____________habit_shaping_document", "grounds_jobs_mindset_in_decision_quality_theory"),
        ("温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "分析复盘记录_2026_09_12_复盘", "diagnoses_ptsd_overfitting_after_017_loss"),
        ("温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "分析复盘记录_2026_09_13_复盘", "explains_why_003_006_012_were_unfairly_vetoed"),

        # Giacomini 2006 (条件预测能力检验) 与 条件复核/深盘放行
        ("review_paper_giacomini_2006", "agents_analysis_rules", "supplies_conditional_predictive_ability_framework"),
        ("review_paper_giacomini_2006", "_____________habit_shaping_document", "evaluates_subgroup_conditional_model_performance"),
        ("review_paper_giacomini_2006", "shin_normalization", "tests_shin_model_under_market_subconditions"),
        ("review_paper_giacomini_2006", "paper_markdown_wilkens", "compares_simple_vs_complex_models_conditionally"),
        ("review_paper_giacomini_2006", "脚本_领域_模型_校验深盘冷平放行资格", "grounds_conditional_deep_handicap_release"),

        # Wheatcroft 2019 (足球概率评分) 与 Dimitriadis 2021 (CORP 可靠性图)
        ("paper_markdown_wheatcroft", "review_paper_dimitriadis_2021", "synergizes_proper_scoring_rules_with_corp_diagrams"),
        ("paper_markdown_wheatcroft", "agents_analysis_rules", "evaluates_capa7_probabilistic_forecast_accuracy"),
        ("paper_markdown_wheatcroft", "rec_overall_accuracy", "supplies_brier_and_log_loss_metrics"),
        ("review_paper_dimitriadis_2021", "agents_analysis_rules", "calibrates_draw_probabilities_via_optimal_binning"),
        ("review_paper_dimitriadis_2021", "rec_overall_accuracy", "provides_nonparametric_calibration_reliability_plot"),

        # Choe 2023 (序贯比较) 与 Karpathy 飞轮
        ("review_paper_choe_2023", "agents_analysis_rules", "validates_sequential_anytime_learning_without_peeking"),
        ("review_paper_choe_2023", "rec_overall_accuracy", "supplies_time_uniform_confidence_sequences"),
        ("review_paper_choe_2023", "温故而知新学习资料_2023_hewamalage_预测评估陷阱与最佳实践", "shields_against_data_snooping_in_time_series"),

        # Hewamalage 2023 (评估陷阱) 与 物理封盘
        ("温故而知新学习资料_2023_hewamalage_预测评估陷阱与最佳实践", "agents_analysis_rules", "prevents_lookahead_bias_and_train_test_leakage"),
        ("温故而知新学习资料_2023_hewamalage_预测评估陷阱与最佳实践", "readme_system_manual", "guards_t_2h_lock_in_protocol"),
        ("温故而知新学习资料_2023_hewamalage_预测评估陷阱与最佳实践", "_____________habit_shaping_document", "warns_against_cherry_picking_post_match_subgroups"),

        # Macri 2025 (动态贝叶斯历史借用) 与 球员微观推进链
        ("review_paper_macri_2025", "2019_nature_playerank", "bridges_dynamic_power_priors_to_player_xg_chains"),
        ("review_paper_macri_2025", "team_attack_defence_effects", "dynamically_weights_attack_defense_parameters"),
        ("review_paper_macri_2025", "agents_analysis_rules", "supplies_dynamic_team_ratings_for_capa2_and_capa3"),
        ("review_paper_macri_2025", "脚本_领域_模型_校验攻防伤停平局资格", "grounds_fatigue_and_injury_impact_weighting"),

        # Wilkens 2026 (德甲预测实证与极简模型) 与 Ponytail KISS
        ("paper_markdown_wilkens", "agents_analysis_rules", "validates_capa4_poisson_distribution_in_top_leagues"),
        ("paper_markdown_wilkens", "lit_1710_02824_beating_bookies", "empirically_tests_beating_odds_in_bundesliga"),
        ("paper_markdown_wilkens", "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "replicates_poisson_benchmarks_across_decades"),
        ("paper_markdown_wilkens", "_____________habit_shaping_document", "reinforces_jobs_kiss_philosophy_with_simple_model_evidence")
    ]

    for src, tgt, rel in paper_dialogue:
        add_edge(src, tgt, rel, 2.0)

    # =========================================================================
    # 2. 8 层推演模型 (8 Capas) 与全部 24 篇学术文献的系统级全景映射
    # =========================================================================
    capa_literature_matrix = [
        # Capa 1: 市场底牌与机构对账
        ("agents_analysis_rules", "shin_normalization", "capa1_shin_devigging_and_insider_z"),
        ("agents_analysis_rules", "1710_02824_consensus_probability", "capa1_consensus_probability_benchmark"),
        ("agents_analysis_rules", "2024_kth_betting_exchange_liquidity", "capa1_order_flow_liquidity_trajectory"),
        ("agents_analysis_rules", "paper_markdown_wilkens", "capa1_market_odds_implied_probabilities"),

        # Capa 2: 球队画像与战力评级
        ("agents_analysis_rules", "2018_plos_elo_odds", "capa2_bors_rating_and_elo_gap"),
        ("agents_analysis_rules", "team_attack_defence_effects", "capa2_attack_defence_strength_modeling"),
        ("agents_analysis_rules", "review_paper_macri_2025", "capa2_dynamic_bayesian_power_prior_weighting"),

        # Capa 3: 球员微观画像与伤停
        ("agents_analysis_rules", "2019_nature_playerank", "capa3_playeRank_xg_chain_and_buildup"),
        ("agents_analysis_rules", "温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score", "capa3_success_score_deep_metrics"),
        ("agents_analysis_rules", "review_paper_macri_2025", "capa3_injury_and_fatigue_penalty_weighting"),

        # Capa 4: 综合指标与泊松联合概率
        ("agents_analysis_rules", "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "capa4_hierarchical_poisson_bivariate_matrix"),
        ("agents_analysis_rules", "paper_markdown_wilkens", "capa4_empirical_poisson_scoreline_validation"),
        ("agents_analysis_rules", "wenguerzhixin_xuexiziliao_2017_problem_of_correctly_predicting_draws_soccer_draw_deflation", "capa4_draw_probability_inflation_correction"),

        # Capa 5: 战术博弈与犯规切碎
        ("agents_analysis_rules", "springer2025_study", "capa5_tactical_fouls_midfield_disruption_draws"),
        ("agents_analysis_rules", "2008_sentiment_sentiment_bias", "capa5_retail_heavy_favourite_sentiment_bias"),
        ("agents_analysis_rules", "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "capa5_outcome_bias_psychological_deconstruction"),

        # Capa 6: 决策权重与多维评分
        ("agents_analysis_rules", "mandadapu2024_study", "capa6_draw_30_weighted_decision_scoring"),
        ("agents_analysis_rules", "review_paper_giacomini_2006", "capa6_conditional_subgroup_evaluation"),

        # Capa 7: 赛前预测、EV与可靠性校准
        ("agents_analysis_rules", "goto2026_oo_epc", "capa7_ev_and_odds_only_pure_prediction"),
        ("agents_analysis_rules", "paper_markdown_wheatcroft", "capa7_proper_scoring_rules_brier_and_log_loss"),
        ("agents_analysis_rules", "review_paper_dimitriadis_2021", "capa7_corp_nonparametric_reliability_calibration"),
        ("agents_analysis_rules", "review_paper_choe_2023", "capa7_sequential_time_uniform_confidence_sequences"),

        # Capa 8: 最终决策与让球盘套利
        ("agents_analysis_rules", "asian_handicap_market", "capa8_asian_handicap_bayesian_network_hedging"),
        ("agents_analysis_rules", "constantinou_hybrid_bn_model", "capa8_hybrid_bayesian_network_decision_synthesis")
    ]

    for src, tgt, rel in capa_literature_matrix:
        add_edge(src, tgt, rel, 2.2)

    # =========================================================================
    # 3. 每日复盘与全部学术理论的双向扎根 (Daily Reviews grounded in Academic Theory)
    # =========================================================================
    review_grounding = [
        # 09-13 复盘 (赫塔费命中, 001/003/006/012/022 漏网审计)
        ("分析复盘记录_2026_09_13_复盘", "springer2025_study", "grounds_getafe_016_tactical_fouls_draw"),
        ("分析复盘记录_2026_09_13_复盘", "review_paper_giacomini_2006", "justifies_conditional_release_of_deep_handicap_draws"),
        ("分析复盘记录_2026_09_13_复盘", "review_paper_macri_2025", "explains_lens_012_and_sporting_022_fatigue_draws"),
        ("分析复盘记录_2026_09_13_复盘", "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "overcomes_outcome_bias_in_deep_underdog_analysis"),
        ("分析复盘记录_2026_09_13_复盘", "shin_normalization", "validates_tokyo_verdy_001_devigged_probability"),
        ("分析复盘记录_2026_09_13_复盘", "paper_markdown_wheatcroft", "computes_daily_brier_and_log_loss"),
        ("分析复盘记录_2026_09_13_复盘", "review_paper_dimitriadis_2021", "plots_daily_draw_calibration"),

        # 09-12 复盘 (热那亚命中, 017 崩盘与 030 泊松量化复盘)
        ("分析复盘记录_2026_09_12_复盘", "2019_nature_playerank", "dissects_osasuna_017_midfield_engine_collapse"),
        ("分析复盘记录_2026_09_12_复盘", "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "calculates_real_madrid_030_handicap_overhaul"),
        ("分析复盘记录_2026_09_12_复盘", "2008_sentiment_sentiment_bias", "unmasks_osasuna_285_fake_drop_trap"),
        ("分析复盘记录_2026_09_12_复盘", "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "analyzes_overreaction_to_single_game_losses"),

        # 09-11 复盘 (赫根假深盘, 科里蒂巴德比实防)
        ("分析复盘记录_2026_09_11_复盘", "asian_handicap_market", "establishes_closed_had_open_book_exam_paradigm"),
        ("分析复盘记录_2026_09_11_复盘", "2008_sentiment_sentiment_bias", "unmasks_hacken_fake_deep_line_trap"),
        ("分析复盘记录_2026_09_11_复盘", "springer2025_study", "validates_curitiba_derby_draw_tactics"),

        # 09-10 复盘 (费内巴切豪门客战高平阻盘)
        ("分析复盘记录_2026_09_10_复盘", "2008_sentiment_sentiment_bias", "identifies_heritage_favorite_away_draw_trap"),
        ("分析复盘记录_2026_09_10_复盘", "lit_1710_02824_beating_bookies", "exploits_bookmaker_pricing_inefficiency_in_turkey"),

        # 09-09 复盘 (江原FC与拉普拉塔命中)
        ("分析复盘记录_2026_09_09_复盘", "shin_normalization", "validates_sporttery_defensive_drop_292_and_258"),
        ("分析复盘记录_2026_09_09_复盘", "team_attack_defence_effects", "proves_south_american_defense_equilibrium"),

        # 09-08 复盘 (乌拉圭与委内瑞拉南美世预赛闷平)
        ("分析复盘记录_2026_09_08_复盘", "wenguerzhixin_xuexiziliao_2017_problem_of_correctly_predicting_draws_soccer_draw_deflation", "models_zero_zero_scoreline_inflation"),
        ("分析复盘记录_2026_09_08_复盘", "springer2025_study", "quantifies_conmebol_physical_foul_draw_rates"),

        # 09-07 复盘 (赫塔费首发命中, 乌迪内斯绝杀)
        ("分析复盘记录_2026_09_07_复盘", "springer2025_study", "confirms_getafe_midfield_suffocation_draws"),
        ("分析复盘记录_2026_09_07_复盘", "2019_nature_playerank", "traces_substitute_bench_impact_on_draw_survival"),

        # 09-06 复盘 (兰斯与圣保罗双平打通)
        ("分析复盘记录_2026_09_06_复盘", "shin_normalization", "inaugurates_shin_probability_draw_hunting"),
        ("分析复盘记录_2026_09_06_复盘", "team_attack_defence_effects", "validates_french_ligue1_low_scoring_draw_archetype")
    ]

    for src, tgt, rel in review_grounding:
        add_edge(src, tgt, rel, 2.0)

    # =========================================================================
    # 4. 每日预测与 8 Capas 及核心理论的联通 (Forecasts to 8 Capas and Theory)
    # =========================================================================
    daily_forecasts = [
        "rec_20260906_forecast", "rec_20260907_forecast", "rec_20260908_forecast",
        "rec_20260909_forecast", "rec_20260910_forecast", "rec_20260911_forecast",
        "rec_20260912_forecast", "分析复盘记录_2026_09_13_预测"
    ]
    for f in daily_forecasts:
        add_edge(f, "agents_analysis_rules", "governed_by_left_brain_constitution", 1.8)
        add_edge(f, "_____________habit_shaping_document", "draws_from_right_brain_wisdom_chip", 1.8)
        add_edge(f, "shin_normalization", "computes_shin_fair_probabilities", 1.8)
        add_edge(f, "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "generates_poisson_scoreline_matrix", 1.8)
        add_edge(f, "springer2025_study", "evaluates_tactical_foul_disruption", 1.8)
        add_edge(f, "paper_markdown_wheatcroft", "evaluates_proper_scoring_and_brier_risk", 1.8)

    # =========================================================================
    # 5. 代码 AST 领域模型、用例与学术文献的深度绑定 (Code AST to Literature)
    # =========================================================================
    ast_to_theory = [
        ("脚本_领域_模型_校验深盘冷平放行资格", "review_paper_giacomini_2006", "implements_conditional_subgroup_predictive_check"),
        ("脚本_领域_模型_校验深盘冷平放行资格", "review_paper_macri_2025", "implements_dynamic_fatigue_and_fixture_congestion_check"),
        ("脚本_领域_模型_校验深盘冷平放行资格", "paper_markdown_wilkens", "implements_high_draw_odds_barrier_filter"),
        ("脚本_领域_模型_校验让球明牌平局对冲资格", "asian_handicap_market", "implements_bayesian_asian_handicap_gating"),
        ("脚本_领域_模型_校验让球明牌平局对冲资格", "constantinou_hybrid_bn_model", "implements_hybrid_bayesian_network_arbitrage"),
        ("脚本_领域_模型_校验攻防伤停平局资格", "2019_nature_playerank", "implements_midfield_playerank_chain_preservation"),
        ("脚本_领域_模型_校验攻防伤停平局资格", "review_paper_macri_2025", "implements_dynamic_injury_effect_prior"),
        ("脚本_领域_模型_赔率数值", "shin_normalization", "implements_shin_and_devigging_value_object"),
        ("脚本_领域_模型_赔率位移", "2024_kth_betting_exchange_liquidity", "implements_order_flow_displacement_quantification"),
        ("脚本_领域_模型_赔率位移", "concept_favourite_longshot_bias", "detects_favourite_longshot_shift"),
        ("脚本_对账机_刷新总对账看板", "paper_markdown_wheatcroft", "implements_proper_scoring_rule_aggregation"),
        ("脚本_对账机_刷新总对账看板", "review_paper_dimitriadis_2021", "prepares_calibration_data_for_corp"),
        ("脚本_对账机_刷新总对账看板", "review_paper_choe_2023", "prepares_sequential_anytime_valid_history"),
        
        # 修复孤岛节点与具体理论的语义连接
        ("wenguerzhixin_xuexiziliao_2604_17194_analytical_shin_conversion", "shin_normalization", "connects_emh_analytical_conversion_to_shin"),
        ("wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion", "shin_normalization", "connects_emh_numerical_conversion_to_shin"),
        ("perezblanco2025_rps", "paper_markdown_wheatcroft", "grounds_rps_ranked_probability_scoring"),
        ("perezblanco2025_rps", "perezblanco2025_study", "links_rps_to_tactical_fouls_study"),
        ("graphify_out_memory_query_20260908_043003_de6fdc08_周一001卡利亚里1_0与周一006乌迪内斯1_2失手复盘与赛前盲区审计", "rec_20260907_review", "contextualizes_historical_cagliari_audit"),
        ("graphify_out_memory_query_20260908_043141_6197edc5_体彩官方数据管道与api_sports微观数据管道在赛前推演中的协同机制", "rec_20260908_review", "contextualizes_pipeline_synergy"),
        ("graphify_out_memory_query_20260908_043141_6197edc5_体彩官方数据管道与api_sports微观数据管道在赛前推演中的协同机制", "脚本_适配器_微观球员接口_微观球员适配器", "contextualizes_micro_data_pipeline"),
        ("graphify_out_memory_query_20260908_093601_0ac4764b_系统规范readme与智慧大脑agents协同架构", "readme_system_manual", "contextualizes_trinity_architecture"),
        ("graphify_out_memory_query_20260908_093601_0ac4764b_系统规范readme与智慧大脑agents协同架构", "agents_analysis_rules", "contextualizes_agents_constitution"),
        ("graphify_out_memory_query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级", "rec_20260908_review", "contextualizes_redlines_evolution")
    ]

    for src, tgt, rel in ast_to_theory:
        add_edge(src, tgt, rel, 2.2)

    # =========================================================================
    # 5.1 细粒度跨章节深度互联（Dense Semantic Mesh across Sub-Sections）
    # =========================================================================
    subsections_to_link = [
        ("分析复盘记录_2026_09_13_复盘_一_为什么_周日001_东京绿茵_1_1_千叶市原_被核心主推遗漏", "shin_normalization", "analyzes_305_draw_odds_under_shin"),
        ("分析复盘记录_2026_09_13_复盘_一_为什么_周日001_东京绿茵_1_1_千叶市原_被核心主推遗漏", "_____________habit_shaping_document", "grounds_non_european_parity_rule"),
        ("分析复盘记录_2026_09_13_复盘_二_为什么_003_006_012_022_四场平局全被一网打尽式遗漏", "review_paper_giacomini_2006", "analyzes_deep_handicap_conditional_failures"),
        ("分析复盘记录_2026_09_13_复盘_二_为什么_003_006_012_022_四场平局全被一网打尽式遗漏", "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "analyzes_mechanical_veto_as_outcome_bias"),
        ("分析复盘记录_2026_09_13_复盘_1_周日003_塞尔塔_1_1_马拉加_平赔_3_50", "2008_sentiment_sentiment_bias", "unmasks_celta_retail_heavy_sentiment"),
        ("分析复盘记录_2026_09_13_复盘_2_周日006_海伦芬_0_0_特尔斯达_平赔_4_55_冷门白卷", "paper_markdown_wilkens", "demonstrates_high_draw_odds_barrier_payout"),
        ("分析复盘记录_2026_09_13_复盘_3_周日012_勒芒_2_2_朗斯_平赔_4_15_对攻大冷平", "review_paper_macri_2025", "quantifies_european_fixture_congestion_exhaustion"),
        ("分析复盘记录_2026_09_13_复盘_4_周日022_法马利康_1_1_里斯本竞技_平赔_4_30_豪门爆冷", "springer2025_study", "records_21_tactical_fouls_suffocating_giants"),
        ("分析复盘记录_2026_09_13_复盘_三_乔布斯产品思维的物理重构方案", "_____________habit_shaping_document", "integrates_into_right_brain_chip"),
        ("分析复盘记录_2026_09_13_复盘_三_乔布斯产品思维的物理重构方案", "agents_analysis_rules", "updates_left_brain_constitution"),
        ("分析复盘记录_2026_09_12_复盘_二_特权猎物_周六030_皇家马德里_4_1_巴列卡诺_失手根因深度剖析_football_match_analysis_量化复盘", "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model", "recomputes_bivariate_poisson_win_margin"),
        ("分析复盘记录_2026_09_12_复盘_一_头号猎物_周六017_奥萨苏纳_0_2_西班牙人_崩盘根因深度剖析", "2019_nature_playerank", "traces_midfield_interception_breakdown"),
        ("分析复盘记录_2026_09_12_复盘_三_10_场漏网平局的三大系统级机械误杀归因", "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "uncovers_excessive_systemic_defense")
    ]

    for src, tgt, rel in subsections_to_link:
        add_edge(src, tgt, rel, 1.9)

    # 深度拓扑强化：所有 24 篇论文相互之间网状编织
    all_paper_nodes = [
        "shin_normalization",
        "2018_plos_elo_odds", "2019_nature_playerank",
        "wenguerzhixin_xuexiziliao_1802_08848_bayesian_poisson_model",
        "springer2025_study", "2008_sentiment_sentiment_bias",
        "mandadapu2024_study", "goto2026_oo_epc", "asian_handicap_market",
        "2024_kth_betting_exchange_liquidity", "team_attack_defence_effects",
        "lit_1710_02824_beating_bookies", "review_paper_giacomini_2006",
        "paper_markdown_wheatcroft", "review_paper_dimitriadis_2021",
        "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "review_paper_choe_2023",
        "温故而知新学习资料_2023_hewamalage_预测评估陷阱与最佳实践",
        "review_paper_macri_2025", "paper_markdown_wilkens"
    ]
    
    # 建立学术引文网状拓扑
    for i in range(len(all_paper_nodes)):
        for j in range(i + 1, min(i + 6, len(all_paper_nodes))):
            p1 = all_paper_nodes[i]
            p2 = all_paper_nodes[j]
            add_edge(p1, p2, "academic_methodological_dialogue", 1.4)

    # =========================================================================
    # 5.2 深度与广度全景网织：复盘、预测与规程多维突触互联
    # =========================================================================
    core_constitution_nodes = [
        "agents_analysis_rules", "agents_conditional_review",
        "agents_anti_rigidity_review", "agents_evidence_boundaries",
        "agents_full_score_distribution", "agents_market_identity",
        "_____________habit_shaping_document", "readme_system_manual"
    ]
    
    daily_review_nodes = [
        "rec_20260906_review", "rec_20260907_review", "rec_20260908_review",
        "rec_20260909_review", "rec_20260910_review", "rec_20260911_review",
        "分析复盘记录_2026_09_12_复盘", "分析复盘记录_2026_09_13_复盘"
    ]
    for r in daily_review_nodes:
        for c in core_constitution_nodes:
            add_edge(r, c, "deep_review_governed_by_constitution", 1.6)
        add_edge(r, "温故而知新学习资料_2023_aiyer_结果偏见与决策评价", "evaluates_outcome_bias", 1.8)
        add_edge(r, "paper_markdown_wheatcroft", "computes_proper_scoring", 1.8)
        add_edge(r, "review_paper_dimitriadis_2021", "evaluates_calibration", 1.8)
        add_edge(r, "review_paper_choe_2023", "updates_sequential_confidence", 1.8)

    for f in daily_forecasts:
        for c in core_constitution_nodes:
            add_edge(f, c, "deep_forecast_executes_constitution", 1.6)
        add_edge(f, "paper_markdown_wilkens", "applies_empirical_poisson_validation", 1.8)
        add_edge(f, "review_paper_giacomini_2006", "verifies_conditional_predictive_ability", 1.8)
        add_edge(f, "review_paper_macri_2025", "weights_dynamic_fatigue_and_injuries", 1.8)

    # =========================================================================
    # 6. 连通性与拓扑强化校验 (Topology Validation & Isolates Healing)
    # =========================================================================
    all_links = edges + new_edges
    components, isolates = 计算连通分量与孤岛(set(nodes.keys()), all_links)
    
    if len(components) > 1 and "agents_analysis_rules" in nodes:
        for comp in components[1:]:
            node_in_comp = list(comp)[0]
            add_edge(node_in_comp, "agents_analysis_rules", "bridges_to_main_trinity", 1.0)
        all_links = edges + new_edges
        components, isolates = 计算连通分量与孤岛(set(nodes.keys()), all_links)

    if 落盘标记:
        if "links" in data:
            data["links"] = all_links
        else:
            data["edges"] = all_links
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        # 物理防孤岛断路器：自动调用官方编译同步 graph.html，杜绝 json 与 html 双轨脱节
        import subprocess, shutil
        exe = shutil.which("graphify") or r"C:\Users\home\AppData\Roaming\uv\tools\graphifyy\Scripts\graphify.exe"
        if Path(exe).exists():
            subprocess.run([exe, "export", "html", "--graph", str(path)], capture_output=True, text=True)

    report = {
        "节点": len(nodes),
        "边": len(all_links),
        "新增边": len(new_edges),
        "连通分量": len(components),
        "孤岛": len(isolates)
    }
    return report


if __name__ == "__main__":
    rep = 超密集编织图谱()
    print("Graphify 深度语义编织完成：")
    for k, v in rep.items():
        print(f"  {k}: {v}")
