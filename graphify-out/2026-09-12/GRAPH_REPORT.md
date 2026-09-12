# Graph Report - 足球预测  (2026-09-12)

## Corpus Check
- 53 files · ~158,642 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 269 nodes · 797 edges · 17 communities (16 shown, 1 thin omitted)
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 290 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f1d07e10`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 赔率快照
- 深度联想连线.py
- 对账机.py
- 微观球员适配器
- 心电图录像机.py
- Shin Insider Trading Odds Inversion Model
- Football Quant Agent Brain
- 体彩官方适配器
- Five Hard Red Lines (V3.1 Physical Circuit Breakers)
- 8-Capas Betting Deduction Model
- 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）
- 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- Q: 系统规范README与智慧大脑AGENTS协同架构
- query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md
- Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制

## God Nodes (most connected - your core abstractions)
1. `8-Capas Betting Deduction Model` - 62 edges
2. `赔率快照` - 44 edges
3. `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` - 36 edges
4. `Shin Insider Trading Odds Inversion Model` - 34 edges
5. `Football Quant Agent Brain` - 30 edges
6. `General Post-Mortem Manual & Blind-Spot Audit` - 29 edges
7. `赔率数值` - 25 edges
8. `微观球员适配器` - 24 edges
9. `体彩官方适配器` - 24 edges
10. `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` - 24 edges

## Surprising Connections (you probably didn't know these)
- `add_edge()` --bridges_to_main_trinity--> `Football Quant Agent Brain`  [INFERRED]
  脚本/深度联想连线.py → AGENTS.md
- `8-Capas Betting Deduction Model` --capa1_parses_value_object--> `赔率数值`  [INFERRED]
  AGENTS.md → 脚本/领域/模型.py
- `赔率数值` --controlled_by_brain--> `Football Quant Agent Brain`  [INFERRED]
  脚本/领域/模型.py → AGENTS.md
- `赔率数值` --part_of_ddd_onion_architecture--> `DDD Onion Architecture & System Specs`  [INFERRED]
  脚本/领域/模型.py → README.md
- `赔率快照` --controlled_by_brain--> `Football Quant Agent Brain`  [INFERRED]
  脚本/领域/模型.py → AGENTS.md

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
Cohesion: 0.19
Nodes (13): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), test_客优于主且平赔下降精准识别为伪降水诱平(), test_极热假深盘诱主阻平形态识别(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入() (+5 more)

### Community 1 - "赔率快照"
Cohesion: 0.17
Nodes (7): Numerical Variant of Shin Conversion, 内存模拟提供者, 内存模拟账本, 赔率快照, 聚合根实体：带时间戳与赛事身份的心电图观测点, 富领域模型核心行为：计算连续轨迹的倾斜角与定性, 赔率快照

### Community 2 - "深度联想连线.py"
Cohesion: 0.50
Nodes (3): 全量超密集知识图谱编织引擎 (Graphify Ultra-Dense Semantic Mesh Synthesizer) 将全项目 34…, 超密集编织图谱(), add_edge()

### Community 3 - "对账机.py"
Cohesion: 0.60
Nodes (3): 中国体彩足球平局自动化对账机 (对账机.py) 用于扫描 分析复盘记录/*_复盘.md，自动聚合计算总胜率与复盘手法，并实时无缝物理刷新： 1.…, 刷新总对账看板(), test_对账看板能正常聚合数据并更新总准确率文件()

### Community 4 - "微观球员适配器"
Cohesion: 0.14
Nodes (13): Any, test_微观球员适配器提取交锋历史H2H(), test_微观球员适配器提取比赛微观高阶数据(), test_微观球员适配器提取球员高阶链条数据(), test_微观球员适配器解析伤停数据(), test_微观球员适配器计算体能负荷(), DDD 适配器：API-Sports 微观球员与伤停数据管道 支持双 Key 轮换，负责拉取核心伤停、关键组织大脑与防守对抗数据, 从 Understat 提取球员微观进攻链 xG Chain、xG Buildup 与关键传球数据 (+5 more)

### Community 5 - "心电图录像机.py"
Cohesion: 0.21
Nodes (11): ABC, 回溯连续轨迹用例, 探测并记录心电图用例, main(), 足球倍率心电图连续录像机 - 组装根 (Composition Root) 纯正 10/10 DDD 洋葱整洁架构，信达雅全中文命名, 展示比赛轨迹(), 执行单次探测(), 组装架构() (+3 more)

### Community 6 - "Shin Insider Trading Odds Inversion Model"
Cohesion: 0.06
Nodes (46): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Betting Exchange Liquidity Dynamics (+38 more)

### Community 7 - "Football Quant Agent Brain"
Cohesion: 0.18
Nodes (15): Football Quant Agent Brain, DDD Onion Architecture & System Specs, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例, 记录结果 (+7 more)

### Community 8 - "体彩官方适配器"
Cohesion: 0.24
Nodes (6): test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照, DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体, 实现赔率提供者契约，直连国家体彩中心官方网关, 体彩官方适配器

### Community 9 - "Five Hard Red Lines (V3.1 Physical Circuit Breakers)"
Cohesion: 0.16
Nodes (37): ELO-Odds Rating System, Informational Loss Metric, PlayeRank Framework, Five Hard Red Lines (V3.1 Physical Circuit Breakers), Karpathy Skill Self-Evolution Flywheel, Asian Handicap (AH) Betting Market, Odds-Only Equal Profitability Confidence (OO-EPC), Mandadapu (2024) Football Match Outcome Forecasting Study (+29 more)

### Community 10 - "8-Capas Betting Deduction Model"
Cohesion: 0.14
Nodes (30): ELO-Goals Rating System, ELO-Result Rating System, Passing Network Centrality, Wyscout Spatio-Temporal Match Events Dataset, 8-Capas Betting Deduction Model, Constantinou Hybrid Bayesian Network Model, Egidi Hierarchical Bayesian Poisson Model, Elo Rating Difference (+22 more)

### Community 11 - "2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）"
Cohesion: 0.50
Nodes (4): 🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）, 一、 今日黄金猎物精选榜单, 二、 今日一票否决淘汰场次（全部触犯 3.1 版硬红线）

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
- **38 isolated node(s):** `1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】`, `2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】`, `3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】`, `二、 严格过筛：红线断路器执行记录`, `Answer` (+33 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 71 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `8-Capas Betting Deduction Model` connect `8-Capas Betting Deduction Model` to `赔率数值`, `赔率快照`, `微观球员适配器`, `Shin Insider Trading Odds Inversion Model`, `Football Quant Agent Brain`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`?**
  _High betweenness centrality (0.268) - this node is a cross-community bridge._
