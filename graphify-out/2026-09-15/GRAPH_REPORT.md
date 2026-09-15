# Graph Report - 足球预测  (2026-09-15)

## Corpus Check
- 72 files · ~1,344,444 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .db 1)

## Summary
- 633 nodes · 1382 edges · 58 communities (42 shown, 16 thin omitted)
- Extraction: 62% EXTRACTED · 29% INFERRED · 9% AMBIGUOUS · INFERRED: 401 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0c5e1508`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 赔率快照
- 足球概率分析现行规程
- 微观球员适配器
- 历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告
- **Forecast evaluation for data scientists: common pitfalls and best practices**
- 预测记录与智慧复盘契约
- Sentiment Bias in Betting Odds
- 足球概率预测评分比较（Wheatcroft，2019预印本）
- 2026-09-13（周日）中国体育彩票精算推演报告
- What You Must Do When Invoked
- **RESULTS**
- 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告
- **DISCUSSION**
- 刷新总对账看板
- **METHOD**
- 历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告
- Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计
- 2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）
- Q: 系统规范README与智慧大脑AGENTS协同架构
- Shin与比例归一化：方法说明及适用边界
- graphify reference: extra exports and benchmark
- PDF 第 16 页
- **4 Guidelines and best practices for forecast evaluation**
- 二、 核心败因深度解剖（四大低级错误）
- graphify reference: query, path, explain
- PDF 第 14 页
- graphify reference: add a URL and watch a folder
- 2023_Aiyer_结果偏见与决策评价.md
- PDF 第 8 页
- PDF 第 12 页
- **3 Motivation and common pitfalls**
- PDF 第 15 页
- PDF 第 17 页
- PDF 第 22 页
- PDF 第 23 页
- PDF 第 24 页
- PDF 第 25 页
- PDF 第 34 页
- PDF 第 28 页
- 赔率账本契约
- 2026-09-14（周一）中国体育彩票精算推演报告
- **ABSTRACT**
- 历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- 2026-09-09（周三）中国体彩平局全要素深度复盘报告
- 已取代：智慧复盘论文索引
- 本地账本仓储
- 赔率数值
- 体彩官方适配器
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- graphify reference: GitHub clone and cross-repo merge
- 超密集编织图谱
- 二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？
- transcribe.md
- Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey’s (1988) Outcome Bias Experiment 1
- graphify reference: extraction subagent prompt (compact)
- Q: 2026-09-08 赛后复盘与模型3.1硬红线升级
- Forecast evaluation for data scientists: common pitfalls and best practices

## God Nodes (most connected - your core abstractions)
1. `足球概率分析现行规程` - 73 edges
2. `**Forecast evaluation for data scientists: common pitfalls and best practices**` - 52 edges
3. `赔率快照` - 48 edges
4. `智慧经验与习惯塑形` - 41 edges
5. `Wheatcroft 论文 Markdown（附公式与图表）` - 31 edges
6. `Sentiment Bias in Betting Odds` - 31 edges
7. `赔率数值` - 29 edges
8. `Tests of Conditional Predictive Ability` - 29 edges
9. `PlayeRank Framework` - 29 edges
10. `Hierarchical Bayesian Poisson Football Score Model` - 28 edges

## Surprising Connections (you probably didn't know these)
- `test_回溯连续轨迹用例提炼单边变盘态势()` --legacy_unverified_relation--> `KTH 2024 Betting Exchange Liquidity Study`  [AMBIGUOUS]
  脚本/测试/test_业务用例.py → 温故而知新学习资料/2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md
- `test_微观球员适配器严格断言完场比分()` --legacy_unverified_relation--> `Overall Accuracy & Real-time Scoreboard`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py → 分析复盘记录/总准确率.md
- `test_微观球员适配器提取球员高阶链条数据()` --legacy_unverified_relation--> `PlayeRank Framework`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py → 温故而知新学习资料/2019_Nature_PlayeRank_Data_Driven_Framework.md
- `test_微观球员适配器提取球员高阶链条数据()` --legacy_unverified_relation--> `Success Score Metric`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py → 温故而知新学习资料/2025_Success_Score_Deep_Learning_Football_Prediction.md
- `体彩官方适配器` --legacy_unverified_relation--> `Bookmakers' Consensus Probability`  [AMBIGUOUS]
  脚本/适配器/体彩接口.py → 温故而知新学习资料/1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Daily Actuarial Deduction and Audit Cycle** — rec_20260908_forecast, rec_20260908_review, rec_20260909_forecast [EXTRACTED 0.95]
