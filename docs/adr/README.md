# 架构决策记录集 (Architecture Decision Records, ADR)

本文档索引本项目确立的 16 项核心架构决策记录（ADR）。每一项决策均针对实际推演中的痛点制定，全面贯穿“AI 战术球商与全息博弈智慧”，与 [AGENTS.md](../../AGENTS.md)、[量化术语表](../glossary.md) 及 [知识图谱](../../graphify-out/GRAPH_REPORT.md) 形成严密互锁。

---

## ADR 索引总表

| 编号 | 决策标题 | 核心内涵 | 状态 |
| :---: | :--- | :--- | :---: |
| [ADR 0001](0001-best-value-selection-mode.md) | **全盘单一最佳价值推演模式** | 结合 AI 战术穿透打破胜平负人为割裂，每日仅推选 1~2 场全盘最高价值标的，允许全日空仓 | Accepted |
| [ADR 0002](0002-pure-mathematical-ev-orientation.md) | **纯数学 +EV 极值与战术一票否决** | 纯数学 $EV = P \times Odds - 1$ 为基准；战术相克/诱盘陷阱一票抹杀；低赔强制 $\ge 5\%$ 安全边际 | Accepted |
| [ADR 0003](0003-hybrid-probability-engine.md) | **双引擎混合概率架构** | 尖端做市商 Shin 去水无偏基准 与 独立 AI 四维战术博弈（相克/体能/战意/中轴）微观校准互校 | Accepted |
| [ADR 0004](0004-mandatory-missing-players-physical-gate.md) | **伤停与首发刚性物理门禁** | 强制物理调取双方首发伤停，评估中轴系统性代偿能力，严禁未核验伤停即定性胜负 | Accepted |
| [ADR 0005](0005-minimalist-fast-decision-card-layout.md) | **极简秒看纯数据决策卡** | 剥离冗长套话，工整表格直给终审指令【胜/平/负/观望空仓】，剧本栏直击战术死穴与胜负手 | Accepted |
| [ADR 0006](0006-aiyer-deep-academic-post-match-review.md) | **Aiyer (2023) 赛果解耦深度复盘** | 赛后遮蔽比分审核事前决策质量，严格解耦“偶发赛果”与“决策逻辑”，严禁马后炮 | Accepted |
| [ADR 0007](0007-tiered-ev-staking-policy.md) | **动态阶梯定注策略** | 依据纯数学 +EV 与战术确定性严格执行：<3% 为 0u(空仓)；3-6% 为 1u；6-10% 为 2u；$\ge 10\%$ 顶格 3u | Accepted |
| [ADR 0008](0008-adaptive-odds-movement-recalibration.md) | **异动自适应重估模型** | 当做市商盘口位移 $|\Delta Odds| \ge 0.15$ 或水位波动 $\ge 8\%$ 时强制自适应重算最新 EV | Accepted |
| [ADR 0009](0009-mandatory-verified-polymarket-linking.md) | **Polymarket 真实链接刚性交付** | 强制附带实测存活或已核验的 Polymarket 预测市场直达 URL，无市场如实说明，严禁造假 | Accepted |
| [ADR 0010](0010-bookmaker-accumulator-harvesting-and-favourite-trap.md) | **庄家对赌头寸与串关收割机制** | 基于 Levitt (2004) 理论破除低赔稳胆执念，防范机构利用大热诱聚连环串关资金后冷平冷负收割 | Accepted |
| [ADR 0011](0011-sporttery-official-fixtures-physical-reconciliation-gate.md) | **官方开售清单物理对账门禁** | 推演前必须物理核验体彩真实开售序号（001~N），首尾闭合，严防早场截售导致漏网与断号 | Accepted |
| [ADR 0012](0012-professional-odds-api-time-series-integration.md) | **做市商矩阵与时序流水追踪** | 接入主流机构(Pinnacle/Bet365/体彩)比对初盘锚点与即盘位移，消除单点静态认知茧房 | Accepted |
| [ADR 0013](0013-odds-movement-and-bookmaker-intent-decoding.md) | **时序异动与庄家意图反向破译** | 量化三维破译（初即位移 RLM、欧亚背离、真实做市商离散度），拒绝赛果倒推机构意图 | Accepted |
| [ADR 0014](0014-hybrid-dual-skill-grounding-and-anti-hallucination-gate.md) | **双引擎融合做实与防幻觉门禁** | 融合 match-analysis 与 betting-analysis；剔除虚假50家高频包装；数据缺失强制打 N/A 水印 | Accepted |
| [ADR 0015](0015-micro-injury-quantitative-calibration-and-poisson-decay.md) | **微观伤停量化与攻防泊松衰减** | 建立位置权重折损模型（中卫/门将防守劣化、前锋进攻钝化），联动泊松模型重算真实概率与 +EV | Accepted |
| [ADR 0016](0016-tactical-micro-metrics-and-pressing-conversion-penalty.md) | **全域微观战术指标与逼抢转化惩罚** | 集成 PPDA/Field Tilt/夺回/射门质量，建立围攻破大巴乏力衰减模型，精准预警冷平与爆冷 | Accepted |


