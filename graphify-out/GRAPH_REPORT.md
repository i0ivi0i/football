# Graph Report - 足球预测  (2026-09-17)

## Corpus Check
- 48 files · ~1,329,422 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 437 nodes · 677 edges · 36 communities (25 shown, 11 thin omitted)
- Extraction: 77% EXTRACTED · 9% INFERRED · 14% AMBIGUOUS · INFERRED: 60 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `768b8663`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？
- 足球概率分析现行规程
- Wheatcroft 论文 Markdown（附公式与图表）
- 历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告
- **Forecast evaluation for data scientists: common pitfalls and best practices**
- 历史待核查：2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）
- Sentiment Bias in Betting Odds
- 足球概率预测评分比较（Wheatcroft，2019预印本）
- 2026-09-13（周日）中国体育彩票精算推演报告
- **DISCUSSION**
- **RESULTS**
- 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告
- 2026-09-16（周三）中国体育彩票量化推演与 Polymarket 纯平局交易指南
- 历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告
- 2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）
- 2026-09-14（周一）中国体育彩票精算推演报告
- **4 Guidelines and best practices for forecast evaluation**
- 二、 核心败因深度解剖（四大低级错误）
- PDF 第 14 页
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
- Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study
- 历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）
- 2026-09-09（周三）中国体彩平局全要素深度复盘报告
- 已取代：智慧复盘论文索引
- 2026-09-15（周二）中国体彩平局阶段复盘与 004 漏网审计报告

## God Nodes (most connected - your core abstractions)
1. `**Forecast evaluation for data scientists: common pitfalls and best practices**` - 52 edges
2. `足球概率分析现行规程` - 47 edges
3. `智慧经验与习惯塑形` - 36 edges
4. `Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study` - 19 edges
5. `Sentiment Bias in Betting Odds` - 19 edges
6. `智慧复盘论文索引` - 18 edges
7. `Overall Accuracy & Real-time Scoreboard` - 18 edges
8. `PlayeRank Framework` - 18 edges
9. `Hierarchical Bayesian Poisson Football Score Model` - 17 edges
10. `已取代：智慧复盘论文索引` - 16 edges

