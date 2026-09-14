# 温故而知新：论文与方法资料库

唯一资料入口：[智慧复盘论文](#review-papers) · [原有资料导航](#classic-papers) · [阅读与迁移边界](#reading-boundaries)。
应用入口：[项目规程](../AGENTS.md) · [复盘流程与整改依据](../分析复盘记录/README.md) · [经验与习惯塑形](../分析复盘记录/总复盘总结.md)。

资料类型含期刊论文、预印本、学位论文和项目笔记；原有目录的更新时间为2026-09-06，后续版本与校验日期以各节记录为准。
本页合并原有两份资料索引；保留八篇智慧复盘论文的PDF/Markdown、239页版本信息、转换校验限制及原有15条资料导航。引用关系用于检索，不证明项目策略有效。

<a id="review-papers"></a>
## 智慧复盘：足球预测评估与决策学习论文

入口：[原有资料导航](#classic-papers) · 应用位置：[总复盘总结](../分析复盘记录/总复盘总结.md) · [分析复盘规程](../分析复盘记录/README.md)。这些关联表示研究方法可用于审查现有流程，不表示论文支持现有全部盘口假设。

## 原文与来源

| 论文 | 本地文件与版本 | 一手来源及下载来源 | 阅读重点与适用边界 |
| --- | --- | --- | --- |
| Sascha Wilkens, *Can simple models predict football — and beat the odds? Lessons from the German Bundesliga* (2026) | [Markdown，18 页](./2026_Wilkens_德甲预测与滚动验证.md) · [原始 PDF](./wilkens-2026-can-simple-models-predict-football-and-beat-the-odds-lessons-from-the-german-bundesliga.pdf)（主人手动下载） | [期刊与 DOI](https://doi.org/10.1177/22150218261416681) · [原 PDF](https://journals.sagepub.com/doi/pdf/10.1177/22150218261416681) | 概率校准、按赛季滚动样本外检验、按投注类型评估。该研究结果受联赛、时期、赔率和模拟条件限制，不能视作本项目盈利证明。 |
| Edward Wheatcroft, *Evaluating probabilistic forecasts of football matches: The case against the Ranked Probability Score* (2019 预印本) | [Markdown，29 页](./2019_Wheatcroft_足球概率预测评分.md) · [原始 PDF](./2019_Wheatcroft_足球概率预测评分.pdf)；arXiv 版本 | [arXiv:1908.08980](https://arxiv.org/abs/1908.08980) · [下载地址](https://arxiv.org/pdf/1908.08980) · [后续期刊 DOI](https://doi.org/10.1515/jqas-2019-0089) | 比较 RPS、Brier 与 ignorance/log score；仿真中 ignorance 更优，不表示一个评分指标能涵盖全部预测与投资目标。 |
| Sriraj Aiyer 等, *Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey’s (1988) Outcome Bias Experiment 1* (2023) | [Markdown，16 页](./2023_Aiyer_结果偏见与决策评价.md) · [原始 PDF](./2023_Aiyer_结果偏见与决策评价.pdf) | [期刊 DOI](https://doi.org/10.5334/irsp.751) · [PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12372742/) · [PDF 镜像](https://pdfs.semanticscholar.org/4370/9ac96fe810b5bc1aa687571f3d78574f591d.pdf) | 692 名参与者的医疗决策情境实验复现结果偏见。向足球复盘迁移属于方法建议，不能将其说成足球投注实验。 |
| Hansika Hewamalage、Klaus Ackermann、Christoph Bergmeir, *Forecast evaluation for data scientists: common pitfalls and best practices* (2023 卷期，2022 在线发表) | [Markdown，45 页](./2023_Hewamalage_预测评估陷阱与最佳实践.md) · [原始 PDF](./2023_Hewamalage_预测评估陷阱与最佳实践.pdf) | [期刊 DOI](https://doi.org/10.1007/s10618-022-00894-5) · [下载地址](https://link.springer.com/content/pdf/10.1007/s10618-022-00894-5.pdf) | 数据划分、信息泄漏、基准、误差指标和统计检验。主要讨论时间序列点预测；足球分类任务需要另选概率评分指标。 |

## 第二批：条件适应与连续评估

| 论文 | 本地文件与实际版本 | 一手来源 | 可复用方法与边界 |
| --- | --- | --- | --- |
| Macrì-Demartino、Egidi、Torelli, *Bayesian weighted discrete-time dynamic models for association football prediction* | [Markdown，26 页](./2025_Macri_足球贝叶斯加权动态模型_arXiv.md) · [PDF](./2025_Macri_足球贝叶斯加权动态模型_arXiv.pdf)。保存的是 2025 年 arXiv v1 作者预印本，非 2026 年期刊排版版。 | [arXiv:2508.05891v1](https://arxiv.org/abs/2508.05891v1) · [2026 年期刊 DOI](https://doi.org/10.1093/jrsssc/qlag032) | 随球队攻防变化自适应借用历史信息。可用于研究何时降低旧经验权重；作者比较的联赛、模型和时段有限，不表示任何变动都应重置规则。 |
| Giacomini & White, *Tests of Conditional Predictive Ability* (2006) | [Markdown，34 页](./2006_Giacomini_条件预测能力检验.md) · [PDF](./2006_Giacomini_条件预测能力检验.pdf)。Econometrica 74(6), 1545–1578，高校课程站保存的期刊版。 | [期刊 DOI](https://doi.org/10.1111/j.1468-0262.2006.00718.x) · [高校 PDF](https://economia.uc3m.es/jgonzalo/teaching/PhdTimeSeries/GiacominiWhite.pdf) | 条件预测能力与估计不确定性。可预先定义场景并检验新旧预测方法的差异；原检验有估计窗口、矩条件等适用要求，不是赛后任意切分样本的依据。 |
| Choe & Ramdas, *Comparing Sequential Forecasters* | [Markdown，61 页，含附录](./2023_Choe_序贯预测者比较_arXiv_v6.md) · [PDF](./2023_Choe_序贯预测者比较_arXiv_v6.pdf)。arXiv v6 于 2023-11-09 提交，PDF 标题页日期为 11 月 10 日；期刊 2023 年在线发表、2024 年卷期。 | [作者 arXiv v6](https://arxiv.org/abs/2110.00115v6) · [期刊 DOI](https://doi.org/10.1287/opre.2021.0792) | 用置信序列持续比较预测评分差异，减少反复查看结果造成的误判。主要结果适用于有界评分，论文另讨论无界评分；实证为棒球与天气，迁移足球需核验设定。 |
| Dimitriadis、Gneiting、Jordan, *Stable reliability diagrams for probabilistic classifiers* (2021) | [Markdown，10 页](./2021_Dimitriadis_稳定可靠性图_CORP.md) · [PDF](./2021_Dimitriadis_稳定可靠性图_CORP.pdf)。PNAS 正文，未包含另外发布的 SI Appendix。 | [PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC7923594/) · [作者机构库 PDF](https://publikationen.bibliothek.kit.edu/1000130510/106591216) · [期刊 DOI](https://doi.org/10.1073/pnas.2016191118) | CORP 稳定可靠性图、校准诊断与评分分解。可分别检查胜/平/负事件的概率；不应直接把二元分析当成完整三分类联合校准，时间相关性也需处理。 |

第二批处理与校验（2026-09-14）：

- 四份 PDF 和四份完整逐页 Markdown，共 131 页；加上首批为八篇、239 页。保留各文献实际版本、英文正文、参考文献和所下载 PDF 中的附录，未翻译或摘要化。
- 使用 PyMuPDF4LLM 1.28.2 提取布局，保存 279 张图形、公式、表格和整页校对图，其中 22 个表格区域另附原貌。移动 Markdown 时请一并携带 `论文配图/`。
- 两篇 arXiv 文献从相同版本的官方 HTML 提取 138 个原始 LaTeX 公式块：114 个按编号对应到 PDF 公式原图旁，24 个因无编号或布局差异放入明确标注的转换附录；另对照 PDF 转写 CORP 的 5 个公式与 Giacomini 的 2 个核心假设公式。编号映射及排版经过抽检，未逐符人工校对全部作者 HTML 公式。
- **数学完整性边界**：Giacomini 的 25 页、Choe 的 28 页及 CORP 的 3 页含无法直接解码的行内数学符号，已标明「⟦未识别符号⟧」并附整页原图。其余公式和复杂表格保留原貌，不声称纯文字完全无损；纯文字 AI 无法独立读取这些图片。涉及证明或精确计算时必须核对原图/PDF。
- 校验包括标题与作者、逐页非空、全部页码锚点、配图及本地链接、转换前后 PDF 的 SHA-256；抽查了开头正文、双栏布局、公式编号对应及表格。没有修改已有四篇正文、分析规程或全局记忆。
- 下载差异：足球动态模型的期刊/机构库入口受访问验证限制，采用作者公开预印本；Choe 采用可公开下载且包含附录的作者 v6。上述替代均在文首明确说明。

## 面向本项目的应用建议（综合提炼，尚未验证改进效果）

1. **先审判断，再看结果**：复盘时先读取封存的赛前数据、概率和理由，再揭示赛果；赢球和失手均纳入。这样减少结果偏见，不把赛后新增信息混作赛前可用依据。并非忽略结果，而是将过程审查与结果统计分开。
2. **以成组概率评估校准**：记录胜/平/负完整概率；比较累计 Brier、log loss 与市场去水概率基准。预测平局概率 30% 的单场不平，不足以判定模型失效；同类预测的实际频率和不确定性才提供校准证据。小样本分组只能提出问题。
3. **分层修正条件，不从个案写永久禁令**：事先定义有业务理由的联赛、实力差、赔率区间等分组，记录样本数与反例；按赛果反复切分容易找到偶然规律。数据错误可立即修正，统计模式先保持为假设。
4. **新旧规则接受未来检验**：冻结改动，在后续未用于改规则的比赛上并行记录新旧结果；同时记录避免的错误和误杀的机会。把命中率、概率质量、收益、成本及回撤分开评价，不能只挑有利指标。
5. **习惯塑形记录**：触发情境 → 检查动作 → 可核查证据与反例 → 暂定调整 → 后续反馈与验证 → 失效条件。明确何时暂不修改；失败可能涉及信息遗漏、概率失准或随机波动，不能仅凭最终比分确认原因。

## 保存与完整性

- 首批收录与转换日期：2026-09-14。四份原始 PDF、四份 Markdown，共 108 页；所有页面均有锚点和原始 PDF 回查链接。转换前后 PDF 的 SHA-256 一致，未修改原论文。第二批的版本与校验另见上节。
- 转换方式：试用 MarkItDown 0.1.7 后，因章节、图形和断行保留不足，最终使用 PyMuPDF4LLM 1.28.2；英文正文未翻译或摘要化。27 个识别为独立公式的区域逐条看图转写 LaTeX，同时保留公式原图；另修复 Wilkens 第 7–8 页的 5 处行内数学表达式。
- 29 个识别为表格的区域保留提取文字并附原貌截图，共 104 张配图与公式/表格截图。Hewamalage 第 29–33、35–36 页的横向表格截图已转正。配图在 `论文配图/`，转移 Markdown 时应一并携带。
- 补修：Hewamalage 第 29–33 页 Table 8 的 43 项指标定义已按截图逐项重建为 Markdown + LaTeX，修复自动提取的 98 处无法解码字符；保留原文印刷公式和原表截图，没有擅自纠正原论文可能的数学或排版问题。
- **已知限制**：其余复杂表头、合并单元格、行内上下标及跨页段落未全部逐符校对。纯文字 AI 无法自动理解图片，不能把本版本称为完美无损转换；公式能否正确计算也不能仅凭转写判断。
- 校验范围：四篇标题、页数、逐页非空、配图链接与 PDF 哈希；独立公式逐条看图核对；正文阅读顺序及部分图表、数值抽检。抽检包括 Aiyer 第 7 页的样本数与统计量、Wilkens 第 4 页的 3,366 场及主/平/客比例、Hewamalage 第 29 页的横向公式表；未宣称逐字校对全文。
- 原有 [Wilkens 早期文字提取版](./2026_Wilkens_德甲预测与滚动验证_原文文字版.md) 保留作溯源，日常阅读优先使用上表的新 Markdown 与原始 PDF。
- 此索引与 Graphify 关联用于检索和方法学习，不自动修改分析规程、下注条件或长期全局记忆。

| 文件 | PDF 页数 | 独立公式 LaTeX | 表格截图 | 配图总数 |
| --- | ---: | ---: | ---: | ---: |
| Wheatcroft | 29 | 5 | 3 | 15 |
| Aiyer | 16 | 0 | 8 | 14 |
| Hewamalage | 45 | 14 | 14 | 43 |
| Wilkens | 18 | 8 | 5 | 32 |

本项目现行应用方式见[习惯塑形](../分析复盘记录/总复盘总结.md)及[规则审计](../分析复盘记录/README.md#rule-audit)，它们属于项目方法设计，尚非论文或实测对预测改进的认证。

<a id="classic-papers"></a>
## 一、 原有资料导航（历史条目，书目信息使用前核验）

| 序号 | 核心文献标识 | 刊物与年代 | 核心预测突破 | 强互联关联文献与模型 | 纯净全文链接 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **1710.02824** | 皇家学会 (2017) | 《用庄家自己的数据击败庄家：利用多庄家共识赔率发现定价错误》 | 关联 [BORS 评级](./2018_PLOS_Betting_Odds_Rating_System_BORS.md) 与 [2604 纯赔率模型](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) | [1710 全文](./1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) |
| 2 | **1802.08848** | 统计建模 (2018) | 《历史战绩与博彩赔率联合建模：分层贝叶斯泊松模型》 | 关联 [平局难题](./2017_Problem_of_Correctly_Predicting_Draws_Soccer.md) 与 [Shin 算法](./Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) | [1802 全文](./1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) |
| 3 | **2003.09384** | 风险决策 (2020) | 《让球盘（亚洲盘口）市场有效性检验与贝叶斯因果网络分析》 | 关联 [BORS 评级](./2018_PLOS_Betting_Odds_Rating_System_BORS.md) 与 [2025 深度学习](./2025_Success_Score_Deep_Learning_Football_Prediction.md) | [2003 全文](./2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md) |
| 4 | **2008 顶刊** | 应用经济学 (2008) | 《博彩市场中的散户情绪偏见与庄家西甲定价偏见》 | 关联 [2604 冷门偏差](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) 与 [高平阻盘诱胜总复盘](../分析复盘记录/总复盘总结.md) | [2008 全文](./2008_Sentiment_and_Bookmaker_Pricing_Bias.md) |
| 5 | **2017 IJCSS** | 体育计算机 (2017) | 《有序与名义回归模型及足球平局正确预测的世界难题》 | 关联 [2025 犯规与平局](./2025_Springer_Predicting_Draws_and_Fouls_Bayesian.md) 与 [1802 泊松模型](./1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) | [2017 平局难题](./2017_Problem_of_Correctly_Predicting_Draws_Soccer.md) |
| 6 | **2018 PLOS** | PLOS ONE (2018) | 《BORS 体系：直接用庄家赔率反向提炼球队高灵敏度动态战力》 | 关联 [1710 击败庄家](./1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) 与 [2003 亚盘有效性](./2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md) | [2018 BORS](./2018_PLOS_Betting_Odds_Rating_System_BORS.md) |
| 7 | **2019 Nature** | 自然子刊 (2019) | 《PlayeRank: 足球运动员单兵表现微观多维量化评估开源框架》 | 关联 [2025 深度架构](./2025_Success_Score_Deep_Learning_Football_Prediction.md) 与 [今日球员微观推演](../分析复盘记录/2026-09-08_预测.md) | [2019 Nature](./2019_Nature_PlayeRank_Data_Driven_Framework.md) |
| 8 | **2025 Springer** | 人工智能进展 (2025) | 《粗暴战术犯规与平局概率联合预测贝叶斯网络分类器》 | 关联 [2017 平局难题](./2017_Problem_of_Correctly_Predicting_Draws_Soccer.md) 与 [赫塔费肉搏绞杀复盘](../分析复盘记录/2026-09-07_复盘.md) | [2025 平局与犯规](./2025_Springer_Predicting_Draws_and_Fouls_Bayesian.md) |
| 9 | **2025 深度架构** | 科研广场 (2025) | 《Success Score: 结合球队动态形态与球员表现的深度学习架构》 | 关联 [2019 PlayeRank](./2019_Nature_PlayeRank_Data_Driven_Framework.md) 与 [2003 贝叶斯网络](./2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md) | [2025 深度架构](./2025_Success_Score_Deep_Learning_Football_Prediction.md) |
| 10 | **2403.16282** | 综述预印本 (2024) | 《足球博彩与机器学习预测及赔率估计的演进（最新权威综述）》 | 关联 [2604 纯赔率模型](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) 与 [1710 击败庄家](./1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) | [2403 全文](./2403.16282_The_Evolution_of_Football_Betting_Machine_Learning.md) |
| 11 | **2505.21275** | 状态空间 (2025) | 《滚球盘口能感知进球到来吗？德甲高频实时赔率微观实证》 | 关联 [1710 庄家赔率](./1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) 与 [体彩实时赔率](../AGENTS.md) | [2505 滚球感知](./2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md) |
| 12 | **2604.17194** | 2026 最新 (2026) | 《有效市场假说下的赛果预测：纯赔率与冷门偏差广义线性模型》 | 关联 [Shin 算法专卷](./Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) 与 [2008 散户偏见](./2008_Sentiment_and_Bookmaker_Pricing_Bias.md) | [2604 全文](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) |
| 13 | **Shin & Štrumbelj**| 算法专卷 (2026) | 《Shin与比例归一化：方法说明及适用边界》 | 关联 [2604 纯赔率模型](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md) 与 [1802 泊松去水](./1802.08848_Combining_Historical_Data_and_Bookmakers_Odds.md) | [Shin算法精要](./Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) |
| 14 | **2605.30209** | 2026 前沿 (2026) | 《通过滚球盘口动态与秒级资金流识别资本做局与异常注码》 | 关联 [2505 滚球感知](./2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md) 与 [Shin 算法](./Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md) | [2605 全文](./2605.30209_Betting_Against_Integrity_Identifying_Match_Fixing_Market_Dynamics.md) |
| 15 | **2024 KTH** | 瑞典皇家理工 (2024) | 《必发博彩交易所赔率跳跃与挂单资金流动性预测模型》 | 关联 [2605 资金流做局](./2605.30209_Betting_Against_Integrity_Identifying_Match_Fixing_Market_Dynamics.md) 与 [1710 击败庄家](./1710.02824_Beating_the_Bookies_with_Their_Own_Numbers.md) | [2024 KTH 全文](./2024_KTH_Predicting_Odds_Movement_Betting_Exchange_Liquidity.md) |

---

<a id="reading-boundaries"></a>
## 阅读与迁移边界

上表是历史资料导航，其中刊物、中文题名与方法解读尚未逐项重新核对；不能把目录关联当成论文支持项目阈值或机构意图的证据。原文与本地笔记要分开阅读。

- 概率转换、球队攻防、球员指标与市场变化是不同层次的问题；各方法有输入、样本和假设边界。
- 犯规、赔率变化与平局即使有关联，也不能直接确认因果机制；需要比较替代解释和独立样本。
- [Shin方法笔记](Shin_1993_and_Strumbelj_2014_庄家赔率反向破译算法精要.md)已修正旧公式和内幕解释；它不是原论文或项目已实现功能。
- [智慧复盘论文](README.md#review-papers)用于指导条件评估、时间变化及校准；应用状态见[规则审计](../分析复盘记录/README.md#rule-audit)与[习惯塑形](../分析复盘记录/总复盘总结.md)。