- **Soccer ELO Rating System Hierarchy** — 2018_plos_elo_odds, 2018_plos_elo_goals, 2018_plos_elo_result [EXTRACTED 0.95]
- **Reverse Odds to Probability Conversion Methods** — goto2026_oo_epc, wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_analytical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_power_conversion [EXTRACTED 0.95]
- **Football Match Outcome Modelling Paradigms** — 温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_draw_prediction_evaluation, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_dnn_model, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bookmaker_odds_model [INFERRED 0.85]
- **Betting Market Aggregate Information Framework** — 1710_02824_consensus_probability, 2018_plos_elo_odds, 2008_sentiment_sentiment_bias [INFERRED 0.85]
- **Soccer Match Outcome Forecasting Frameworks** — egidi_hierarchical_poisson_model, constantinou_hybrid_bn_model, ordered_logit_regression, multinomial_logit_regression [INFERRED 0.85]

## Communities (58 total, 16 thin omitted)

### Community 0 - "赔率快照"
Cohesion: 0.24
Nodes (9): 赔率快照, test_回溯连续轨迹用例提炼单边变盘态势(), test_探测并记录心电图用例捕获关闭基础胜平负场次(), test_探测并记录心电图用例捕获异动跳水(), 内存模拟提供者, 内存模拟账本, 聚合根实体：带时间戳与赛事身份的心电图观测点, 只比较同场、同市场、同让球线且时间递增的观测。 (+1 more)

### Community 1 - "足球概率分析现行规程"
Cohesion: 0.15
Nodes (58): Choe与Ramdas：序贯预测者比较, Dimitriadis等：CORP稳定可靠性图, Giacomini与White：条件预测能力检验, Macrì-Demartino等：动态历史信息借用, 智慧复盘论文索引, 论文的方法角色与迁移边界, 反例、适用范围与失效条件, 习惯塑形 (+50 more)

### Community 2 - "微观球员适配器"
Cohesion: 0.11
Nodes (18): Any, test_微观球员适配器严格断言完场比分(), test_微观球员适配器提取交锋历史H2H(), test_微观球员适配器提取比赛微观高阶数据(), test_微观球员适配器提取球员高阶链条数据(), test_微观球员适配器解析伤停数据(), test_微观球员适配器计算体能负荷(), test_加时完场取常规时间比分() (+10 more)

### Community 3 - "历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.20
Nodes (10): 历史待核查：1. 赛前（T-2h）已知客观数据流水, 历史待核查：1. 赛前已知数据与操盘陷阱, 历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告, 历史待核查：2. 为什么会被模型错误一票否决？（三大认知根因剖析）, 历史待核查：一、 唯一平局漏网盲区深度审计：【周四001 费内巴切 1:1 罗马】, 历史待核查：三、 经验物理固化与飞轮升级成果, 历史待核查：二、 周四007【德尔瓦耶 0:2 弗拉门戈】单挑失手深度复盘, 历史待核查：根因一：机械教条主义滥用【红线 4】（前置条件校验严重缺失） (+2 more)

### Community 4 - "**Forecast evaluation for data scientists: common pitfalls and best practices**"
Cohesion: 0.05
Nodes (39): **1 Introduction**, **2 Terminology of forecast evaluation**, **5 Conclusions**, **Abstract**, **Forecast evaluation for data scientists: common pitfalls and best practices**, PDF 第 10 页, PDF 第 11 页, PDF 第 13 页 (+31 more)

### Community 5 - "预测记录与智慧复盘契约"
Cohesion: 0.33
Nodes (6): 概率评分、校准、命中率与收益分开, 赛前实际时间与版本封存, 先审过程再揭示赛果, 冻结假设与未来样本比较, 预测记录与智慧复盘契约, 温故而知新：论文与方法资料库

### Community 6 - "Sentiment Bias in Betting Odds"
Cohesion: 0.06
Nodes (69): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, ELO-Goals Rating System (+61 more)

