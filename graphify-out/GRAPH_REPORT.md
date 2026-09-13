# Graph Report - 足球预测  (2026-09-13)

## Corpus Check
- 54 files · ~159,749 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 292 nodes · 829 edges · 19 communities (18 shown, 1 thin omitted)
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 296 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d45d0989`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率数值
- 赔率快照
- 深度联想连线.py
- 对账机.py
- 微观球员适配器
- 赔率账本契约
- test_领域模型.py
- Football Quant Agent Brain
- 体彩接口.py
- Five Hard Red Lines (V3.1 Physical Circuit Breakers)
- 8-Capas Betting Deduction Model
- 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）
- KTH 2024 Betting Exchange Liquidity Study
- 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- Q: 系统规范README与智慧大脑AGENTS协同架构
- 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告
- query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md
- Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制

## God Nodes (most connected - your core abstractions)
1. `8-Capas Betting Deduction Model` - 62 edges
2. `赔率快照` - 44 edges
3. `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` - 36 edges
4. `Shin Insider Trading Odds Inversion Model` - 34 edges
5. `Football Quant Agent Brain` - 32 edges
6. `General Post-Mortem Manual & Blind-Spot Audit` - 30 edges
7. `赔率数值` - 25 edges
8. `体彩官方适配器` - 24 edges
9. `微观球员适配器` - 24 edges
10. `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` - 24 edges

## Surprising Connections (you probably didn't know these)
- `add_edge()` --bridges_to_main_trinity--> `Football Quant Agent Brain`  [INFERRED]
  脚本/深度联想连线.py → AGENTS.md
- `探测并记录心电图用例` --executes_t_2h_physical_lockin--> `Karpathy Skill Self-Evolution Flywheel`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md
- `回溯连续轨迹用例` --controlled_by_brain--> `Football Quant Agent Brain`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md
- `回溯连续轨迹用例` --supplies_capa1_heartbeat_trend--> `8-Capas Betting Deduction Model`  [INFERRED]
  脚本/应用/用例.py → AGENTS.md
- `回溯连续轨迹用例` --part_of_ddd_onion_architecture--> `DDD Onion Architecture & System Specs`  [INFERRED]
  脚本/应用/用例.py → README.md

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

## Communities (19 total, 1 thin omitted)

### Community 0 - "赔率数值"
Cohesion: 0.20
Nodes (9): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), 赔率快照, DDD 输出适配器 - SQLite 赔率心电图连续账本 负责在结构化本地数据目录中存储和检索时序快照, 实现赔率账本契约，基于轻量高效的标准库 SQLite, 本地账本仓储 (+1 more)

### Community 1 - "赔率快照"
Cohesion: 0.17
Nodes (10): Numerical Variant of Shin Conversion, 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, 赔率快照, 聚合根实体：带时间戳与赛事身份的心电图观测点 (+2 more)

### Community 2 - "深度联想连线.py"
Cohesion: 0.50
Nodes (3): 全量超密集知识图谱编织引擎 (Graphify Ultra-Dense Semantic Mesh Synthesizer) 将全项目 34…, 超密集编织图谱(), add_edge()

### Community 3 - "对账机.py"
Cohesion: 0.60
Nodes (3): 中国体彩足球平局自动化对账机 (对账机.py) 用于扫描 分析复盘记录/*_复盘.md，自动聚合计算总胜率与复盘手法，并实时无缝物理刷新： 1.…, 刷新总对账看板(), test_对账看板能正常聚合数据并更新总准确率文件()

### Community 4 - "微观球员适配器"
Cohesion: 0.14
Nodes (13): Any, test_微观球员适配器提取交锋历史H2H(), test_微观球员适配器提取比赛微观高阶数据(), test_微观球员适配器提取球员高阶链条数据(), test_微观球员适配器解析伤停数据(), test_微观球员适配器计算体能负荷(), DDD 适配器：API-Sports 微观球员与伤停数据管道 支持双 Key 轮换，负责拉取核心伤停、关键组织大脑与防守对抗数据, 从 Understat 提取球员微观进攻链 xG Chain、xG Buildup 与关键传球数据 (+5 more)

### Community 5 - "赔率账本契约"
Cohesion: 0.18
Nodes (13): ABC, 回溯连续轨迹用例, 探测并记录心电图用例, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, main(), 足球倍率心电图连续录像机 - 组装根 (Composition Root) 纯正 10/10 DDD 洋葱整洁架构，信达雅全中文命名, 展示比赛轨迹() (+5 more)

### Community 6 - "test_领域模型.py"
Cohesion: 0.16
Nodes (13): 物理守卫：断言自规范确立以来的预测报告中每个核心推荐场次都必须包含规范的 Polymarket 直达链接, 断言当体彩关闭胜平负时，防守漏风且面对全主力豪门绝不能盲目买平, 断言当进攻核心缺阵但后腰对抗率低于60%时，必须一票否决假闷平, test_攻防伤停平衡校验防017假闷平崩盘(), test_红线7关闭胜平负时必须校验受让方铁桶指标防无脑买平(), test_赔率快照计算连续位移与异动信号(), test_赔率数值拒绝非正数非法输入(), test_预测报告必须附带Polymarket直达链接() (+5 more)

### Community 7 - "Football Quant Agent Brain"
Cohesion: 0.24
Nodes (12): Football Quant Agent Brain, DDD Onion Architecture & System Specs, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 探测并记录心电图用例, 记录结果, 轨迹结果, 实现赔率提供者契约，直连国家体彩中心官方网关 (+4 more)

### Community 8 - "体彩接口.py"
Cohesion: 0.40
Nodes (3): test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), DDD 适配器防腐层 - 中国体彩官方 API 适配器 负责将不可控的外部体彩原始 JSON 清洗转化为优雅纯净的领域实体

### Community 9 - "Five Hard Red Lines (V3.1 Physical Circuit Breakers)"
Cohesion: 0.10
Nodes (38): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Five Hard Red Lines (V3.1 Physical Circuit Breakers) (+30 more)

### Community 10 - "8-Capas Betting Deduction Model"
Cohesion: 0.12
Nodes (57): ELO-Goals Rating System, ELO-Odds Rating System, ELO-Result Rating System, Informational Loss Metric, Passing Network Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events Dataset, 8-Capas Betting Deduction Model (+49 more)

### Community 11 - "2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）"
Cohesion: 0.50
Nodes (4): 🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）, 一、 今日黄金猎物精选榜单, 二、 今日一票否决淘汰场次（全部触犯 3.1 版硬红线）

### Community 12 - "KTH 2024 Betting Exchange Liquidity Study"
Cohesion: 0.10
Nodes (21): Betting Exchange Liquidity Dynamics, Technical Indicators (SMA & RSI), Favourite-Longshot Bias (FLB), Goto et al. (2026) Odds-Only and FL-GLM Conversion Study, Chi-squared Test Feature Selection, Multilayer Perceptron (Betting Exchange), Recursive Feature Elimination (RFE), Relative Strength Index (RSI Classifier) (+13 more)

### Community 13 - "一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）"
Cohesion: 0.33
Nodes (6): 1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】, 2026-09-11 竞彩足球平局精算推演报告, 2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】, 3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】, 一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）, 二、 严格过筛：红线断路器执行记录

### Community 14 - "Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes

### Community 15 - "Q: 系统规范README与智慧大脑AGENTS协同架构"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 系统规范README与智慧大脑AGENTS协同架构, Source Nodes

### Community 17 - "2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.18
Nodes (11): 1. 红线 2（伪降水死锁）机械误杀三大豪门客平局（018 摩纳哥 1:1、020 米兰 2:2、028 里昂 0:0）, 1. 赛前已知特征与当时推演假设, 1. 赛前推演与当时假设, 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告, 2. 真实赛况与血淋淋认知盲区, 2. 真实赛果与 `football-match-analysis` 硬核量化复盘, 2. 红线 4（均势大球前置锁）机械误杀两场对攻大球平局（013 伯恩茅斯 2:2、023 科隆 1:1）, 3. 红线 1（强队深盘一票否决）机械误杀四大豪门冷平（010 勒沃库森 2:2、012 切尔西 2:2、016 利物浦 0:0、024 毕包 1:1） (+3 more)

### Community 21 - "Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes

## Knowledge Gaps
- **44 isolated node(s):** `Answer`, `Outcome`, `Source Nodes`, `Answer`, `Outcome` (+39 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 82 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Football Quant Agent Brain` connect `Football Quant Agent Brain` to `赔率数值`, `赔率快照`, `深度联想连线.py`, `微观球员适配器`, `赔率账本契约`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `8-Capas Betting Deduction Model`, `KTH 2024 Betting Exchange Liquidity Study`, `Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计`, `Q: 系统规范README与智慧大脑AGENTS协同架构`, `2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告`, `query_20260909_022637_7cd78681_2026_09_08_赛后复盘与模型3_1硬红线升级.md`, `Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制`?**
  _High betweenness centrality (0.276) - this node is a cross-community bridge._
