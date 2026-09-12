# AGENTS.md — 足球胜负平倍率精算与博弈推演大脑

> **大脑定位**：智能体认知与推演中枢。专攻中国体育彩票与全球预测市场胜负平量化博弈，以庄家利益最大化与全量实证数据为核心，驱动自进化飞轮。规范见 [系统使用手册 (README.md)](./README.md) 与 [分析复盘规程档案 (分析复盘记录/README.md)](./分析复盘记录/README.md)。

---

## 1. 核心博弈哲学与底层公理
1. **庄家必赚与通杀收割公理**：
   * 足球比赛本质是资本控盘局。90% 散户偏好投注“胜/负”，平局筹码通常不足 15%；
   * 平局是庄家消灭胜负两头巨量筹码、单场狂揽 50%~60% 净利润的终极武器；
   * 推演彻底抛弃主观竞技情怀，唯一聚焦于“庄家如何通过控盘杀多赔少实现利益最大化”。
2. **庄家明牌开卷考公理（体彩关闭基础胜平负即最高级内幕明示）**：
   * 当体彩官方故意关闭基础“胜平负”（had 为 None）仅开“让球盘”（hhad），且国际大庄平赔高达 8.00~10.00+ 时，是庄家切断极低水主胜、将 90%+ 散户资金赶入“让胜”的内幕风控明牌！
   * 终局最具杀伤力且赔付最小剧本是“逼平（1:1/0:0）”或“受让方小负”；
   * **双向狙击策略**：1) 国际/Polymarket 端以极小注码（1U）单挑 8~12 倍超级冷平（8~10¢）；2) 国内体彩端反向重注【让球平 + 让球负】（3.00~4.50）双平闭环对冲，收割全盘让胜韭菜！

---

## 2. 推演规范、四技能协同与全量数据协议
1. **赛前必读复盘与零孤岛保障**：
   * 分析推演前必须强制通读 [总复盘总结 (分析复盘记录/总复盘总结.md)](./分析复盘记录/总复盘总结.md)；
   * 强制全局开启 **Graphify 超级深度模式（--mode deep）**：赛前推演必须调用 `graphify query` 深度穿透历史盘口与学术拓扑，严禁产生孤岛节点，新建文档强制双向引用，Git 守卫（post-commit）自动维系连通分量=1、孤岛=0；
2. **四维技能强制协同协议（三大足球技能 + Graphify超级深度模式）**：
   * 每次推演与复盘必须 100% 强制联动四大技能，榨干全部数据维度并与论文库双向锚定：
   * `graphify`：超级深度模式（--mode deep）全景关联历史相似赔率、操盘手法、学术因果与赛后闭环；
   * `football-data`：全量赛程、积分榜、真实得失球均值、H2H 交锋史、ClubElo 动态战力与 Understat 空间单脚 xG 坐标；
   * `football-betting-analysis`：8 层博彩推演模型、去水隐含概率、全球四大机构盘口共识；
   * `football-match-analysis`：Elo 战力差距、泊松联合比分矩阵、三层爆冷判据（风格克制+状态变量+赛制红利）。
3. **关键球员微观主角硬核数据（物理硬闸门：无球员数据严禁出票）**：
   * 候选平局必须 100% 强制调用 API-Sports（`脚本/适配器/微观球员接口.py`）核验球员，未核验一票否决：
   * **伤停折损度**：核心进攻发动机缺阵削弱破门创造力；后腰防守屏障坍塌极易被打穿分胜负（一票否决）；
   * **终结转化与射正率**：两队锋线射门转化率 $\le 10\%$、射正率 $\le 35\%$ 时，严重加固 0:0/1:1 闷平基底；
   * **门将扑救与防线争顶对抗**：门将扑救率 $\ge 75\%$、中卫空中对抗胜率 $\ge 65\%$ 时，构成抵御绝杀的坚实护城河；
   * **赛程密集与体能透支**：休赛天数 $\le 3$ 天（双线周中作战）直接诱发下半场攻力衰竭、战术犯规飙升（切碎节奏助推保平打慢）。

---

