# Graph Report - 足球预测  (2026-09-08)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 195 nodes · 313 edges · 23 communities (16 shown, 7 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 25 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `19857dad`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 赔率快照
- 心电图录像机.py
- Sports Betting Actuarial Literature Corpus Index
- 体彩官方适配器
- Skellam Convex Combination Model
- 赛前 3 道金刚硬红线
- Karpathy 技能自进化飞轮
- 足球倍率精算与赛事量化预测系统 (Football Quant & Odds Actuarial System)
- Success Score Metric
- ELO-Odds Rating System
- Naive Bayes Foul Prediction Model
- Predicting Odds Movement and Betting Exchange Liquidity (KTH 2024)
- Bettor State-Space Model with Inflated Beta Distribution
- 对账机.py
- Wyscout Spatio-Temporal Match Events (Soccer-logs)
- Betfair Exchange Match Odds Dataset
- Power Odds Conversion
- 分析复盘三位一体自驱动规程
- 查询记忆: 体彩与API-Sports管道协同机制
- 1710.02824 庄家共识赔率破译策略
- 2008 散户情绪与庄家定价偏见
- Power Conversion Method

## God Nodes (most connected - your core abstractions)
1. `赔率快照` - 37 edges
2. `赔率数值` - 20 edges
3. `赔率账本契约` - 18 edges
4. `本地账本仓储` - 16 edges
5. `赔率提供者契约` - 14 edges
6. `体彩官方适配器` - 14 edges
7. `探测并记录心电图用例` - 13 edges
8. `回溯连续轨迹用例` - 11 edges
9. `组装架构()` - 10 edges
10. `赔率位移` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Sports Betting Actuarial Literature Corpus Index` --references--> `2026-09-07 赛后全量复盘报告 (3.0模型确立)`  [EXTRACTED]
  温故而知新学习资料/README_学习资料索引与经典论文导读.md → 分析复盘记录/2026-09-07_复盘.md
- `查询记忆: 001与006失手盲区审计` --references--> `赛前 3 道金刚硬红线`  [EXTRACTED]
  graphify-out/memory/query_20260908_043003_de6fdc08_周一001卡利亚里1_0与周一006乌迪内斯1_2失手复盘与赛前盲区审计.md → 分析复盘记录/总复盘总结.md
- `四大安全断路器` --semantically_similar_to--> `赛前 3 道金刚硬红线`  [INFERRED] [semantically similar]
  分析复盘记录/README.md → 分析复盘记录/总复盘总结.md
- `本地账本仓储` --uses--> `赔率快照`  [INFERRED]
  脚本/适配器/本地账本.py → 脚本/领域/模型.py
- `探测并记录心电图用例` --uses--> `赔率位移`  [INFERRED]
  脚本/应用/用例.py → 脚本/领域/模型.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Betting Market Exploitation and Decision Thresholds** — wenguerzhixinxuexiziliao_1802_08848_combining_historical_data_and_bookmakers_odds_betting_strategies, wenguerzhixinxuexiziliao_2003_09384_asian_handicap_market_efficiency_bayesian_networks_roi_vs_profit_optimization, wenguerzhixinxuexiziliao_2003_09384_asian_handicap_market_efficiency_bayesian_networks_asian_handicap_rules [EXTRACTED 0.90]
- **Statistical and Probabilistic Football Match Forecasting Models** — wenguerzhixinxuexiziliao_1802_08848_combining_historical_data_and_bookmakers_odds_skellam_convex_model, wenguerzhixinxuexiziliao_2003_09384_asian_handicap_market_efficiency_bayesian_networks_hybrid_bayesian_network, wenguerzhixinxuexiziliao_2017_problem_of_correctly_predicting_draws_soccer_ordered_logit_regression, wenguerzhixinxuexiziliao_2017_problem_of_correctly_predicting_draws_soccer_multinomial_logit_regression [EXTRACTED 0.90]
- **赛前精算推演与赛后盲区复盘进化飞轮** — fenxifupan_readme_workflow, fenxifupan_summary_three_red_lines [EXTRACTED 0.95]
- **Football Team Strength and Dynamic Rating Systems** — wenguerzhixinxuexiziliao_2003_09384_asian_handicap_market_efficiency_bayesian_networks_modified_pi_rating, wenguerzhixinxuexiziliao_2017_problem_of_correctly_predicting_draws_soccer_soccer_elo_system, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score_metric [EXTRACTED 0.95]
- **推演预测与对账闭环演进** — agents_karpathy_flywheel, analysis_20260908_prediction, analysis_total_accuracy [EXTRACTED 0.95]
- **In-Match Betting Market Anticipation Analysis Framework** — 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_in_match_betting_data, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bookmaker_regression_models, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bettor_ssm, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_anticipation_analysis_goal [EXTRACTED 0.95]
- **Spatio-Temporal Performance Indicators from Event Streams** — 温故而知新学习资料_2019_nature_playerank_data_driven_framework_soccer_logs, 温故而知新学习资料_2019_nature_playerank_data_driven_framework_playerank, 温故而知新学习资料_2019_nature_playerank_data_driven_framework_passing_network, 温故而知新学习资料_2019_nature_playerank_data_driven_framework_invasion_acceleration [EXTRACTED 0.95]
- **Success Score Modeling and Outcome Classification Pipeline** — 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_feature_vector_68d, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_dnn_model, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_threshold_classification, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_success_score_metric [EXTRACTED 0.95]
- **Market Efficiency and Odds-Based Ratings in Soccer** — 温故而知新学习资料_2008_sentiment_and_bookmaker_pricing_bias_sentiment_bias, 温故而知新学习资料_2008_sentiment_and_bookmaker_pricing_bias_clustered_probit, 温故而知新学习资料_2018_plos_betting_odds_rating_system_bors_elo_odds, 温故而知新学习资料_2024_kth_predicting_odds_movement_betting_exchange_liquidity_odds_movement_classifier [INFERRED 0.80]
- **平局决策模型进化与断路器防线血统** — fenxifupan_20260906_six_dimension_model, fenxifupan_summary_three_red_lines, fenxifupan_readme_four_circuit_breakers [INFERRED 0.85]
- **8层推演模型与数据管道集成** — agents_eight_capas_model, readme_pipeline_sporttery, readme_pipeline_apisports [INFERRED 0.85]
- **Odds to True Probability Inversion Methodologies** — shin_1993_and_strumbelj_2014_z_parameter, 2604_17194_shin_conversion, 2604_17194_oo_epc_method, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_fl_glm, 温故而知新学习资料_1802_08848_combining_historical_data_and_bookmakers_odds_implicit_scoring_rates [INFERRED 0.85]

## Communities (23 total, 7 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.11
Nodes (17): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入(), test_赔率数值验证与去水计算(), 赔率快照 (+9 more)

### Community 1 - "赔率快照"
Cohesion: 0.16
Nodes (13): ABC, 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, DDD 领域端口契约 - 抽象基类定义输入与输出边界, 输入/输出端口：从外部获取最新的实时赔率快照 (+5 more)

### Community 2 - "心电图录像机.py"
Cohesion: 0.18
Nodes (14): 回溯连续轨迹用例, 探测并记录心电图用例, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例, 记录结果 (+6 more)

### Community 3 - "Sports Betting Actuarial Literature Corpus Index"
Cohesion: 0.11
Nodes (19): 1x2 Bookmaker Odds Formulation, Premier League Match Outcome ML Pipeline, Multiplicative Odds Conversion, Odds-Only-Equal-Profitability-Confidence (OO-EPC), Shin Odds Conversion, Sports Betting Actuarial Literature Corpus Index, solve_shin_probabilities, Shin Insider Trading Rate (z) (+11 more)

### Community 4 - "体彩官方适配器"
Cohesion: 0.24
Nodes (6): test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照, DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体, 实现赔率提供者契约，直连国家体彩中心官方网关, 体彩官方适配器

### Community 5 - "Skellam Convex Combination Model"
Cohesion: 0.20
Nodes (11): Profitability Betting Strategies A and B, Shin's Odds Normalization Method, Skellam Convex Combination Model, Asian Handicap Market Mechanisms, Beta-Binomial Hybrid Bayesian Network, Modified Pi-Rating System, Threshold Optimization Discrepancy (ROI vs Profit), Multinomial Logit Regression (MLR) in Soccer (+3 more)

### Community 6 - "赛前 3 道金刚硬红线"
Cohesion: 0.20
Nodes (10): 2026-09-06 赛前精算预测, 2026-09-06 赛后全景复盘报告, 平局精算推演六维加权决策模型 (100分制), 2026-09-07 赛前精算预测, 2026-09-07 赛后全量复盘报告 (3.0模型确立), 四大安全断路器, 周一001 卡利亚里盲区审计 (倾斜盘误判), 周一006 乌迪内斯盲区审计 (伪降水诱平) (+2 more)

### Community 7 - "Karpathy 技能自进化飞轮"
Cohesion: 0.28
Nodes (9): 庄家必赚与通杀收割公理, 8层博彩推演模型 (8 Capas), Karpathy 技能自进化飞轮, 赛前三道金刚一票否决红线, 2026-09-08 赛前精算推演报告, 中国体彩足球平局全量推演看板, 全球微观数据管道 (API-Sports), 体彩官方赔率直连管道 (+1 more)

### Community 8 - "足球倍率精算与赛事量化预测系统 (Football Quant & Odds Actuarial System)"
Cohesion: 0.25
Nodes (7): 1.1 系统架构设计, 1.2 数据管道规范, 1. 核心架构与系统规范, 2. 目录资产规范, 3. 硬性运行规则与操作契约, 4. 常用 CLI 操作指南, 足球倍率精算与赛事量化预测系统 (Football Quant & Odds Actuarial System)

### Community 9 - "Success Score Metric"
Cohesion: 0.25
Nodes (8): Success Score DNN Architecture, Ten Tactical Play Styles Framework, Deep Neural Network Model, 68-Dimensional Input Vector, Home Ground Advantage Statistical Analysis, Rolling Averages Feature Engineering, Success Score Metric, Match Outcome Classification Thresholds

### Community 10 - "ELO-Odds Rating System"
Cohesion: 0.25
Nodes (8): BOOKPROB Implied Probability, Clustered Probit Model (Forrest & Simmons), DIFFATTEND Metric, Sentiment Bias in Sports Betting, ELO-Goals Model, ELO-Odds Rating System, ELO-Result Baseline Model, Informational Loss (Li)

### Community 11 - "Naive Bayes Foul Prediction Model"
Cohesion: 0.33
Nodes (6): Relative-Distance Cluster Discretization, Naive Bayes Draw Prediction Model, Naive Bayes Foul Prediction Model, Rank Probability Score (RPS), Weighted Accuracy & Recall (WAP / WAR), Predicting Draws and Number of Fouls in Football Matches using Bayesian Network Classifiers

### Community 12 - "Predicting Odds Movement and Betting Exchange Liquidity (KTH 2024)"
Cohesion: 0.40
Nodes (5): Betting Exchange Liquidity Filtering, MLP Odds Prediction Model, Random Forest Odds Prediction Model, SVM Odds Prediction Model, Predicting Odds Movement and Betting Exchange Liquidity (KTH 2024)

### Community 13 - "Bettor State-Space Model with Inflated Beta Distribution"
Cohesion: 0.60
Nodes (5): Goal Anticipation Empirical Test, Bettor State-Space Model with Inflated Beta Distribution, Bookmaker Implied Probability Regression Models, High-Resolution In-Match Betting Data, In-Match Expected Goals Difference (xgdiff/t)

### Community 14 - "对账机.py"
Cohesion: 0.60
Nodes (3): 中国体彩足球平局自动化对账机 (对账机.py) 用于扫描 分析复盘记录/*_复盘.md，自动聚合计算总胜率与复盘手法，并实时无缝物理刷新： 1.…, 刷新总对账看板(), test_对账看板能正常聚合数据并更新总准确率文件()

### Community 15 - "Wyscout Spatio-Temporal Match Events (Soccer-logs)"
Cohesion: 0.50
Nodes (4): Invasion Index & Acceleration Index, Passing Network & Flow Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events (Soccer-logs)

## Knowledge Gaps
- **50 isolated node(s):** `1.1 系统架构设计`, `1.2 数据管道规范`, `2. 目录资产规范`, `3. 硬性运行规则与操作契约`, `4. 常用 CLI 操作指南` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 75 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `心电图录像机.py`, `体彩官方适配器`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `赔率数值` connect `赔率数值` to `赔率快照`, `体彩官方适配器`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `本地账本仓储` connect `赔率数值` to `赔率快照`, `心电图录像机.py`, `体彩官方适配器`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `赔率数值` (e.g. with `体彩官方适配器` and `本地账本仓储`) actually correct?**
  _`赔率数值` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `赔率账本契约` (e.g. with `回溯连续轨迹用例` and `探测并记录心电图用例`) actually correct?**
  _`赔率账本契约` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `本地账本仓储` (e.g. with `赔率快照` and `赔率数值`) actually correct?**
  _`本地账本仓储` has 2 INFERRED edges - model-reasoned connections that need verification._