- **Why does `Football Quant Agent Brain` connect `Football Quant Agent Brain` to `赔率数值`, `赔率快照`, `深度联想连线.py`, `微观球员适配器`, `心电图录像机.py`, `Shin Insider Trading Odds Inversion Model`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `8-Capas Betting Deduction Model`, `Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计`, `Q: 系统规范README与智慧大脑AGENTS协同架构`, `query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md`, `Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制`?**
  _High betweenness centrality (0.264) - this node is a cross-community bridge._
- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `心电图录像机.py`, `Shin Insider Trading Odds Inversion Model`, `Football Quant Agent Brain`, `体彩官方适配器`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `8-Capas Betting Deduction Model`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `8-Capas Betting Deduction Model` (e.g. with `DIFFATTEND Proxy` and `ELO-Goals Rating System`) actually correct?**
  _`8-Capas Betting Deduction Model` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` (e.g. with `Bookmakers' Consensus Probability` and `ELO-Goals Rating System`) actually correct?**
  _`Five Hard Red Lines (V3.1 Physical Circuit Breakers)` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `Shin Insider Trading Odds Inversion Model` (e.g. with `2026-09-06 Pre-Match Forecast` and `2026-09-07 Pre-Match Forecast`) actually correct?**
  _`Shin Insider Trading Odds Inversion Model` has 26 INFERRED edges - model-reasoned connections that need verification._