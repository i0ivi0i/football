# Graph Report - 足球预测  (2026-09-12)

## Corpus Check
- 53 files · ~158,455 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 264 nodes · 777 edges · 17 communities (16 shown, 1 thin omitted)
- Extraction: 65% EXTRACTED · 35% INFERRED · 0% AMBIGUOUS · INFERRED: 275 edges (avg confidence: 0.58)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `721df44d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 赔率快照
- Any
- 对账机.py
- 8-Capas Betting Deduction Model
- 心电图录像机.py
- Sentiment Bias in Betting Odds
- Football Quant Agent Brain
- 体彩官方适配器
- Five Hard Red Lines (V3.1 Physical Circuit Breakers)
- 本地账本仓储
- 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- Q: 系统规范README与智慧大脑AGENTS协同架构
- 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）
- query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md
- Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制

## God Nodes (most connected - your core abstractions)
1. `8-Capas Betting Deduction Model` - 61 edges
2. `赔率快照` - 44 edges
3. `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` - 35 edges
4. `Shin Insider Trading Odds Inversion Model` - 33 edges
5. `Football Quant Agent Brain` - 29 edges
6. `赔率数值` - 25 edges
7. `General Post-Mortem Manual & Blind-Spot Audit` - 25 edges
8. `微观球员适配器` - 24 edges
9. `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` - 24 edges
10. `本地账本仓储` - 23 edges

## Surprising Connections (you probably didn't know these)
- `2026-09-11 Pre-Match Forecast` --records_coritiba_and_seville_heartbeat--> `本地账本仓储`  [INFERRED]
  分析复盘记录/2026-09-11_预测.md → 脚本/适配器/本地账本.py
- `本地账本仓储` --persists_order_flow_time_series--> `Betting Exchange Liquidity Dynamics`  [INFERRED]
  脚本/适配器/本地账本.py → 温故而知新学习资料/2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md
- `本地账本仓储` --controlled_by_brain--> `Football Quant Agent Brain`  [INFERRED]
  脚本/适配器/本地账本.py → AGENTS.md
- `本地账本仓储` --stores_liquidity_trajectory--> `KTH 2024 Betting Exchange Liquidity Study`  [INFERRED]
  脚本/适配器/本地账本.py → 温故而知新学习资料/2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md
- `本地账本仓储` --part_of_ddd_onion_architecture--> `DDD Onion Architecture & System Specs`  [INFERRED]
  脚本/适配器/本地账本.py → README.md

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

## Communities (17 total, 1 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.24
Nodes (8): test_客优于主且平赔下降精准识别为伪降水诱平(), test_极热假深盘诱主阻平形态识别(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入(), test_赔率数值验证与去水计算(), DDD 领域模型核心 - 纯净 Python，零框架依赖 包含：胜平负赔率值对象、时序位移值对象、单场比赛心电图聚合根实体, 按 Shin/去抽水归一化算法反推真实无抽水平率, 赔率数值

### Community 1 - "赔率快照"
Cohesion: 0.17
Nodes (8): Numerical Variant of Shin Conversion, 内存模拟提供者, 内存模拟账本, 输出端口：心电图轨迹的数据持久化与历史回溯, 赔率账本契约, 聚合根实体：带时间戳与赛事身份的心电图观测点, 富领域模型核心行为：计算连续轨迹的倾斜角与定性, 赔率快照

### Community 2 - "Any"
Cohesion: 0.17
Nodes (6): Any, 从 Understat 提取球员微观进攻链 xG Chain、xG Buildup 与关键传球数据, 强制断言比赛状态必须为 FT (Match Finished)，绝不采信滚球过程临时比分, 获取比赛双方的核心伤停名单、缺阵原因与战术位置, 从 sports-skills (Understat / ESPN) 提取 xG、射正、门将扑救与战术犯规微观指标, 从 football-data.co.uk 提取双方历史交锋总场次、平局场次与平局基因率

### Community 3 - "对账机.py"
Cohesion: 0.60
Nodes (3): 中国体彩足球平局自动化对账机 (对账机.py) 用于扫描 分析复盘记录/*_复盘.md，自动聚合计算总胜率与复盘手法，并实时无缝物理刷新： 1.…, 刷新总对账看板(), test_对账看板能正常聚合数据并更新总准确率文件()

### Community 4 - "8-Capas Betting Deduction Model"
Cohesion: 0.11
Nodes (38): ELO-Goals Rating System, ELO-Result Rating System, Passing Network Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events Dataset, 8-Capas Betting Deduction Model, Constantinou Hybrid Bayesian Network Model, Egidi Hierarchical Bayesian Poisson Model (+30 more)

### Community 5 - "心电图录像机.py"
Cohesion: 0.18
Nodes (12): ABC, 回溯连续轨迹用例, 探测并记录心电图用例, main(), 足球倍率心电图连续录像机 - 组装根 (Composition Root) 纯正 10/10 DDD 洋葱整洁架构，信达雅全中文命名, 展示比赛轨迹(), 执行单次探测(), 组装架构() (+4 more)

### Community 6 - "Sentiment Bias in Betting Odds"
Cohesion: 0.08
Nodes (31): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Favourite-Longshot Bias (FLB), Goto et al. (2026) Odds-Only and FL-GLM Conversion Study (+23 more)

### Community 7 - "Football Quant Agent Brain"
Cohesion: 0.27
Nodes (12): Football Quant Agent Brain, DDD Onion Architecture & System Specs, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例, 记录结果 (+4 more)

### Community 8 - "体彩官方适配器"
Cohesion: 0.16
Nodes (10): Bookmakers' Consensus Probability, Betting Exchange Liquidity Dynamics, Technical Indicators (SMA & RSI), solve_shin_probabilities Solver, Bettor State-Space Model (SSM), test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照 (+2 more)

### Community 9 - "Five Hard Red Lines (V3.1 Physical Circuit Breakers)"
Cohesion: 0.14
Nodes (44): ELO-Odds Rating System, Informational Loss Metric, Five Hard Red Lines (V3.1 Physical Circuit Breakers), Karpathy Skill Self-Evolution Flywheel, Asian Handicap (AH) Betting Market, Favourite-Longshot-Bias-Adjusted GLM (FL-GLM), Odds-Only Equal Profitability Confidence (OO-EPC), Mandadapu (2024) Football Match Outcome Forecasting Study (+36 more)

### Community 10 - "本地账本仓储"
Cohesion: 0.19
Nodes (8): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), 赔率快照, DDD 输出适配器 - SQLite 赔率心电图连续账本 负责在结构化本地数据目录中存储和检索时序快照, 实现赔率账本契约，基于轻量高效的标准库 SQLite, 本地账本仓储

### Community 13 - "一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）"
Cohesion: 0.33
Nodes (6): 1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】, 2026-09-11 竞彩足球平局精算推演报告, 2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】, 3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】, 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）, 二、 严格过筛：红线断路器执行记录

### Community 14 - "Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes

### Community 15 - "Q: 系统规范README与智慧大脑AGENTS协同架构"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 系统规范README与智慧大脑AGENTS协同架构, Source Nodes

### Community 17 - "2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）"
Cohesion: 0.50
Nodes (4): 🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）, 一、 今日黄金猎物精选榜单, 二、 今日一票否决淘汰场次（全部触犯 3.1 版硬红线）

### Community 21 - "Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes

## Knowledge Gaps
- **38 isolated node(s):** `1. 赛前（T-2h）已知客观数据流水`, `2. 为什么会被模型一票否决漏网？（认知根因）`, `1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】`, `2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】`, `3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】` (+33 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 70 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `8-Capas Betting Deduction Model` connect `8-Capas Betting Deduction Model` to `赔率数值`, `赔率快照`, `Sentiment Bias in Betting Odds`, `Football Quant Agent Brain`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`?**
  _High betweenness centrality (0.278) - this node is a cross-community bridge._
