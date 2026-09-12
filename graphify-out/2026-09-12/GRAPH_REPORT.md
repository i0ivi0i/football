# Graph Report - 足球预测  (2026-09-12)

## Corpus Check
- 47 files · ~155,430 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 232 nodes · 391 edges · 18 communities
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 35 edges (avg confidence: 0.96)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f5bf50e9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 心电图录像机.py
- 赔率快照
- 对账机.py
- Favourite-Longshot-Bias-Adjusted GLM (FL-GLM)
- 2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告
- KTH 2024 Betting Exchange Liquidity Study
- Egidi Hierarchical Bayesian Poisson Model
- ELO-Odds Rating System
- 8-Capas Betting Deduction Model
- 2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告
- 体彩官方适配器
- Success Score Metric
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制
- Q: 系统规范README与智慧大脑AGENTS协同架构
- 2026-09-09（周三）中国体彩平局全要素深度复盘报告
- 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）

## God Nodes (most connected - your core abstractions)
1. `赔率快照` - 37 edges
2. `赔率数值` - 20 edges
3. `赔率账本契约` - 18 edges
4. `本地账本仓储` - 16 edges
5. `体彩官方适配器` - 14 edges
6. `赔率提供者契约` - 14 edges
7. `8-Capas Betting Deduction Model` - 14 edges
8. `探测并记录心电图用例` - 13 edges
9. `General Post-Mortem Manual & Blind-Spot Audit` - 13 edges
10. `回溯连续轨迹用例` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Bettor State-Space Model (SSM)` --supports_capa_7--> `8-Capas Betting Deduction Model`  [EXTRACTED]
  温故而知新学习资料/2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md → AGENTS.md
- `2026-09-11 Post-Match Review` ----> `Sentiment Bias in Betting Odds`  [INFERRED]
  分析复盘记录/2026-09-11_复盘.md → 温故而知新学习资料/2008_Sentiment_and_Bookmaker_Pricing_Bias.md
- `Shin Odds Normalization Procedure` --supports_capa_1--> `8-Capas Betting Deduction Model`  [EXTRACTED]
  温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md → AGENTS.md
- `2026-09-11 Post-Match Review` ----> `Shin Insider Trading Odds Inversion Model`  [INFERRED]
  分析复盘记录/2026-09-11_复盘.md → 温故而知新学习资料/Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md
- `KTH 2024 Betting Exchange Liquidity Study` --supports_capa_6--> `8-Capas Betting Deduction Model`  [EXTRACTED]
  温故而知新学习资料/2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md → AGENTS.md

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

## Communities (18 total, 0 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.11
Nodes (16): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入(), test_赔率数值验证与去水计算(), 赔率快照 (+8 more)

### Community 1 - "心电图录像机.py"
Cohesion: 0.18
Nodes (14): 回溯连续轨迹用例, 探测并记录心电图用例, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例, 记录结果 (+6 more)

### Community 2 - "赔率快照"
Cohesion: 0.15
Nodes (14): ABC, 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, DDD 输出适配器 - SQLite 赔率心电图连续账本 负责在结构化本地数据目录中存储和检索时序快照, DDD 领域端口契约 - 抽象基类定义输入与输出边界 (+6 more)

### Community 3 - "对账机.py"
Cohesion: 0.47
Nodes (4): DDD Onion Architecture & System Specs, 中国体彩足球平局自动化对账机 (对账机.py) 用于扫描 分析复盘记录/*_复盘.md，自动聚合计算总胜率与复盘手法，并实时无缝物理刷新： 1.…, 刷新总对账看板(), test_对账看板能正常聚合数据并更新总准确率文件()

### Community 4 - "Favourite-Longshot-Bias-Adjusted GLM (FL-GLM)"
Cohesion: 0.12
Nodes (15): Favourite-Longshot Bias (FLB), Favourite-Longshot-Bias-Adjusted GLM (FL-GLM), Odds-Only Equal Profitability Confidence (OO-EPC), Goto et al. (2026) Odds-Only and FL-GLM Conversion Study, Analytical Variant of Shin Conversion, Draw Bias in Odds Conversion Models, Multiplicative Odds Conversion, Numerical Variant of Shin Conversion (+7 more)

### Community 5 - "2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.20
Nodes (10): 1. 赛前（T-2h）已知客观数据流水, 1. 赛前已知数据与操盘陷阱, 2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告, 2. 为什么会被模型错误一票否决？（三大认知根因剖析）, 一、 唯一平局漏网盲区深度审计：【周四001 费内巴切 1:1 罗马】, 三、 经验物理固化与飞轮升级成果, 二、 周四007【德尔瓦耶 0:2 弗拉门戈】单挑失手深度复盘, 根因一：机械教条主义滥用【红线 4】（前置条件校验严重缺失） (+2 more)

### Community 6 - "KTH 2024 Betting Exchange Liquidity Study"
Cohesion: 0.15
Nodes (13): Betting Exchange Liquidity Dynamics, Technical Indicators (SMA & RSI), Chi-squared Test Feature Selection, Multilayer Perceptron (Betting Exchange), Random Forest Classifier (Betting Exchange), Recursive Feature Elimination (RFE), Relative Strength Index (RSI Classifier), Simple Moving Average (SMA Classifier) (+5 more)

### Community 7 - "Egidi Hierarchical Bayesian Poisson Model"
Cohesion: 0.25
Nodes (9): Egidi Hierarchical Bayesian Poisson Model, Elo Rating Difference, Multinomial Logit Regression (MLR) for Soccer, Ordered Logit Regression (OLR) for Soccer, Shin Odds Normalization Procedure, Skellam Distribution (Poisson-Difference), Dynamic Seasonal Team Attack and Defence Effects, Draw Prediction Evaluation Framework (+1 more)

### Community 8 - "ELO-Odds Rating System"
Cohesion: 0.25
Nodes (8): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, ELO-Goals Rating System, ELO-Odds Rating System, ELO-Result Rating System, Informational Loss Metric

### Community 9 - "8-Capas Betting Deduction Model"
Cohesion: 0.07
Nodes (38): Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Passing Network Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events Dataset, Football Quant Agent Brain, 8-Capas Betting Deduction Model (+30 more)

### Community 10 - "2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.25
Nodes (8): 1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误, 1. 赛前（T-2h）已知客观数据流水, 2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告, 2. 为什么会被模型一票否决漏网？（认知根因）, 2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡, 一、 主推失手深度剖析：为什么周五012与011会全军覆没？, 三、 闭环演化：两道物理级断路器系统升级（写入代码与大脑）, 二、 漏网盲区深度审计：【周五004 赫根 1:1 米亚尔比】

### Community 11 - "体彩官方适配器"
Cohesion: 0.24
Nodes (6): test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照, DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体, 实现赔率提供者契约，直连国家体彩中心官方网关, 体彩官方适配器

### Community 12 - "Success Score Metric"
Cohesion: 0.33
Nodes (6): Deep Neural Network (DNN) Architecture, Match Outcome Classification via Thresholds, Success Score Metric, Tactical Play Styles Framework, Bettor State-Space Model (SSM), Bookmaker Implied Probability Regression Models

### Community 13 - "Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes

### Community 14 - "Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes

### Community 15 - "Q: 系统规范README与智慧大脑AGENTS协同架构"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 系统规范README与智慧大脑AGENTS协同架构, Source Nodes

### Community 16 - "2026-09-09（周三）中国体彩平局全要素深度复盘报告"
Cohesion: 0.40
Nodes (5): 1. 🎯 【周三001 江原FC 1:1 全北现代】（赛果：平局 1:1 · 体彩平赔 2.92）, 2026-09-09（周三）中国体彩平局全要素深度复盘报告, 2. 🎯 【周三014 拉普拉塔大学 1:1 科林蒂安】（赛果：平局 1:1 · 体彩平赔 2.58）, 一、 两场命中平局全景精算复盘, 二、 五道硬红线 3.1 版排雷审计（9场分胜负全量排雷成功）

### Community 17 - "2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）"
Cohesion: 0.40
Nodes (4): 🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）, 一、 今日黄金猎物精选榜单, 二、 今日一票否决淘汰场次（全部触犯 3.1 版硬红线）

## Knowledge Gaps
- **65 isolated node(s):** `1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误`, `1. 赛前（T-2h）已知客观数据流水`, `2. 为什么会被模型一票否决漏网？（认知根因）`, `2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡`, `三、 闭环演化：两道物理级断路器系统升级（写入代码与大脑）` (+60 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 89 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DDD Onion Architecture & System Specs` connect `对账机.py` to `心电图录像机.py`?**
  _High betweenness centrality (0.476) - this node is a cross-community bridge._
- **Why does `8-Capas Betting Deduction Model` connect `8-Capas Betting Deduction Model` to `ELO-Odds Rating System`, `Success Score Metric`, `KTH 2024 Betting Exchange Liquidity Study`, `Egidi Hierarchical Bayesian Poisson Model`?**
  _High betweenness centrality (0.379) - this node is a cross-community bridge._
- **Why does `Football Quant Agent Brain` connect `8-Capas Betting Deduction Model` to `Favourite-Longshot-Bias-Adjusted GLM (FL-GLM)`, `Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计`, `Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制`, `Q: 系统规范README与智慧大脑AGENTS协同架构`?**
  _High betweenness centrality (0.312) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `赔率数值` (e.g. with `体彩官方适配器` and `本地账本仓储`) actually correct?**
  _`赔率数值` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `赔率账本契约` (e.g. with `回溯连续轨迹用例` and `探测并记录心电图用例`) actually correct?**
  _`赔率账本契约` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `本地账本仓储` (e.g. with `赔率快照` and `赔率数值`) actually correct?**
  _`本地账本仓储` has 2 INFERRED edges - model-reasoned connections that need verification._