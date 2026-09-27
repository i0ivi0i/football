# ADR 0016: 全域微观战术指标集成与高位逼抢转化惩罚引擎 (Tactical Micro-Metrics Integration & Pressing Conversion Penalty Engine)

- **状态**: Accepted (已采纳)
- **决策日期**: 2026-09-23
- **决策人**: 主人与 Antigravity AI 对齐确认

---

## 背景与问题陈述 (Context)
在伤停物理门禁（ADR-0004/0015）与体能断崖监控落地后，比赛推演已具备坚实的物理底盘。然而，足球比赛中的“得势不得分”与“围攻反被偷”是导致热门大热暴死、爆出冷平（1-1、0-0）或冷负的核心战术根源。仅看控球率或射门次数常陷入假象；必须将高位逼抢强度（PPDA）、场区倾斜度（Field Tilt）、前场危险夺回、防守动作密度与射门真实质量（xG/Shot、PSxG）全面集成，建立微观战术与泊松攻防期望值（$\lambda$）的深层量化联动。

## 决策内容 (Decision)

1. **全息微观战术指标矩阵 (全量 5 大维度 26 项核心字段)**：
   - **一、压迫与反逼抢维度 (5项)**：`ppda` (逼抢强度)、`opp_ppda` (抗逼抢能力)、`high_turnovers` (高位夺回)、`opp_half_recoveries` (对方半场夺回)、`danger_zone_recoveries` (危险前场夺回)。
   - **二、场区与球权推进维度 (5项)**：`possession_pct` (控球率)、`field_tilt` (前场30米传球倾斜度)、`deep_completions` (禁区前沿深区渗透传球)、`progressive_passes` (推进传球数)、`box_touches` (禁区内触球数)。
   - **三、机会创造与射门质量 (5项)**：`xg` (预期进球)、`xag` (预期助攻)、`xg_per_shot` (单脚射门期望质量)、`psxg_per_sot` (门前射正质量)、`big_chances_ratio` (绝佳机会创造与转化率)。
   - **四、防守微观与门线 (6项)**：`tackles_won` (成功抢断数)、`interceptions` (拦截数)、`clearances` (解围数)、`blocks` (关键封堵射门数)、`box_def_actions` (禁区内防守动作总和)、`psxg_net_goalkeeping` (门将净扑救增益)。
   - **五、球员物理负荷与伤情 (5项)**：`missing_players_count` (伤停人数)、`core_injury_severity` (核心中轴折损权重)、`fixture_congestion_72h` (72小时密集双赛)、`rest_days_gap` (休整天数差)、`sprint_fatigue_index` (60分钟冲刺体能衰减指数)。

2. **高位逼抢转化效率惩罚模型 (Pressing Conversion Efficiency Penalty)**：
   - **触发门限（围攻破防死穴/假性繁荣陷阱）**：
     当优势方满足：
     $$\text{Field Tilt} \ge 65\% \quad \text{或} \quad \text{控球率} \ge 60\%$$
     且 $\text{PPDA} \le 9.5$（形成围攻压制），
     但 $\text{xG / Shot} < 0.085$（破大巴乏力、禁区渗透无门、大量远射浪射）：
   - **泊松进球期望 $\lambda$ 动态衰减重算**：
     - 优势方进球期望衰减：$\lambda_{fav}' = \lambda_{fav} \times (1 - \text{Penalty})$，其中 $\text{Penalty} \in [15\%, 25\%]$；
     - 弱队反击偷刀期望上浮：$\lambda_{dog}' = \lambda_{dog} \times (1 + \text{Bonus})$，其中 $\text{Bonus} \in [10\%, 20\%]$；
   - **矩阵映射**：
     重算泊松概率矩阵，直接压低大热方胜率，大幅拉升 1-1 冷平与让球负概率，直接联锁触发 ADR-0010（庄家串关收割陷阱警报）与 ADR-0002（负期望坚决抹杀）。

3. **微观盘口倍率加权融合进 λ (Micro-Odds → λ Fusion)**：
   - 微观盘口异动（≥10% 位移触发，联动 ADR-0008）不否决也不降级主模型，而是按异动维度数量**动态调整泊松参数 λ**；
   - 融合路径：微观盘口位移 → 映射为攻防效率修正系数 → 代入 $\lambda_{home}$ / $\lambda_{away}$ → 重算比分矩阵与 +EV；
   - 异动维度越多 → λ 修正幅度越大 → 自然产生新概率与新 EV。
4. **微观盘口异动矩阵表交付 (Micro-Odds Anomaly Matrix)**：
   - 每次推演除标准 6 列终审决策卡外，附带一张微观盘口异动矩阵表：

   | 维度 | 初盘 | 即盘 | 位移% | 方向 |
   |------|------|------|-------|------|
   | 角球大小 | — | — | — | — |
   | 犯规数 | — | — | — | — |
   | 黄牌数 | — | — | — | — |
   | 射正数 | — | — | — | — |
   | BTTS | — | — | — | — |
   
   - 无数据维度如实标 [N/A]，严禁脑补。
5. **模型工程落地与门禁 (Implementation)**：
   - 建立专用计算引擎 `脚本/模型/高阶战术压迫引擎.py`；
   - 纳入常规推演自动化管道，与做市商 Shin 赔率去水交叉验证，挖掘被公众舆论忽视的冷门 +EV。

## 影响与收益 (Consequences)
- **正面收益**：精准破解“全场围攻却 1-1 闷平或 0-1 被反击绝杀”的世纪难题，从战术球商与微观数据底层识破庄家开出的低赔诱盘陷阱。
- **协同效应**：与 ADR-0004（伤停）、ADR-0010（防收割）、ADR-0015（泊松衰减）形成四位一体的立体防御体系。