### Community 7 - "足球概率预测评分比较（Wheatcroft，2019预印本）"
Cohesion: 0.12
Nodes (16): Ignorance 对数评分, 足球概率预测评分比较（Wheatcroft，2019预印本）, 概率预测评分, RPS 排序距离假设, 决策质量与赛果分离审查, 结果偏见, 结果偏见与决策质量评价（Aiyer 等，2023）, 预注册重复实验 (+8 more)

### Community 8 - "2026-09-13（周日）中国体育彩票精算推演报告"
Cohesion: 0.12
Nodes (16): 1. Capa 1 [ODDS] 市场底牌与心电图轨迹, 1. Capa 1 [ODDS] 盘口结构, 1. Capa 1 [ODDS] 盘口结构, 1. 乔布斯灵活思维解构（破除红线2死板一刀切）, 1. 盘口与战术特征, 2026-09-13（周日）中国体育彩票精算推演报告, 2. Capa 3 [API] 微观防守护城河核验, 2. Capa 4 & 7 泊松落点 (+8 more)

### Community 9 - "What You Must Do When Invoked"
Cohesion: 0.08
Nodes (24): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+16 more)

### Community 10 - "**RESULTS**"
Cohesion: 0.13
Nodes (15): **CONFIRMATORY (PRE-REGISTERED) RESULTS** Replication: Decision Quality, **EXPLORATORY RESULTS (NOT PREREGISTERED)**, **EXTENSIONS**, Mediation Analyses, PDF 第 10 页, PDF 第 11 页, PDF 第 7 页, PDF 第 8 页 (+7 more)

### Community 11 - "2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.22
Nodes (9): 1. 红线 2（伪降水死锁）机械误杀三大豪门客平局（018 摩纳哥 1:1、020 米兰 2:2、028 里昂 0:0）, 1. 赛前已知特征与当时推演假设, 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告, 2. 真实赛况与血淋淋认知盲区, 2. 红线 4（均势大球前置锁）机械误杀两场对攻大球平局（013 伯恩茅斯 2:2、023 科隆 1:1）, 3. 红线 1（强队深盘一票否决）机械误杀四大豪门冷平（010 勒沃库森 2:2、012 切尔西 2:2、016 利物浦 0:0、024 毕包 1:1）, 一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析, 三、 10 场漏网平局的三大系统级机械误杀归因 (+1 more)

### Community 12 - "**DISCUSSION**"
Cohesion: 0.17
Nodes (12): Broader Importance of Outcome Bias, Constraints on Generality, **DISCUSSION**, **EXTENSIONS**, Limitations and Future Directions, PDF 第 12 页, PDF 第 13 页, PDF 第 14 页 (+4 more)

### Community 13 - "刷新总对账看板"
Cohesion: 0.33
Nodes (8): 汇总复盘卡片的申报计数；不认证赛前封存、不修改经验或训练模型。, 刷新总对账看板(), 计数(), 读取卡片(), test_对账允许零胜率且不猜头号推荐(), test_空目录不除零(), test_错误计数不覆盖原看板(), write_card()

### Community 14 - "**METHOD**"
Cohesion: 0.22
Nodes (9): Comprehension Checks, Decision Quality, **MEASURES**, **METHOD**, **OUTCOME BIAS MANIPULATION**, **PARTICIPANTS**, PDF 第 5 页, PDF 第 6 页 (+1 more)

### Community 15 - "历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.25
Nodes (8): 历史待核查：1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误, 历史待核查：1. 赛前（T-2h）已知客观数据流水, 历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告, 历史待核查：2. 为什么会被模型一票否决漏网？（认知根因）, 历史待核查：2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡, 历史待核查：一、 主推失手深度剖析：为什么周五012与011会全军覆没？, 历史待核查：三、 闭环演化：两道物理级断路器系统升级（写入代码与大脑）, 历史待核查：二、 漏网盲区深度审计：【周五004 赫根 1:1 米亚尔比】

### Community 16 - "Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计"
Cohesion: 0.50
Nodes (4): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes

### Community 17 - "2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）"
Cohesion: 0.18
Nodes (10): 1. 周二001 亚冠精英 叻武里 vs 上海海港 (18:00 开球), 1. 周二009 荷甲 阿贾克斯 vs 威廉二世 [让球-2] (02:00), 1. 周二014 解放者杯 普拉滕斯 vs 弗鲁米嫩 (06:00), 2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）, 2. 周二002 亚冠精英 大田市民 vs 京都 (18:00 开球), 2. 周二007 西甲 巴列卡诺 vs 西班牙人 (01:00), 2. 周二013 西甲 埃尔切 vs 皇马 [让球+2] (03:30), ⭐ 一级核心：高平阻盘·正期望值（+EV）黄金标的（破除低赔执念） (+2 more)