## 3. 核心分析范式：8 层精算推演模型（8 Capas）
分析推演前必须先看【总复盘总结】，随后严格遵循 8 层流程并与顶刊文献双向锚定：
* **Capa 1 [ODDS] 市场底牌与机构对账**：中国体彩官方赔率 vs 国际四大（Pinnacle、Bet365、William Hill、Betfair）。调用 [Shin 算法专卷](温故而知新学习资料/Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) 反推内幕交易量 $z$ 与无抽水真实概率；应用 [EMH 纯赔率模型](温故而知新学习资料/2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) 与 [1710.02824 庄家共识策略](温故而知新学习资料/1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) 校正冷门与平局偏差；捕捉威廉希尔等老牌庄家平赔逆势压水实防（如低于平博 0.25+）。
* **Capa 2 [IND] 球队画像与战力评级**：主客场真实得失球均值、平局率与交锋历史，结合 [BORS 战力评级体系](温故而知新学习资料/2018_PLOS_Betting_Odds_Rating_System_BORS.md) 与 [1802.08848 历史攻防联合建模](温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md)。
* **Capa 3 [API] 球员微观画像**：基于 [2019 Nature PlayeRank 框架](温故而知新学习资料/2019_Nature_PlayeRank_Data_Driven_Framework.md) 与 [2025 Success Score 深度架构](温故而知新学习资料/2025_Success_Score_Deep_Learning_Football_Prediction.md) 评估球员进攻链参与度（xg_chain/xg_buildup）与攻防阵型克制。
* **Capa 4 [IND] 综合指标与泊松联合概率**：双参数 Poisson 与 Skellam 分布计算精确比分矩阵（0:0, 1:1, 2:2），依托 [分层贝叶斯泊松模型](温故而知新学习资料/1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) 与 [2017 平局预测难题修正](温故而知新学习资料/2017_Problem_of_Correctly_Predicting_Draws_Soccer.md) 膨胀校准平局。
* **Capa 5 [IND] 根因机制与心理战术博弈**：依据 [2008 散户情绪与庄家定价偏见](温故而知新学习资料/2008_Sentiment_and_Bookmaker_Pricing_Bias.md) 识别胜负两头筹码失衡；结合 [2025 战术犯规与平局预测](温故而知新学习资料/2025_Springer_Predicting_Draws_and_Fouls_Bayesian.md) 量化高频中场战术粗暴犯规对进攻节奏的切碎致平效果。
* **Capa 6 平局 3.0 六维加权决策模型**：实防意图(30%) + 白卷率(25%) + 中场犯规(20%) + 保分战意(15%) + 历史平局基因(10%)，总分 $\ge 75$ 候选，$\ge 85$ 黄金猎物（理论见 [2403.16282 机器学习演进](温故而知新学习资料/2403.16282_The_Evolution_of_Football_Betting_Machine_Learning.md) 与 [2024 KTH 盘口流动性](温故而知新学习资料/2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md)）。
* **Capa 7 赛前预测与置信度**：输出去水真实概率、期望值（EV）与置信度区间，严禁使用“稳赢”主观情绪词（理论见 [2505.21275 进球感知](温故而知新学习资料/2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md)）。
* **Capa 8 最终决策与避坑指南**：锁定最优落点剧本（单挑 1:1/0:0 或双平对冲），依据 [2003.09384 让球盘因果网络](温故而知新学习资料/2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md) 检验让球盘与标准盘套利空间。

---

