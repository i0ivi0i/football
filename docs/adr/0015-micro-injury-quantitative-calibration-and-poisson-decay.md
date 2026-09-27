# ADR 0015: 微观伤停量化修正与攻防泊松动态衰减引擎 (Micro-Injury Quantitative Calibration & Dynamic Poisson Decay Engine)

- **状态**: Accepted (已采纳)
- **决策日期**: 2026-09-22
- **决策人**: 主人与 Antigravity AI 对齐确认

---

## 背景与问题陈述 (Context)
此前系统虽确立了伤停物理门禁（ADR-0004/0014）并打通了三层伤停查证渠道（FPL自动化流 + 德转穿透 + 俱乐部战报），但伤停数据此前仅停留在“定性门禁”层面，尚未与 `football-match-analysis` 的泊松攻防模型建立深层数学联动。为响应主人指示将伤停数据在推演中真正利用起来，特制定本决策，建立微观伤停驱动的攻防参数衰减与价值发现闭环。

## 决策内容 (Decision)

1. **三维伤停与战术体能折损模型 (Position & Tactical Impact)**：
   - **门将/后防中轴折损（防守劣化 $\Delta\beta$）**：首发主力门将或主力中卫伤停，该队失球期望系数 $\beta$ 强制上浮 $+15\% \sim +25\%$（防守漏洞放大）；
   - **射手王/组织核心折损（进攻钝化 $\Delta\alpha$）**：队内头号射手或核心进攻中场伤停，该队进球期望系数 $\alpha$ 强制衰减 $-15\% \sim -30\%$（终结效率下降）；
   - **战术打法相克与体能拐点（Tactical & Fatigue Collapse）**：青年军 60 分钟体能断崖或 72h 密集双赛疲劳，动态上调下半场进球期望 $\lambda$；遭遇铁桶大巴克制破防乏力时，动态下调进球期望 $\lambda$；
   - **系统性战力坍塌阈值（Team Collapse）**：当单一球队关键主力伤停 $\ge 4$ 人（如诺茨郡 8 主力重伤潮）或战意动机严重缺失时，判定为【系统性战力断崖】，整体期望值强力向对手倾斜。

2. **动态泊松进球期望联动重算 (Dynamic Goal Expectancy Pipeline)**：
   - 将伤停与战术衰减后的最新攻防参数 $(\alpha', \beta')$ 注入双变量泊松模型：
     $$\lambda_{home}' = \text{Avg} \times \alpha_{home}' \times \beta_{away}' \times \text{HomeFactor}$$
     $$\lambda_{away}' = \text{Avg} \times \alpha_{away}' \times \beta_{home}'$$
   - 重新生成全比分矩阵，导出修正后的无偏客观胜平负概率 $P_{model}'$。

3. **捕捉零售庄家定价迟钝与正期望选拔 (Value Discovery)**：
   - 将修正后的 $P_{model}'$ 与 `football-betting-analysis` 中的做市商 Shin 去水概率 $P_{Shin}$ 比对；
   - 当大众散户受名气影响使零售庄家盘口未充分反映伤停（$|P_{model}' - P_{Shin}| \ge 4\%$）时，触发核心价值预警，计算纯数学 $+EV = (P_{model}' \times Odds) - 1$，驱动阶梯定注。

## 影响与收益 (Consequences)
- **正面收益**：伤停数据彻底成为改写胜负平概率与挖掘超额 +EV 的核心发动机，将理论优势转化为实战维度的降维打击。
- **潜在代价**：需维持三层伤停渠道的持续查验，但确保了每一个推荐都具备无可辩驳的物理数据支撑。