### Community 18 - "Q: 系统规范README与智慧大脑AGENTS协同架构"
Cohesion: 0.50
Nodes (4): Answer, Outcome, Q: 系统规范README与智慧大脑AGENTS协同架构, Source Nodes

### Community 19 - "Shin与比例归一化：方法说明及适用边界"
Cohesion: 0.23
Nodes (12): 项目规则与数据口径审计, 比例归一化市场概率, Shin逆变换的平方与总和项, Shin潜在参数的解释边界, Shin与比例归一化：方法说明及适用边界, 历史待核查：2026-09-10_预测.md, 历史待核查：🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 历史待核查：2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版） (+4 more)

### Community 20 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 21 - "PDF 第 16 页"
Cohesion: 0.50
Nodes (4): **COPYRIGHT:**, PDF 第 16 页, **REFERENCES**, **TO CITE THIS ARTICLE:**

### Community 22 - "**4 Guidelines and best practices for forecast evaluation**"
Cohesion: 0.50
Nodes (4): **4.1.1 Fixed origin setup**, **4.1.2 Rolling origin, time series cross-validation and prequential evaluation setups**, **4.1 Data partitioning**, **4 Guidelines and best practices for forecast evaluation**

### Community 23 - "二、 核心败因深度解剖（四大低级错误）"
Cohesion: 0.22
Nodes (9): 1. 概率主客颠倒（把 30% 概率当成必然事件）, 2026-09-14（周一）中国体育彩票平局推演深度复盘报告, 2. 心电图神化与阴谋论脑补, 3. 刻舟求剑套用前日教训（过度拟合）, 4. 盲目博冷（都灵 0-2 罗马）, 5. 【全天最大罪证·周一007深度解剖】庄家关盘明牌开卷考的系统性漏网, 一、 战绩看板与客观结算, 三、 习惯塑形：六道物理拦截卡片 (+1 more)

### Community 24 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 25 - "PDF 第 14 页"
Cohesion: 0.67
Nodes (3): **3.2 Datasets for empirical evaluations**, **3.3 Evaluation measures for forecasting**, PDF 第 14 页

### Community 26 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 27 - "2023_Aiyer_结果偏见与决策评价.md"
Cohesion: 0.11
Nodes (18): **ADDITIONAL FILES**, **AUTHOR AFFILIATIONS**, **AUTHOR CONTRIBUTIONS**, **AUTHOR INFORMATION**, **BACKGROUND**, **CHOSEN STUDY FOR REPLICATION: BARON AND HERSHEY (1988)**, **CITATION OF THE TARGET RESEARCH ARTICLE**, **COMPETING INTERESTS** (+10 more)

### Community 39 - "赔率账本契约"
Cohesion: 0.12
Nodes (21): ABC, 回溯连续轨迹用例, 探测并记录心电图用例, DDD 应用层 - 业务用例编排 协调领域模型与契约端口，无任何具体数据库或 HTTP 请求实现细节, 业务用例：定时探测盘口，自动与上一时刻比对位移，发现异动报警并落库, 业务用例：对特定场次调取从初盘到终盘的全部时序数据并提炼态势, 回溯连续轨迹用例, 探测并记录心电图用例 (+13 more)

### Community 40 - "2026-09-14（周一）中国体育彩票精算推演报告"
Cohesion: 0.18
Nodes (11): 1. Capa 1 [ODDS] 盘口结构与心电图流水, 1. Capa 1 [ODDS] 盘口结构与心电图流水, 1. 为什么不再机械一票否决？（深盘放行法则）, 2026-09-14（周一）中国体育彩票精算推演报告, 2. Capa 3 & 4 [API] 攻防均衡与法乙平局温床, 2. Capa 5 & 7 [IND] 破除高比分平局误杀, 3. Capa 7 [IND] 比分与落点, 一、 【头号黄金猎物·均势低平】周一009 法乙 圣旺红星 vs 梅斯 (+3 more)