- **Why does `Football Quant Agent Brain` connect `Football Quant Agent Brain` to `赔率数值`, `赔率快照`, `8-Capas Betting Deduction Model`, `心电图录像机.py`, `Sentiment Bias in Betting Odds`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `本地账本仓储`, `Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计`, `Q: 系统规范README与智慧大脑AGENTS协同架构`, `query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md`, `Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制`?**
  _High betweenness centrality (0.251) - this node is a cross-community bridge._
- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `8-Capas Betting Deduction Model`, `心电图录像机.py`, `Sentiment Bias in Betting Odds`, `Football Quant Agent Brain`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `本地账本仓储`?**
  _High betweenness centrality (0.164) - this node is a cross-community bridge._
- **Are the 26 inferred relationships involving `8-Capas Betting Deduction Model` (e.g. with `DIFFATTEND Proxy` and `ELO-Goals Rating System`) actually correct?**
  _`8-Capas Betting Deduction Model` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` (e.g. with `Bookmakers' Consensus Probability` and `ELO-Goals Rating System`) actually correct?**
  _`Five Hard Red Lines (V3.1 Physical Circuit Breakers)` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `Shin Insider Trading Odds Inversion Model` (e.g. with `2026-09-06 Pre-Match Forecast` and `2026-09-07 Pre-Match Forecast`) actually correct?**
  _`Shin Insider Trading Odds Inversion Model` has 25 INFERRED edges - model-reasoned connections that need verification._