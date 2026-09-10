# Graph Report - 足球预测  (2026-09-09)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 175 nodes · 292 edges · 22 communities (14 shown, 8 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0a7ee79b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 心电图录像机.py
- 赔率快照
- Football Quant Agent Brain
- Favourite-Longshot-Bias-Adjusted GLM (FL-GLM)
- 体彩官方适配器
- KTH 2024 Betting Exchange Liquidity Study
- Egidi Hierarchical Bayesian Poisson Model
- ELO-Odds Rating System
- Success Score Metric
- Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study
- Clustered Probit Model
- Wyscout Spatio-Temporal Match Events Dataset
- Constantinou Hybrid Bayesian Network Model
- Betting Exchange Liquidity Dynamics
- Ranked Probability Score (RPS)
- 2026-09-06 Pre-Match Forecast
- 2026-09-06 Post-Match Review
- 2026-09-07 Pre-Match Forecast
- 2026-09-08 Pre-Match Forecast
- Overall Accuracy & Real-time Scoreboard
- Analytical Variant of Shin Conversion

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
- `Football Quant Agent Brain` --cites--> `Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017)`  [EXTRACTED]
  AGENTS.md → 温故而知新学习资料/1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md
- `Analysis Review Records Manual` --references--> `Football Quant Agent Brain`  [EXTRACTED]
  分析复盘记录/README.md → AGENTS.md
- `本地账本仓储` --uses--> `赔率快照`  [INFERRED]
  脚本/适配器/本地账本.py → 脚本/领域/模型.py
- `探测并记录心电图用例` --uses--> `赔率位移`  [INFERRED]
  脚本/应用/用例.py → 脚本/领域/模型.py
- `记录结果` --uses--> `赔率位移`  [INFERRED]
  脚本/应用/用例.py → 脚本/领域/模型.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Daily Actuarial Deduction and Audit Cycle** — agents_eight_capas_model, agents_five_hard_red_lines_v31, rec_20260908_forecast, rec_20260908_review, rec_20260909_forecast [EXTRACTED 0.95]
- **Closed-Loop Flywheel System Architecture** — agents_karpathy_flywheel, rec_readme_guidelines, 脚本_对账机, rec_overall_accuracy, rec_overall_summary [EXTRACTED 0.95]
- **Soccer ELO Rating System Hierarchy** — 2018_plos_elo_odds, 2018_plos_elo_goals, 2018_plos_elo_result [EXTRACTED 0.95]
- **Reverse Odds to Probability Conversion Methods** — goto2026_oo_epc, wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_analytical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_power_conversion, wenguerzhixin_xuexiziliao_shin_1993_and_strumbelj_2014_shin_model [EXTRACTED 0.95]
- **Football Match Outcome Modelling Paradigms** — 温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_draw_prediction_evaluation, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_dnn_model, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bookmaker_odds_model [INFERRED 0.85]
- **Betting Market Aggregate Information Framework** — 1710_02824_consensus_probability, 2018_plos_elo_odds, 2008_sentiment_sentiment_bias [INFERRED 0.85]
- **Soccer Match Outcome Forecasting Frameworks** — egidi_hierarchical_poisson_model, constantinou_hybrid_bn_model, ordered_logit_regression, multinomial_logit_regression [INFERRED 0.85]

## Communities (22 total, 8 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.12
Nodes (16): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入(), test_赔率数值验证与去水计算(), 赔率快照 (+8 more)

### Community 1 - "心电图录像机.py"
Cohesion: 0.14
Nodes (18): ABC, 回溯连续轨迹用例, 探测并记录心电图用例, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例 (+10 more)

### Community 2 - "赔率快照"
Cohesion: 0.19
Nodes (10): 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, 输出端口：心电图轨迹的数据持久化与历史回溯, 赔率账本契约, 聚合根实体：带时间戳与赛事身份的心电图观测点 (+2 more)

### Community 3 - "Football Quant Agent Brain"
Cohesion: 0.14
Nodes (14): Football Quant Agent Brain, 8-Capas Betting Deduction Model, Five Hard Red Lines (V3.1 Physical Circuit Breakers), Karpathy Skill Self-Evolution Flywheel, Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017), DDD Onion Architecture & System Specs, 2026-09-07 Post-Match Review, 2026-09-08 Post-Match Review (+6 more)