### Community 41 - "**ABSTRACT**"
Cohesion: 0.40
Nodes (5): **ABSTRACT**, **CORRESPONDING AUTHOR: Gilad Feldman**, **KEYWORDS:**, PDF 第 2 页, **TO CITE THIS ARTICLE:**

### Community 42 - "历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）"
Cohesion: 0.33
Nodes (6): 历史待核查：1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】, 历史待核查：2026-09-11 竞彩足球平局精算推演报告, 历史待核查：2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】, 历史待核查：3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】, 历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）, 历史待核查：二、 严格过筛：红线断路器执行记录

### Community 43 - "2026-09-09（周三）中国体彩平局全要素深度复盘报告"
Cohesion: 0.40
Nodes (5): 1. 🎯 【周三001 江原FC 1:1 全北现代】（赛果：平局 1:1 · 体彩平赔 2.92）, 2026-09-09（周三）中国体彩平局全要素深度复盘报告, 2. 🎯 【周三014 拉普拉塔大学 1:1 科林蒂安】（赛果：平局 1:1 · 体彩平赔 2.58）, 一、 两场命中平局全景精算复盘, 二、 五道硬红线 3.1 版排雷审计（9场分胜负全量排雷成功）

### Community 44 - "已取代：智慧复盘论文索引"
Cohesion: 0.40
Nodes (5): 已取代：保存与完整性, 已取代：原文与来源, 已取代：智慧复盘论文索引, 已取代：第二批：条件适应与连续评估, 已取代：面向本项目的应用建议（综合提炼，尚未验证改进效果）

### Community 45 - "本地账本仓储"
Cohesion: 0.14
Nodes (13): parametrize, test_不会跨周拼接同名场次(), test_不同市场与不同比赛禁止计算虚假位移(), test_伤停对抗率不直接判定赛果(), test_失球阈值不产生准入或否决(), test_拒绝非法十进制赔率(), test_旧账本迁移保持原赔率并识别让球(), test_让球快照入库回读不丢失市场() (+5 more)

### Community 46 - "赔率数值"
Cohesion: 0.13
Nodes (17): fixture, test_本地账本仓储保存并检索时序轨迹(), test_本地账本仓储查询空赛事安全返回空(), 临时数据库(), 断言强队胜赔<1.60时，若满足铁桶、多赛疲劳或高平阻盘，严禁机械枪毙，必须放行, test_客优于主且平赔下降只记录观测(), test_深盘冷平放行资格防003_006_012_022机械误杀(), test_热门主队平赔上升只记录观测() (+9 more)

### Community 47 - "体彩官方适配器"
Cohesion: 0.15
Nodes (11): Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes, test_体彩官方适配器在基础胜平负关闭时自动捕获让球盘(), test_体彩官方适配器安全过滤无赔率异常赛事(), test_体彩官方适配器解析原始数据为纯净领域快照(), 赔率快照 (+3 more)

### Community 48 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 49 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 51 - "超密集编织图谱"
Cohesion: 0.29
Nodes (6): test_图谱检查不写文件(), 深度联想连线机 (Deep Associative Weaver) ===================================== 负责在 535…, 纯 Python 标准库实现的广度优先搜索 (BFS) 图连通性算法, 深度语义编织执行引擎。 若传入自定义图谱路径且未显式指定是否落盘，则默认纯计算不写文件，保护测试隔离。, 计算连通分量与孤岛(), 超密集编织图谱()

### Community 52 - "二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？"
Cohesion: 0.50
Nodes (4): 2. 【周日006 海伦芬 0:0 特尔斯达】（平赔 4.55，冷门白卷）, 3. 【周日012 勒芒 2:2 朗斯】（平赔 4.15，对攻大冷平）, 4. 【周日022 法马利康 1:1 里斯本竞技】（平赔 4.30，豪门爆冷）, 二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？

### Community 54 - "Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey’s (1988) Outcome Bias Experiment 1"
Cohesion: 0.67
Nodes (3): **GILAD FELDMAN**, Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey’s (1988) Outcome Bias Experiment 1, PDF 第 1 页

## Ambiguous Edges - Review These
- `探测并记录心电图用例` → `体彩官方适配器`  [AMBIGUOUS]
  脚本/应用/用例.py · relation: legacy_unverified_relation
- `回溯连续轨迹用例` → `本地账本仓储`  [AMBIGUOUS]
  脚本/应用/用例.py · relation: legacy_unverified_relation