- **Why does `8-Capas Betting Deduction Model` connect `8-Capas Betting Deduction Model` to `赔率数值`, `赔率快照`, `微观球员适配器`, `赔率账本契约`, `Football Quant Agent Brain`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `KTH 2024 Betting Exchange Liquidity Study`?**
  _High betweenness centrality (0.247) - this node is a cross-community bridge._
- **Why does `赔率快照` connect `赔率快照` to `赔率数值`, `赔率账本契约`, `test_领域模型.py`, `Football Quant Agent Brain`, `体彩接口.py`, `Five Hard Red Lines (V3.1 Physical Circuit Breakers)`, `8-Capas Betting Deduction Model`, `KTH 2024 Betting Exchange Liquidity Study`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `8-Capas Betting Deduction Model` (e.g. with `DIFFATTEND Proxy` and `ELO-Goals Rating System`) actually correct?**
  _`8-Capas Betting Deduction Model` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `赔率快照` (e.g. with `轨迹结果` and `内存模拟提供者`) actually correct?**
  _`赔率快照` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `Five Hard Red Lines (V3.1 Physical Circuit Breakers)` (e.g. with `Bookmakers' Consensus Probability` and `ELO-Goals Rating System`) actually correct?**
  _`Five Hard Red Lines (V3.1 Physical Circuit Breakers)` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `Shin Insider Trading Odds Inversion Model` (e.g. with `2026-09-06 Pre-Match Forecast` and `2026-09-07 Pre-Match Forecast`) actually correct?**
  _`Shin Insider Trading Odds Inversion Model` has 26 INFERRED edges - model-reasoned connections that need verification._