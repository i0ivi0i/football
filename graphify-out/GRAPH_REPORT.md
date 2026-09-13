# Graph Report - 足球预测  (2026-09-13)

## Corpus Check
- 55 files · ~160,227 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 307 nodes · 850 edges · 18 communities (16 shown, 2 thin omitted)
- Extraction: 65% EXTRACTED · 35% INFERRED · 0% AMBIGUOUS · INFERRED: 300 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3bad8c52`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 赔率快照
- 深度联想连线.py
- Football Quant Agent Brain
- 微观球员适配器
- 心电图录像机.py
- Five Hard Red Lines (V3.1 Physical Circuit Breakers)
- 体彩官方适配器
- 2026-09-13（周日）中国体育彩票精算推演报告
- General Post-Mortem Manual & Blind-Spot Audit
- 8-Capas Betting Deduction Model
- 契约.py
- Sentiment Bias in Betting Odds
- 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- Q: 系统规范README与智慧大脑AGENTS协同架构
- query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md
- Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制

## God Nodes (most connected - your core abstractions)
1. `8-Capas Betting Deduction Model` - 62 edges
2. `赔率快照` - 44 edges
3. `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` - 38 edges
4. `Shin Insider Trading Odds Inversion Model` - 34 edges
5. `Football Quant Agent Brain` - 32 edges
6. `General Post-Mortem Manual & Blind-Spot Audit` - 31 edges
7. `赔率数值` - 25 edges
8. `体彩官方适配器` - 24 edges
9. `微观球员适配器` - 24 edges
10. `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` - 24 edges

## Surprising Connections (you probably didn't know these)
- `add_edge()` --bridges_to_main_trinity--> `Football Quant Agent Brain`  [INFERRED]
  脚本/深度联想连线.py → AGENTS.md
- `探测并记录心电图用例` --controlled_by_brain--> `Football Quant Agent Brain`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md
- `探测并记录心电图用例` --executes_t_2h_physical_lockin--> `Karpathy Skill Self-Evolution Flywheel`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md
- `探测并记录心电图用例` --part_of_ddd_onion_architecture--> `DDD Onion Architecture & System Specs`  [INFERRED]
  脚本/应用/用例.py → README.md
- `回溯连续轨迹用例` --supplies_capa1_heartbeat_trend--> `8-Capas Betting Deduction Model`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md

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

## Communities (18 total, 2 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.17
Nodes (11): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), test_赔率快照计算连续位移与异动信号(), 赔率快照, DDD 输出适配器 - SQLite 赔率心电图连续账本 负责在结构化本地数据目录中存储和检索时序快照, 实现赔率账本契约，基于轻量高效的标准库 SQLite (+3 more)

### Community 1 - "赔率快照"
Cohesion: 0.24
Nodes (8): 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, 聚合根实体：带时间戳与赛事身份的心电图观测点, 富领域模型核心行为：计算连续轨迹的倾斜角与定性, 赔率快照

### Community 2 - "深度联想连线.py"
Cohesion: 0.50
Nodes (3): 全量超密集知识图谱编织引擎 (Graphify Ultra-Dense Semantic Mesh Synthesizer) 将全项目 34…, 超密集编织图谱(), add_edge()

### Community 3 - "Football Quant Agent Brain"
Cohesion: 0.29
Nodes (10): Football Quant Agent Brain, DDD Onion Architecture & System Specs, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 记录结果, 轨迹结果, 输出端口：心电图轨迹的数据持久化与历史回溯 (+2 more)

### Community 4 - "微观球员适配器"
Cohesion: 0.11
Nodes (18): Passing Network Centrality, Wyscout Spatio-Temporal Match Events Dataset, Any, Dynamic Seasonal Team Attack and Defence Effects, Match Outcome Classification via Thresholds, Success Score Metric, test_微观球员适配器提取交锋历史H2H(), test_微观球员适配器提取比赛微观高阶数据() (+10 more)

### Community 5 - "心电图录像机.py"
Cohesion: 0.36
Nodes (7): 回溯连续轨迹用例, 探测并记录心电图用例, main(), 足球倍率心电图连续录像机 - 组装根 (Composition Root) 纯正 10/10 DDD 洋葱整洁架构，信达雅全中文命名, 展示比赛轨迹(), 执行单次探测(), 组装架构()

### Community 6 - "Five Hard Red Lines (V3.1 Physical Circuit Breakers)"
Cohesion: 0.11
Nodes (22): Five Hard Red Lines (V3.1 Physical Circuit Breakers), 二、 五道硬红线 3.1 版排雷审计（9场分胜负全量排雷成功）, 2. 为什么会被模型错误一票否决？（三大认知根因剖析）, 根因一：机械教条主义滥用【红线 4】（前置条件校验严重缺失）, 根因三：国际对账只盯平博，忽视威廉希尔逆势压水 0.29 的内幕信号, 根因二：误把“高平阻盘”当成“无防平”, 1. 赛前（T-2h）已知客观数据流水, 2. 为什么会被模型一票否决漏网？（认知根因） (+14 more)

### Community 7 - "体彩官方适配器"
Cohesion: 0.15
Nodes (10): 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 探测并记录心电图用例, test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照, DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体, 实现赔率提供者契约，直连国家体彩中心官方网关, 体彩官方适配器 (+2 more)

### Community 8 - "2026-09-13（周日）中国体育彩票精算推演报告"
Cohesion: 0.14
Nodes (14): 1. Capa 1 [ODDS] 市场底牌与去水概率, 1. Capa 1 [ODDS] 市场底牌与去水概率, 1. Capa 1 [ODDS] 盘口结构, 2026-09-13（周日）中国体育彩票精算推演报告, 2. Capa 2 & 3 [IND/API] 球队画像与保级绞杀, 2. Capa 2 & 3 [IND/API] 球队画像与球员微观防守大闸, 2. Capa 5 & 8 战术博弈与落点, 3. Capa 4 & 5 [IND] 泊松联合概率与战术博弈 (+6 more)

### Community 9 - "General Post-Mortem Manual & Blind-Spot Audit"
Cohesion: 0.10
Nodes (30): Karpathy Skill Self-Evolution Flywheel, 2026-09-06 Post-Match Review, 2026-09-07 Post-Match Review, 2026-09-08 Post-Match Review, 2026-09-10 Post-Match Review, 2026-09-11 Post-Match Review, Overall Accuracy & Real-time Scoreboard, General Post-Mortem Manual & Blind-Spot Audit (+22 more)

### Community 10 - "8-Capas Betting Deduction Model"
Cohesion: 0.11
Nodes (56): ELO-Goals Rating System, ELO-Odds Rating System, ELO-Result Rating System, Informational Loss Metric, PlayeRank Framework, 8-Capas Betting Deduction Model, Asian Handicap (AH) Betting Market, Constantinou Hybrid Bayesian Network Model (+48 more)

### Community 12 - "Sentiment Bias in Betting Odds"
Cohesion: 0.08
Nodes (33): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Betting Exchange Liquidity Dynamics (+25 more)

### Community 13 - "一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）"
Cohesion: 0.33
Nodes (6): 1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】, 2026-09-11 竞彩足球平局精算推演报告, 2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】, 3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】, 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）, 二、 严格过筛：红线断路器执行记录

### Community 14 - "Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes

### Community 15 - "Q: 系统规范README与智慧大脑AGENTS协同架构"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 系统规范README与智慧大脑AGENTS协同架构, Source Nodes

### Community 21 - "Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes

## Knowledge Gaps
- **54 isolated node(s):** `Answer`, `Outcome`, `Source Nodes`, `Answer`, `Outcome` (+49 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 92 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Football Quant Agent Brain` connect `Football Quant Agent Brain` to `赔率数值`, `赔率快照`, `深度联想连线.py`, `微观球员适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `体彩官方适配器`, `General Post-Mortem Manual & Blind-Spot Audit`, `8-Capas Betting Deduction Model`, `Sentiment Bias in Betting Odds`, `Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计`, `Q: 系统规范README与智慧大脑AGENTS协同架构`, `query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md`, `Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制`?**
  _High betweenness centrality (0.269) - this node is a cross-community bridge._
- **Why does `8-Capas Betting Deduction Model` connect `8-Capas Betting Deduction Model` to `赔率数值`, `赔率快照`, `Football Quant Agent Brain`, `微观球员适配器`, `体彩官方适配器`, `General Post-Mortem Manual & Blind-Spot Audit`, `Sentiment Bias in Betting Odds`?**
  _High betweenness centrality (0.221) - this node is a cross-community bridge._
- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `Football Quant Agent Brain`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `体彩官方适配器`, `General Post-Mortem Manual & Blind-Spot Audit`, `8-Capas Betting Deduction Model`, `契约.py`, `Sentiment Bias in Betting Odds`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `8-Capas Betting Deduction Model` (e.g. with `DIFFATTEND Proxy` and `ELO-Goals Rating System`) actually correct?**
  _`8-Capas Betting Deduction Model` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` (e.g. with `Bookmakers' Consensus Probability` and `ELO-Goals Rating System`) actually correct?**
  _`Five Hard Red Lines (V3.1 Physical Circuit Breakers)` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `Shin Insider Trading Odds Inversion Model` (e.g. with `2026-09-06 Pre-Match Forecast` and `2026-09-07 Pre-Match Forecast`) actually correct?**
  _`Shin Insider Trading Odds Inversion Model` has 26 INFERRED edges - model-reasoned connections that need verification._