- `test_回溯连续轨迹用例提炼单边变盘态势()` → `KTH 2024 Betting Exchange Liquidity Study`  [AMBIGUOUS]
  脚本/测试/test_业务用例.py · relation: legacy_unverified_relation
- `test_微观球员适配器严格断言完场比分()` → `Overall Accuracy & Real-time Scoreboard`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py · relation: legacy_unverified_relation
- `test_微观球员适配器提取球员高阶链条数据()` → `PlayeRank Framework`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py · relation: legacy_unverified_relation
- `test_微观球员适配器提取球员高阶链条数据()` → `Success Score Metric`  [AMBIGUOUS]
  脚本/测试/test_微观球员接口.py · relation: legacy_unverified_relation
- `体彩官方适配器` → `Bookmakers' Consensus Probability`  [AMBIGUOUS]
  脚本/适配器/体彩接口.py · relation: legacy_unverified_relation
- `体彩官方适配器` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  脚本/适配器/体彩接口.py · relation: legacy_unverified_relation
- `体彩官方适配器` → `Constantinou Hybrid Bayesian Network Model`  [AMBIGUOUS]
  脚本/适配器/体彩接口.py · relation: legacy_unverified_relation
- `体彩官方适配器` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  脚本/适配器/体彩接口.py · relation: legacy_unverified_relation
- `微观球员适配器` → `PlayeRank Framework`  [AMBIGUOUS]
  脚本/适配器/微观球员接口.py · relation: legacy_unverified_relation
- `微观球员适配器` → `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study`  [AMBIGUOUS]
  脚本/适配器/微观球员接口.py · relation: legacy_unverified_relation
- `微观球员适配器` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  脚本/适配器/微观球员接口.py · relation: legacy_unverified_relation
- `微观球员适配器` → `Dynamic Seasonal Team Attack and Defence Effects`  [AMBIGUOUS]
  脚本/适配器/微观球员接口.py · relation: legacy_unverified_relation
- `微观球员适配器` → `Success Score Metric`  [AMBIGUOUS]
  脚本/适配器/微观球员接口.py · relation: legacy_unverified_relation
- `本地账本仓储` → `Betting Exchange Liquidity Dynamics`  [AMBIGUOUS]
  脚本/适配器/本地账本.py · relation: legacy_unverified_relation
- `本地账本仓储` → `KTH 2024 Betting Exchange Liquidity Study`  [AMBIGUOUS]
  脚本/适配器/本地账本.py · relation: legacy_unverified_relation
- `本地账本仓储` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `本地账本仓储` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  脚本/适配器/本地账本.py · relation: legacy_unverified_relation
- `.批量保存快照()` → `Betting Exchange Liquidity Dynamics`  [AMBIGUOUS]
  脚本/适配器/本地账本.py · relation: legacy_unverified_relation
- `赔率位移` → `Favourite-Longshot Bias (FLB)`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `赔率位移` → `KTH 2024 Betting Exchange Liquidity Study`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `.是否显著防守降水()` → `Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017)`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `赔率快照` → `Numerical Variant of Shin Conversion`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `校验让球明牌平局对冲资格()` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `校验攻防伤停平局资格()` → `PlayeRank Framework`  [AMBIGUOUS]
  脚本/领域/模型.py · relation: legacy_unverified_relation
- `2026-09-12_复盘.md` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md · relation: legacy_unverified_relation
- `2026-09-12_复盘.md` → `Overall Accuracy & Real-time Scoreboard`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md · relation: legacy_unverified_relation
- `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md · relation: legacy_unverified_relation
- `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `ELO-Odds Rating System`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `Odds-Only Equal Profitability Confidence (OO-EPC)`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `Mandadapu (2024) Football Match Outcome Forecasting Study`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `2026-09-13_预测.md` → `Hierarchical Bayesian Poisson Football Score Model`  [AMBIGUOUS]
  分析复盘记录/2026-09-13_预测.md · relation: legacy_unverified_relation
- `已取代：项目规则与数据口径审计` → `智慧复盘论文索引`  [AMBIGUOUS]
  温故而知新学习资料/README.md · relation: legacy_unverified_relation
- `已取代：项目规则与数据口径审计` → `智慧经验与习惯塑形`  [AMBIGUOUS]
  分析复盘记录/总复盘总结.md · relation: legacy_unverified_relation
