# AGENTS.md — 足球倍率精算与赛事预测项目工作指南

> **项目定位**：基于“数据为王 + 庄家倍率精算”的足球赛事量化分析与预测工作区。  
> **核心哲学**：只要有庄家在，任何足球比赛本质上都是有黑幕的资本局；庄家不可能亏，庄家是一定要赚钱的。彻底拒绝赌徒主观臆断与竞技情怀，以“庄家必赚、利益最大化”为唯一推演公理。

---

## 1. 核心架构与数据管道

### 1.1 官方赔率数据管道（体彩直连）
* **免密端点**：`https://webapi.sporttery.cn/gateway/uniform/football/getMatchCalculatorV1.qry?channel=c`
* **覆盖范围**：当日开售全部场次，涵盖胜平负(`had`)、让球(`hhad`)、总进球(`ttg`)、比分(`crs`)、半全场(`hafu`)。
* **时效性**：分钟级同步，带精确到秒的 `updateTime` 时间戳。

### 1.2 全球微观数据管道（API-Sports）
* **接口地址**：`https://v3.football.api-sports.io/`
* **双 Key 自动轮换**：
  * 主 Key：`832130dcfdadb0aac6af9e19300f74ec` (100次/天)
  * 备 Key：`d3ee3cb753c07c442d7d3fd16bb6dceb` (100次/天)
* **核心价值**：提取日职联(98)、韩职联(292)、挪超(103)等次级赛事的射门转化率、零封率与白卷率。

### 1.3 学术文献引擎（Microsoft MarkItDown）
* **调用方式**：`MarkItDown().convert("file.pdf").text_content`
* **作用**：自动将学术研究 PDF 转化为结构化 Markdown，供大模型精准读取公式与数据表。

---

## 2. 核心分析范式：8 层博彩推演模型（8 Capas）

任何赛事深度分析必须严格遵守 8 层标准流程，并与学术文献与实战复盘库双向锚定：
1. **Capa 1 [ODDS]**：市场底牌（反推无抽水概率，计算平赔、大小球盘口防范度）。理论支撑见 [1710.02824 庄家倍率策略](./温故而知新学习资料/1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md)、[Shin 算法专卷](./温故而知新学习资料/Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) 与 [2604.17194 赔率转化模型](./温故而知新学习资料/2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md)。
2. **Capa 2 [IND]**：球队画像（主客场真实得失球均值、平局率与交锋历史）。理论支撑见 [1802.08848 攻防联合建模](./温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) 与 [2018 BORS 战力评级](./温故而知新学习资料/2018_PLOS_Betting_Odds_Rating_System_BORS.md)。
3. **Capa 3 [API]**：微观主角（射正率、射门转化率、主力对抗胜率与门将扑救率）。理论支撑见 [2019 Nature PlayeRank 框架](./温故而知新学习资料/2019_Nature_PlayeRank_Data_Driven_Framework.md) 与 [2025 Success Score 深度架构](./温故而知新学习资料/2025_Success_Score_Deep_Learning_Football_Prediction.md)。
4. **Capa 4 [IND]**：综合指标（泊松分布联合概率计算，检验数据与盘面一致性）。理论支撑见 [1802.08848 分层贝叶斯泊松模型](./温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) 与 [2017 平局预测难题](./温故而知新学习资料/2017_Problem_of_Correctly_Predicting_Draws_Soccer.md)。
5. **Capa 5 [IND]**：根因机制（为什么打平/分胜负？揭示战术动机与保守保分心理）。理论支撑见 [2008 散户情绪与庄家定价偏见](./温故而知新学习资料/2008_Sentiment_and_Bookmaker_Pricing_Bias.md) 与 [2025 战术犯规与平局预测](./温故而知新学习资料/2025_Springer_Predicting_Draws_and_Fouls_Bayesian.md)。
6. **Capa 6**：信号权重（区分强信号、中信号与无效噪音）。理论支撑见 [2403.16282 机器学习预测演进](./温故而知新学习资料/2403.16282_The_Evolution_of_Football_Betting_Machine_Learning.md)。
7. **Capa 7**：赛前预测（严谨概率分布与置信度，严禁使用“稳赢”字眼）。理论支撑见 [2505.21275 滚球盘口进球感知](./温故而知新学习资料/2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md) 与 [2604.17194 冷门偏差模型](./温故而知新学习资料/2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md)。
8. **Capa 8**：最终决策（最具性价比落点剧本与严厉避坑指南）。理论支撑见 [2003.09384 让球盘因果网络](./温故而知新学习资料/2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md)。实战案例见 [分析复盘记录档案](./分析复盘记录/2026-09-06_周日体彩平局精算分析与复盘档案.md)。