## Surprising Connections (you probably didn't know these)
- `历史待核查：1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误` --legacy_unverified_relation--> `Skellam Distribution (Poisson-Difference)`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md → 温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md
- `历史待核查：2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡` --legacy_unverified_relation--> `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md → 温故而知新学习资料/2019_Nature_PlayeRank_Data_Driven_Framework.md
- `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` --legacy_unverified_relation--> `Sentiment Bias in Betting Odds`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md → 温故而知新学习资料/2008_Sentiment_and_Bookmaker_Pricing_Bias.md
- `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` --legacy_unverified_relation--> `PlayeRank Framework`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_复盘.md → 温故而知新学习资料/2019_Nature_PlayeRank_Data_Driven_Framework.md
- `历史待核查：二、 漏网盲区深度审计：【周五004 赫根 1:1 米亚尔比】` --legacy_unverified_relation--> `Asian Handicap (AH) Betting Market`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md → 温故而知新学习资料/2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md

## Hyperedges (group relationships)
- **Daily Actuarial Deduction and Audit Cycle** — rec_20260908_forecast, rec_20260908_review, rec_20260909_forecast [EXTRACTED 0.95]
- **Soccer ELO Rating System Hierarchy** — 2018_plos_elo_odds, 2018_plos_elo_goals, 2018_plos_elo_result [EXTRACTED 0.95]
- **Reverse Odds to Probability Conversion Methods** — goto2026_oo_epc, wenguerzhixin_xuexiziliao_2604_17194_numerical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_analytical_shin_conversion, wenguerzhixin_xuexiziliao_2604_17194_power_conversion [EXTRACTED 0.95]
- **Football Match Outcome Modelling Paradigms** — 温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_draw_prediction_evaluation, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_dnn_model, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_bookmaker_odds_model [INFERRED 0.85]
- **Betting Market Aggregate Information Framework** — 1710_02824_consensus_probability, 2018_plos_elo_odds, 2008_sentiment_sentiment_bias [INFERRED 0.85]
- **Soccer Match Outcome Forecasting Frameworks** — egidi_hierarchical_poisson_model, constantinou_hybrid_bn_model, ordered_logit_regression, multinomial_logit_regression [INFERRED 0.85]

## Communities (36 total, 11 thin omitted)

### Community 0 - "二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？"
Cohesion: 0.25
Nodes (8): 1. 【周日003 塞尔塔 1:1 马拉加】（平赔 3.50）, 2026-09-13（周日）中国体彩平局全要素深度复盘与 5 场漏网盲区审计报告, 2. 【周日006 海伦芬 0:0 特尔斯达】（平赔 4.55，冷门白卷）, 3. 【周日012 勒芒 2:2 朗斯】（平赔 4.15，对攻大冷平）, 4. 【周日022 法马利康 1:1 里斯本竞技】（平赔 4.30，豪门爆冷）, 一、 为什么【周日001 东京绿茵 1:1 千叶市原】被核心主推遗漏？, 三、 乔布斯产品思维的物理重构方案, 二、 为什么 003 / 006 / 012 / 022 四场平局全被一网打尽式遗漏？

### Community 1 - "足球概率分析现行规程"
Cohesion: 0.06
Nodes (65): Choe与Ramdas：序贯预测者比较, Dimitriadis等：CORP稳定可靠性图, Giacomini与White：条件预测能力检验, Macrì-Demartino等：动态历史信息借用, 智慧复盘论文索引, 论文的方法角色与迁移边界, 反例、适用范围与失效条件, 习惯塑形 (+57 more)

### Community 2 - "Wheatcroft 论文 Markdown（附公式与图表）"
Cohesion: 0.10
Nodes (17): Answer, Outcome, Q: 周一001卡利亚里1:0与周一006乌迪内斯1:2失手复盘与赛前盲区审计, Source Nodes, Answer, Outcome, Q: 体彩官方数据管道与API-Sports微观数据管道在赛前推演中的协同机制, Source Nodes (+9 more)

### Community 3 - "历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.20
Nodes (10): 历史待核查：1. 赛前（T-2h）已知客观数据流水, 历史待核查：1. 赛前已知数据与操盘陷阱, 历史待核查：2026-09-10（周四）中国体彩平局全要素深度复盘与盲区审计报告, 历史待核查：2. 为什么会被模型错误一票否决？（三大认知根因剖析）, 历史待核查：一、 唯一平局漏网盲区深度审计：【周四001 费内巴切 1:1 罗马】, 历史待核查：三、 经验物理固化与飞轮升级成果, 历史待核查：二、 周四007【德尔瓦耶 0:2 弗拉门戈】单挑失手深度复盘, 历史待核查：根因一：机械教条主义滥用【红线 4】（前置条件校验严重缺失） (+2 more)

### Community 4 - "**Forecast evaluation for data scientists: common pitfalls and best practices**"
Cohesion: 0.05
Nodes (39): **1 Introduction**, **2 Terminology of forecast evaluation**, **5 Conclusions**, **Abstract**, **Forecast evaluation for data scientists: common pitfalls and best practices**, PDF 第 10 页, PDF 第 11 页, PDF 第 13 页 (+31 more)

### Community 5 - "历史待核查：2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）"
Cohesion: 0.50
Nodes (4): 历史待核查：🥇 1. 【周四007 解放者杯】德尔瓦耶独立 vs 弗拉门戈（今日唯一黄金王牌 · 评分 94.0）, 历史待核查：2026-09-10（周四）中国体彩平局赛前精算推演报告（3.1 硬红线全量过筛版）, 历史待核查：一、 今日黄金猎物精选榜单, 历史待核查：二、 今日一票否决淘汰场次（全部触犯 3.1 版硬红线）

### Community 6 - "Sentiment Bias in Betting Odds"
Cohesion: 0.09
Nodes (32): Consensus Odds-Based Betting Strategy, Bookmaker Account Limiting / Discriminatory Practices, Bookmakers' Consensus Probability, Paper Trading Validation, Clustered Probit Model, DIFFATTEND Proxy, Sentiment Bias in Betting Odds, Betting Exchange Liquidity Dynamics (+24 more)

### Community 7 - "足球概率预测评分比较（Wheatcroft，2019预印本）"
Cohesion: 0.12
Nodes (17): Ignorance 对数评分, 足球概率预测评分比较（Wheatcroft，2019预印本）, 概率预测评分, RPS 排序距离假设, 决策质量与赛果分离审查, 结果偏见, 结果偏见与决策质量评价（Aiyer 等，2023）, 预注册重复实验 (+9 more)

### Community 8 - "2026-09-13（周日）中国体育彩票精算推演报告"
Cohesion: 0.12
Nodes (16): 1. Capa 1 [ODDS] 市场底牌与心电图轨迹, 1. Capa 1 [ODDS] 盘口结构, 1. Capa 1 [ODDS] 盘口结构, 1. 乔布斯灵活思维解构（破除红线2死板一刀切）, 1. 盘口与战术特征, 2026-09-13（周日）中国体育彩票精算推演报告, 2. Capa 3 [API] 微观防守护城河核验, 2. Capa 4 & 7 泊松落点 (+8 more)

### Community 9 - "**DISCUSSION**"
Cohesion: 0.17
Nodes (12): Broader Importance of Outcome Bias, Constraints on Generality, **DISCUSSION**, **EXTENSIONS**, Limitations and Future Directions, PDF 第 12 页, PDF 第 13 页, PDF 第 14 页 (+4 more)

### Community 10 - "**RESULTS**"
Cohesion: 0.13
Nodes (15): **CONFIRMATORY (PRE-REGISTERED) RESULTS** Replication: Decision Quality, **EXPLORATORY RESULTS (NOT PREREGISTERED)**, **EXTENSIONS**, Mediation Analyses, PDF 第 10 页, PDF 第 11 页, PDF 第 7 页, PDF 第 8 页 (+7 more)

### Community 11 - "2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.15
Nodes (12): 1. 红线 2（伪降水死锁）机械误杀三大豪门客平局（018 摩纳哥 1:1、020 米兰 2:2、028 里昂 0:0）, 1. 赛前已知特征与当时推演假设, 1. 赛前推演与当时假设, 2026-09-12（周六）中国体彩平局全要素深度复盘与盲区审计报告, 2. 真实赛况与血淋淋认知盲区, 2. 真实赛果与 `football-match-analysis` 硬核量化复盘, 2. 红线 4（均势大球前置锁）机械误杀两场对攻大球平局（013 伯恩茅斯 2:2、023 科隆 1:1）, 3. 红线 1（强队深盘一票否决）机械误杀四大豪门冷平（010 勒沃库森 2:2、012 切尔西 2:2、016 利物浦 0:0、024 毕包 1:1） (+4 more)

### Community 12 - "2026-09-16（周三）中国体育彩票量化推演与 Polymarket 纯平局交易指南"
Cohesion: 0.40
Nodes (5): 1. 【周三005 西甲】拉科鲁尼亚 vs 塞维利亚 (01:00 开球), 2026-09-16（周三）中国体育彩票量化推演与 Polymarket 纯平局交易指南, 2. 【周三014 西甲】莱万特 vs 毕尔巴鄂竞技 (03:30 开球), 一、 核心真平局深度八层推演（Polymarket 纯平局直达）, 二、 实力断崖与虚假彩票陷阱审查（坚决一票否决）

### Community 15 - "历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告"
Cohesion: 0.25
Nodes (8): 历史待核查：1. 【周五012 科里蒂巴 1:3 巴拉纳竞技】—— 触犯自身红线 2 的致命“伪降水”失误, 历史待核查：1. 赛前（T-2h）已知客观数据流水, 历史待核查：2026-09-11（周五）中国体彩平局全要素深度复盘与盲区审计报告, 历史待核查：2. 为什么会被模型一票否决漏网？（认知根因）, 历史待核查：2. 【周五011 塞维利亚 1:0 巴伦西亚】—— 进球前置锁正确但终结能力严重失衡, 历史待核查：一、 主推失手深度剖析：为什么周五012与011会全军覆没？, 历史待核查：三、 闭环演化：两道物理级断路器系统升级（写入代码与大脑）, 历史待核查：二、 漏网盲区深度审计：【周五004 赫根 1:1 米亚尔比】

### Community 17 - "2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）"
Cohesion: 0.20
Nodes (10): 1. 周二001 亚冠精英 叻武里 vs 上海海港 (18:00 开球), 1. 周二009 荷甲 阿贾克斯 vs 威廉二世 [让球-2] (02:00), 1. 周二014 解放者杯 普拉滕斯 vs 弗鲁米嫩 (06:00), 2026-09-15（周二）中国体育彩票量化推演报告（纠偏重构版）, 2. 周二002 亚冠精英 大田市民 vs 京都 (18:00 开球), 2. 周二007 西甲 巴列卡诺 vs 西班牙人 (01:00), 2. 周二013 西甲 埃尔切 vs 皇马 [让球+2] (03:30), ⭐ 一级核心：高平阻盘·正期望值（+EV）黄金标的（破除低赔执念） (+2 more)

### Community 19 - "2026-09-14（周一）中国体育彩票精算推演报告"
Cohesion: 0.18
Nodes (11): 1. Capa 1 [ODDS] 盘口结构与心电图流水, 1. Capa 1 [ODDS] 盘口结构与心电图流水, 1. 为什么不再机械一票否决？（深盘放行法则）, 2026-09-14（周一）中国体育彩票精算推演报告, 2. Capa 3 & 4 [API] 攻防均衡与法乙平局温床, 2. Capa 5 & 7 [IND] 破除高比分平局误杀, 3. Capa 7 [IND] 比分与落点, 一、 【头号黄金猎物·均势低平】周一009 法乙 圣旺红星 vs 梅斯 (+3 more)

### Community 22 - "**4 Guidelines and best practices for forecast evaluation**"
Cohesion: 0.50
Nodes (4): **4.1.1 Fixed origin setup**, **4.1.2 Rolling origin, time series cross-validation and prequential evaluation setups**, **4.1 Data partitioning**, **4 Guidelines and best practices for forecast evaluation**

### Community 23 - "二、 核心败因深度解剖（四大低级错误）"
Cohesion: 0.22
Nodes (9): 1. 概率主客颠倒（把 30% 概率当成必然事件）, 2026-09-14（周一）中国体育彩票平局推演深度复盘报告, 2. 心电图神化与阴谋论脑补, 3. 刻舟求剑套用前日教训（过度拟合）, 4. 盲目博冷（都灵 0-2 罗马）, 5. 【全天最大罪证·周一007深度解剖】庄家关盘明牌开卷考的系统性漏网, 一、 战绩看板与客观结算, 三、 习惯塑形：六道物理拦截卡片 (+1 more)

### Community 25 - "PDF 第 14 页"
Cohesion: 0.67
Nodes (3): **3.2 Datasets for empirical evaluations**, **3.3 Evaluation measures for forecasting**, PDF 第 14 页

### Community 27 - "2023_Aiyer_结果偏见与决策评价.md"
Cohesion: 0.04
Nodes (45): 1. 刻舟求剑交锋谬误（古代数据的虚假安全感）, 2026-09-16（周三）中国体育彩票量化推演复盘与 0 命中根因审计, 2. 违背“允许空仓”原则的强行凑单（无米硬炊）, 3. 突发红牌的结构性破坏, 一、 赛果客观实盘对账表, 二、 深度复盘：为什么会 0 命中？犯了什么谬误？, **ABSTRACT**, **ADDITIONAL FILES** (+37 more)

### Community 40 - "Pérez-Blanco & Salmerón (2025) Bayesian Classifier Study"
Cohesion: 0.13
Nodes (33): ELO-Goals Rating System, ELO-Odds Rating System, ELO-Result Rating System, Informational Loss Metric, Passing Network Centrality, PlayeRank Framework, Wyscout Spatio-Temporal Match Events Dataset, Constantinou Hybrid Bayesian Network Model (+25 more)

### Community 42 - "历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）"
Cohesion: 0.33
Nodes (6): 历史待核查：1. 周五012 巴甲：科里蒂巴 vs 巴拉纳竞技【黄金第一猎物 ⬆️】, 历史待核查：2026-09-11 竞彩足球平局精算推演报告, 历史待核查：2. 周五011 西甲：塞维利亚 vs 巴伦西亚【黄金第二猎物】, 历史待核查：3. 周五008 意甲：威尼斯 vs 佛罗伦萨【第二梯队对冲观察】, 历史待核查：一、 核心黄金猎物精算剖析（结合 20:52 实时心电图变盘审计）, 历史待核查：二、 严格过筛：红线断路器执行记录

### Community 43 - "2026-09-09（周三）中国体彩平局全要素深度复盘报告"
Cohesion: 0.40
Nodes (5): 1. 🎯 【周三001 江原FC 1:1 全北现代】（赛果：平局 1:1 · 体彩平赔 2.92）, 2026-09-09（周三）中国体彩平局全要素深度复盘报告, 2. 🎯 【周三014 拉普拉塔大学 1:1 科林蒂安】（赛果：平局 1:1 · 体彩平赔 2.58）, 一、 两场命中平局全景精算复盘, 二、 五道硬红线 3.1 版排雷审计（9场分胜负全量排雷成功）

### Community 44 - "已取代：智慧复盘论文索引"
Cohesion: 0.40
Nodes (5): 已取代：保存与完整性, 已取代：原文与来源, 已取代：智慧复盘论文索引, 已取代：第二批：条件适应与连续评估, 已取代：面向本项目的应用建议（综合提炼，尚未验证改进效果）

### Community 58 - "2026-09-15（周二）中国体彩平局阶段复盘与 004 漏网审计报告"
Cohesion: 0.29
Nodes (7): 1. 【周二004 柔佛 1:1 布里兰】4.00 倍黄金冷平为何漏网？, 2026-09-15（周二）中国体彩平局阶段复盘与 004 漏网审计报告, 2. 【周二001 叻武里 4:6 上海上港】为何打成惨案？, 3. 【周二002 大田市民 1:0 京都不死鸟】为何 78 分钟被绝杀？, 一、 傍晚早场战绩看板与客观结算, 三、 系统级防漏网工程修复落地, 二、 核心败因与 004 漏网深度解剖（八大论文穿透）

## Ambiguous Edges - Review These
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
- `历史待核查：2026-09-11_预测.md` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
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
- `Clustered Probit Model` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_复盘.md · relation: legacy_unverified_relation
- `Sentiment Bias in Betting Odds` → `历史待核查：2026-09-12 Pre-Match Forecast`  [AMBIGUOUS]
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
- `历史待核查：2026-09-12 Pre-Match Forecast` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-12_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-12 Pre-Match Forecast` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Pre-Match Forecast` → `历史待核查：2026-09-10 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Pre-Match Forecast` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_预测.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-10 Post-Match Review` → `历史待核查：2026-09-11 Pre-Match Forecast`  [AMBIGUOUS]
  分析复盘记录/2026-09-10_复盘.md · relation: legacy_unverified_relation
- `历史待核查：2026-09-11 Pre-Match Forecast` → `历史待核查：2026-09-11 Post-Match Review`  [AMBIGUOUS]
  分析复盘记录/2026-09-11_预测.md · relation: legacy_unverified_relation

## Knowledge Gaps
- **247 isolated node(s):** `Answer`, `Outcome`, `Source Nodes`, `Answer`, `Outcome` (+242 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 260 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `2026-09-12_复盘.md` and `Sentiment Bias in Betting Odds`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `2026-09-12_复盘.md` and `Overall Accuracy & Real-time Scoreboard`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` and `Sentiment Bias in Betting Odds`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `一、 头号猎物【周六017 奥萨苏纳 0:2 西班牙人】崩盘根因深度剖析` and `PlayeRank Framework`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `2026-09-13_预测.md` and `ELO-Odds Rating System`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `2026-09-13_预测.md` and `PlayeRank Framework`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._
- **What is the exact relationship between `2026-09-13_预测.md` and `Asian Handicap (AH) Betting Market`?**
  _Edge tagged AMBIGUOUS (relation: legacy_unverified_relation) - confidence is low._