- `已取代：项目规则与数据口径审计` → `足球概率分析系统手册`  [AMBIGUOUS]
  README.md · relation: legacy_unverified_relation
- `已取代：项目规则与数据口径审计` → `预测记录与智慧复盘契约`  [AMBIGUOUS]
  分析复盘记录/README.md · relation: legacy_unverified_relation
- `历史待核查：1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误` → `Skellam Distribution (Poisson-Difference)`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `历史待核查：二、 漏网盲区深度审计：【周五004 赫根 1:1 米亚尔比】` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `历史待核查：一、 唯一平局漏网盲区深度审计：【周四001 费内巴切 1:1 罗马】` → `Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017)`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `历史待核查：二、 周四007【德尔瓦耶 0:2 弗拉门戈】单挑失手深度复盘` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11_预测.md` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-06 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-07 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-08 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-09 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Hierarchical Bayesian Poisson Football Score Model` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `Beating the Bookies with Their Own Numbers (Kaunitz et al. 2017)` → `历史待核查：2026-09-09 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-06 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-07 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-08 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-08 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_复盘.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-09 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-06 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-07 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-08 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-09 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `Mandadapu (2024) Football Match Outcome Forecasting Study` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `ELO-Odds Rating System`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `Egidi Hierarchical Bayesian Poisson Model`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `Odds-Only Equal Profitability Confidence (OO-EPC)`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `历史待核查：2026-09-06 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Pre-Match Forecast` → `历史待核查：2026-09-07 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-06 Post-Match Review` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-06_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `ELO-Odds Rating System`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `Odds-Only Equal Profitability Confidence (OO-EPC)`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Pre-Match Forecast` → `历史待核查：2026-09-08 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-07 Post-Match Review` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-07_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Pre-Match Forecast` → `ELO-Odds Rating System`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Pre-Match Forecast` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Pre-Match Forecast` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Pre-Match Forecast` → `Odds-Only Equal Profitability Confidence (OO-EPC)`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Pre-Match Forecast` → `历史待核查：2026-09-09 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-08 Post-Match Review` → `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-08_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-09 Pre-Match Forecast` → `ELO-Odds Rating System`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-09 Pre-Match Forecast` → `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-09 Pre-Match Forecast` → `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-09 Pre-Match Forecast` → `Odds-Only Equal Profitability Confidence (OO-EPC)`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-09 Pre-Match Forecast` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-09_预测.md · relation: legacy_unverified_relation
- `Overall Accuracy & Real-time Scoreboard` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `Overall Accuracy & Real-time Scoreboard` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Clustered Probit Model` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `ELO-Odds Rating System` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `ELO-Odds Rating System` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `ELO-Odds Rating System` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `ELO-Odds Rating System` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `PlayeRank Framework` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `PlayeRank Framework` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `PlayeRank Framework` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `Asian Handicap (AH) Betting Market` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `Asian Handicap (AH) Betting Market` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `Asian Handicap (AH) Betting Market` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Asian Handicap (AH) Betting Market` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `Odds-Only Equal Profitability Confidence (OO-EPC)` → `历史待核查：2026-09-10 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `Odds-Only Equal Profitability Confidence (OO-EPC)` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `Odds-Only Equal Profitability Confidence (OO-EPC)` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Pre-Match Forecast` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Pre-Match Forecast` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Post-Match Review` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11 Pre-Match Forecast` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11 Pre-Match Forecast` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11 Post-Match Review` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation

## Knowledge Gaps
- **263 isolated node(s):** `Usage`, `What graphify is for`, `Step 0 - GitHub repos and multi-path merge (only if a URL or several paths)`, `Step 1 - Ensure graphify is installed`, `Step 2 - Detect files` (+258 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 318 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `探测并记录心电图用例` and `体彩官方适配器`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `回溯连续轨迹用例` and `本地账本仓储`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `test_回溯连续轨迹用例提炼单边变盘态势()` and `KTH 2024 Betting Exchange Liquidity Study`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `test_微观球员适配器严格断言完场比分()` and `Overall Accuracy & Real-time Scoreboard`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `test_微观球员适配器提取球员高阶链条数据()` and `PlayeRank Framework`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `test_微观球员适配器提取球员高阶链条数据()` and `Success Score Metric`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `体彩官方适配器` and `Bookmakers' Consensus Probability`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._