---

## 3. 工作区目录资产规范

```
D:\100-工作\200-交易\足球预测\
├── AGENTS.md                                   # 本文件：智能体协同与项目全景指南
├── 分析复盘记录\                               # 每日实盘精算推演与赛后复盘追踪档案
│   └── 2026-09-06_周日体彩平局精算分析与复盘档案.md # 今日周日三场平局全景精算档案
└── 温故而知新学习资料\                          # 国际学术经典文献资料库（12篇 MarkItDown .md）
    ├── README_学习资料索引与经典论文导读.md      # 12篇文献导读索引与交叉拓扑
    ├── 1710.02824_Beating_the_Bookies...md      # 用庄家数据击败庄家(实盘验证神作)
    ├── 1802.08848_Combining_Historical...md     # 历史战绩与赔率联合贝叶斯泊松模型
    ├── 2003.09384_Asian_Handicap_Market...md    # 让球盘(亚盘)有效性检验与贝叶斯网络
    ├── 2008_Sentiment_and_Bookmaker...md        # 散户情绪与庄家定价偏见
    ├── 2017_Problem_of_Correctly_Predicting...md# 平局预测的世界难题
    ├── 2018_PLOS_Betting_Odds_Rating...md       # BORS 庄家赔率反向战力评级体系
    ├── 2019_Nature_PlayeRank_Data_Driven...md   # Nature PlayeRank 球员量化框架
    ├── 2025_Springer_Predicting_Draws...md      # 战术粗暴犯规与平局联合预测
    ├── 2025_Success_Score_Deep_Learning...md    # 深度学习球队与球员表现架构
    ├── 2403.16282_The_Evolution_of_Football...md# 足球博彩机器学习预测演进(2024最新综述)
    ├── 2505.21275_Do_Betting_Markets_Sense...md # 滚球赔率进球感知模型
    ├── 2604.17194_Forecast_Sports_Outcomes...md # 2026有效市场假说纯赔率模型
    └── Shin_1993_and_Strumbelj_2014_庄家赔率...md# Shin 破译内幕与去水算法专卷
```

---

## 4. 智能体行为守则
1. **庄家必赚公理（第一铁律）**：只要有庄家在，任何足球比赛本质上都是有黑幕的资本控盘局。庄家绝不可能亏，是一定要赚钱的。彻底摒弃竞技体育情怀与球星童话，一切预测推演必须以“庄家如何杀多赔少、实现利益最大化”为唯一核心底层逻辑。
2. **数据在先，结论在后**：严禁无数据凭空推测，每一次推演必须调取官方赔率与 API 真实进球/白卷率。
3. **强制使用 Graphify 复盘进化**：赛前分析必须基于 `graphify-out/` 图谱推理，赛后必须通过 `graphify save-result` 与 `graphify reflect` 将实际赛果与踩坑教训沉淀入知识库，形成自我进化闭环。
4. **零残留与极简主义**：不产生无用临时脚本，用完即清，保持环境极度整洁。
5. **盘口异动敏感**：紧盯“破3超低平赔（<3.00）”与“0球超低赔率（<9.00）”的庄家避险与割韭菜异动。

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