### Community 4 - "Favourite-Longshot-Bias-Adjusted GLM (FL-GLM)"
Cohesion: 0.16
Nodes (14): Favourite-Longshot Bias (FLB), Favourite-Longshot-Bias-Adjusted GLM (FL-GLM), Odds-Only Equal Profitability Confidence (OO-EPC), Goto et al. (2026) Odds-Only and FL-GLM Conversion Study, Hierarchical Bayesian Poisson Football Score Model, Draw Bias in Odds Conversion Models, Multiplicative Odds Conversion, Numerical Variant of Shin Conversion (+6 more)

### Community 5 - "体彩官方适配器"
Cohesion: 0.24
Nodes (6): test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照, DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体, 实现赔率提供者契约，直连国家体彩中心官方网关, 体彩官方适配器

### Community 6 - "KTH 2024 Betting Exchange Liquidity Study"
Cohesion: 0.18
Nodes (11): Chi-squared Test Feature Selection, Multilayer Perceptron (Betting Exchange), Random Forest Classifier (Betting Exchange), Recursive Feature Elimination (RFE), Relative Strength Index (RSI Classifier), Simple Moving Average (SMA Classifier), KTH 2024 Betting Exchange Liquidity Study, Support Vector Machine (Betting Exchange) (+3 more)

### Community 7 - "Egidi Hierarchical Bayesian Poisson Model"
Cohesion: 0.25
Nodes (9): Egidi Hierarchical Bayesian Poisson Model, Elo Rating Difference, Multinomial Logit Regression (MLR) for Soccer, Ordered Logit Regression (OLR) for Soccer, Shin Odds Normalization Procedure, Skellam Distribution (Poisson-Difference), Dynamic Seasonal Team Attack and Defence Effects, Draw Prediction Evaluation Framework (+1 more)

### Community 8 - "ELO-Odds Rating System"
Cohesion: 0.25
Nodes (8): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, ELO-Goals Rating System, ELO-Odds Rating System, ELO-Result Rating System, Informational Loss Metric

### Community 9 - "Success Score Metric"
Cohesion: 0.33
Nodes (6): Deep Neural Network (DNN) Architecture, Match Outcome Classification via Thresholds, Success Score Metric, Tactical Play Styles Framework, Bettor State-Space Model (SSM), Bookmaker Implied Probability Regression Models

### Community 10 - "Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study"
Cohesion: 0.50
Nodes (4): Relative-Distance Centroid Discretization, Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study, Two-Tier Naive Bayes Cluster Optimization, Weighted Accuracy & Recall (WAP & WAR)

### Community 11 - "Clustered Probit Model"
Cohesion: 0.67
Nodes (3): Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds

### Community 12 - "Wyscout Spatio-Temporal Match Events Dataset"
Cohesion: 0.67
Nodes (3): Passing Network Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events Dataset

### Community 13 - "Constantinou Hybrid Bayesian Network Model"
Cohesion: 0.67
Nodes (3): Asian Handicap (AH) Betting Market, Constantinou Hybrid Bayesian Network Model, Modified Pi-Rating System

## Knowledge Gaps
- **48 isolated node(s):** `Modified Pi-Rating System`, `Bettor State-Space Model (SSM)`, `Match Outcome Classification via Thresholds`, `Tactical Play Styles Framework`, `Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017)` (+43 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 72 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `心电图录像机.py`, `体彩官方适配器`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `DDD Onion Architecture & System Specs` connect `Football Quant Agent Brain` to `心电图录像机.py`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `赔率数值` (e.g. with `体彩官方适配器` and `本地账本仓储`) actually correct?**
  _`赔率数值` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `赔率账本契约` (e.g. with `回溯连续轨迹用例` and `探测并记录心电图用例`) actually correct?**
  _`赔率账本契约` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `本地账本仓储` (e.g. with `赔率快照` and `赔率数值`) actually correct?**
  _`本地账本仓储` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `赔率提供者契约` (e.g. with `探测并记录心电图用例` and `组装架构()`) actually correct?**
  _`赔率提供者契约` has 3 INFERRED edges - model-reasoned connections that need verification._