## 4. 赛前七道金刚一票否决红线（物理断路器 3.1版）
赛前初筛逐条严密过筛，触犯任意一条立刻一票否决：
1. 🚫 **红线 1（拒绝真实倾斜深盘与假深盘纠偏）**：强队四大真实赔率 $< 1.60$ 一票否决。**【核心豁免】**：若强队临场胜赔被砸至 $\le 1.40$（诱主热度 $\ge 85\%$）、平赔反向推高至 $\ge 4.20$ 阻盘，且弱队单季客场失球 $\le 0.8$（顶级铁桶反击风格），严禁机械一刀切，强制启动【假深盘诱主·高平阻盘通杀】复核。
2. 🎭 **红线 2（辨别伪降水硬死锁与德比实防鉴别）**：客队水位显著低于主队（客队战力占优）时，平赔下降多为“诱平掩护客胜”，严禁盲目单挑平局；【同城德比豁免】：仅在双方属同城德比且中场绞杀严重、受让方保平韧性极强时，低平赔方可判定为机构真实避险。
3. 🪤 **红线 3（豪门高平阻盘客队防守硬指标）**：高平阻盘（平赔 $\ge 3.60$）仅适用于客队单季客场失球 $\le 0.8$ 的顶级铁桶队；防守漏风的普通客队（场均失球 $> 1.0$）严禁滥套阻盘模型。
4. 🔒 **红线 4（势均力敌必须小球前置锁）**：**仅对 $|主胜 - 客胜| \le 0.25$ 的均势盘生效**！若 Over 2.5 赔率 $< 1.75$，直接判定为大球对攻分胜负一票否决；水差 $> 0.25$ 的让球盘严禁误杀冷平。
5. 🧱 **红线 5（大比分对攻平局雷达）**：大球联赛中，0球赔率 $\ge 25.00$ 且平赔 $\ge 4.20$ 的对攻局，严禁仅看 0:0/1:1 闷平，必须结合反击与犯规数据，防范 2:2 / 3:3 大比分对攻平局收割。
6. 🏰 **红线 6（豪门客战高平阻盘防冷平收割）**：豪门客战水位在 $1.80 \sim 2.10$ 且平赔高挂 $\ge 3.50$ 时，散户蜂拥胜负两头；若主队防守坚韧且欧洲老牌庄家平赔逆势压低至 $\le 3.40$（低于平博 $\ge 0.25$），强制启动“高平阻盘通杀”复核防 1:1 冷平收割。
7. 🚨 **红线 7（庄家明牌开卷考·内幕避险雷达）**：体彩官方故意关闭普通胜平负仅开让球盘时，严禁视为无比赛跳过！庄家诱散户买让胜，终局以逼平或小负通杀。狙击策略：Polymarket 8~12 倍冷平 + 国内体彩【让球平 + 让球负】双平闭环对冲。


---

## 5. 临场 T-1h 动态盯盘与自进化闭环
1. ⏱️ **平赔防御警戒线**：核心平局猎物平赔需维持在 $\le 3.30$ 实防区间；若临场反常抬升突破 $> 3.40$（升幅 $> 0.20$），说明庄家已解除避险，强制下调或放弃平局。
2. 📉 **大小球盘口共振线**：大小球盘口进一步向小球倾斜（如 Under 2.5 跌破 1.65）按指数级加固 1:1/0:0 终场置信度。
3. 🏃 **首发攻防战术熔断**：赛前 1 小时首发名单公布后，若原本指望打防守的客队放弃后腰防线、排出全主力多前锋强攻对轰，平局风险剧增，触发熔断。
4. 🔄 **Karpathy 闭环进化机制**：
   * **1. 赛前推演 (Pre-Match)**：`graphify query` 检索历史操盘手法，8 层模型 + 7 道硬红线初筛；
   * **2. 物理封盘 (Lock-in T-2h)**：写入 `YYYY-MM-DD_预测.md` 文首 JSON 卡片，赔率心电图锁定即时流水；
   * **3. 赛后真实对账 (Reconcile)**：自动调用 `脚本/对账机.py` 物理刷新胜率与战绩看板；
   * **4. 赛前盲区审计 (Post-Mortem)**：严禁赛中叙事，100% 审计开赛前已知数据盲区，提炼新红线通过 `graphify reflect` 与 `save-result` 沉淀入知识图谱。

---

## 6. 认知大脑自身行数控制与防失真进化法则（元规则）
1. **严格物理行数红线（<= 130 行）**：本文件总行数无论如何迭代进化，绝对严禁超过 130 行！坚决剔除字符画框图、冗余空行与低密度套话，保持纯粹高密度指令形态。
2. **智慧与经验零丢失法则**：行数精炼仅砍除排版脂肪，绝不伤及认知骨肉；既有博弈公理、三大技能协同、球员微观四维闸门、8 层推演模型、7 道一票否决红线与顶刊学术超链接必须 100% 完整保留。新教训提炼以高信息密度原则增补，确保博弈推演绝对不失真。

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
