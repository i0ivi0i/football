# Graph Report - 足球预测  (2026-09-07)

## Corpus Check
- 16 files · ~146,848 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 108 nodes · 122 edges · 12 communities
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 17 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d3e37ba8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 8 Capas Betting Inference Model
- Literature Index & Methodology Map
- Bayesian Football Match Modeling
- Betting Market Efficiency Modeling
- Favourite-Longshot Bias Adjustments
- Logit Match Outcome Prediction
- 重点 1：【周一002 西甲】赫塔费 vs 塞尔塔（全天平局第一核心）
- Tactical Play Style Evaluation
- 四、未来平局精算推演：全新“六维加权决策模型”（100分制）
- 重点 2：【周一006 意甲】乌迪内斯 vs 拉齐奥（均势绞杀盘）
- Q: 2026-09-06 中国体彩周日平局预测赛果复盘
- Q: 2026-09-06 9场平局全景深度复盘与机构操盘手法

## God Nodes (most connected - your core abstractions)
1. `8 Capas Betting Inference Model` - 14 edges
2. `2026-09-06 Sporttery Draw Actuarial Analysis Archive` - 13 edges
3. `Literature Index & Methodology Map` - 10 edges
4. `重点 1：【周一002 西甲】赫塔费 vs 塞尔塔（全天平局第一核心）` - 8 edges
5. `四、未来平局精算推演：全新“六维加权决策模型”（100分制）` - 7 edges
6. `Football Quantitative Betting & Prediction Guide` - 7 edges
7. `Shin's Insider Trading Model` - 7 edges
8. `2026-09-06（周日）中国体彩 9 场平局全景深度复盘与机构控盘手法精算报告` - 6 edges
9. `重点 2：【周一006 意甲】乌迪内斯 vs 拉齐奥（均势绞杀盘）` - 6 edges
10. `Hybrid Bayesian Network for Asian Handicap (Constantinou)` - 5 edges

## Surprising Connections (you probably didn't know these)
- `8 Capas Betting Inference Model` --capa_4_solves_draw_underestimation--> `Soccer Draw Prediction Problem`  [INFERRED]
  AGENTS.md → 温故而知新学习资料/2017_Problem_of_Correctly_Predicting_Draws_Soccer.md
- `8 Capas Betting Inference Model` --capa_8_asian_handicap_inference--> `Hybrid Bayesian Network for Asian Handicap (Constantinou)`  [INFERRED]
  AGENTS.md → 温故而知新学习资料/2003.09384_Asian_Handicap_Market_Efficiency_Bayesian_Networks.md
- `2026-09-06 Sporttery Draw Actuarial Analysis Archive` --identifies_match019_draw_trap--> `Draw Bias Phenomenon`  [INFERRED]
  分析复盘记录/2026-09-06_周日体彩平局精算分析与复盘档案.md → 温故而知新学习资料/2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md
- `8 Capas Betting Inference Model` --capa_3_player_tactical_eval--> `Success Score DNN Predictor`  [INFERRED]
  AGENTS.md → 温故而知新学习资料/2025_Success_Score_Deep_Learning_Football_Prediction.md
- `8 Capas Betting Inference Model` --capa_7_inplay_goal_dynamics--> `In-Match Goal Anticipation Hypothesis`  [INFERRED]
  AGENTS.md → 温故而知新学习资料/2505.21275_Do_Betting_Markets_Sense_a_Goal_Coming.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Match Event & Performance Indicators** — doc_playerank_framework, concept_invasion_index, concept_acceleration_index, concept_passing_network [EXTRACTED 0.90]
- **Odds to Outcome Probability Conversion Models** — 温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_olr, 温故而知新学习资料_2017_problem_of_correctly_predicting_draws_soccer_mlr, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_oo_epc, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_fl_glm [EXTRACTED 0.90]
- **Draw Bias and Separate Power Constants Formulation** — 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_fl_glm_model, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_draw_bias, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_two_power_constants_extension [EXTRACTED 0.95]
- **Theoretical Properties of FL-GLM Model** — 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_fl_glm_model, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_property_5, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_property_6, 温故而知新学习资料_2604_17194_forecast_sports_outcomes_under_emh_odds_only_models_proposition_7 [EXTRACTED 0.95]
- **Sunday 2026-09-06 Prime Draw Targets** — analysissunday_match_alaves_osasuna, analysissunday_match_parma_monza, analysissunday_match_juventus_milan [EXTRACTED 0.95]
- **Odds Normalization and Inversion Frameworks** — concept_shin_inversion_model, doc_combining_historical_data_odds, concept_1x2_betting_odds, doc_shin_strumbelj_guide [EXTRACTED 0.95]
- **Football Score Prediction and Betting Market Modelling** — 180208848_combining_historical_data_and_bookmakers_odds_egidi_model, 200309384_asian_handicap_market_efficiency_bayesian_networks_ah_bn_model, 200309384_asian_handicap_market_efficiency_bayesian_networks_betting_evaluation [INFERRED 0.85]
- **In-Match Dynamics and Performance Representation** — 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_expected_goals, 温故而知新学习资料_2025_success_score_deep_learning_football_prediction_tactical_play_styles, 温故而知新学习资料_2505_21275_do_betting_markets_sense_a_goal_coming_ssm_bettors [INFERRED 0.85]
- **Odds Actuarial Modeling and Evaluation Flow** — agents_8capas, analysissunday_archive_20260906, paper_1710_02824_beating_bookies, paper_2018_bors [INFERRED 0.90]

## Communities (12 total, 0 thin omitted)

### Community 0 - "8 Capas Betting Inference Model"
Cohesion: 0.15
Nodes (20): 8 Capas Betting Inference Model, API-Sports Data Pipeline, Football Quantitative Betting & Prediction Guide, Sporttery Calculator Web API, 2026-09-06 Sporttery Draw Actuarial Analysis Archive, Match Actuarial Analysis: Alaves vs Osasuna, Match Actuarial Analysis: Juventus vs AC Milan, Match Actuarial Analysis: Parma vs Monza (+12 more)

### Community 1 - "Literature Index & Methodology Map"
Cohesion: 0.15
Nodes (12): 1x2 Bet Odds & Overround, Acceleration Index, Invasion Index, Passing Network & Flow Centrality, Ranked Probability Score (RPS), Relative Distance to Adjacent Centroids Discretization, Weighted Accuracy (WAP) and Weighted Recall (WAR), Bayesian Network Classifiers for Fouls and Draws (Pérez-Blanco & Salmerón) (+4 more)

### Community 2 - "Bayesian Football Match Modeling"
Cohesion: 0.25
Nodes (8): Hierarchical Bayesian Poisson Model (Egidi et al.), Shin's Normalisation Method, Skellam Distribution Formulation, Dynamic Seasonal Team Effects, Hybrid Bayesian Network for Asian Handicap (Constantinou), Betting Efficiency & Decision Threshold Evaluation, Modified Pi-Rating System, Temporal In-Match Causal Process

### Community 3 - "Betting Market Efficiency Modeling"
Cohesion: 0.33
Nodes (6): Expected Goals (xG), Bookmaker Implied Probability Regression Model, In-Match Goal Anticipation Hypothesis, Continuous-Valued State-Space Model for Bettors, Efficient Market Hypothesis in Sports Betting (EMH), Odds-Only-Equal-Profitability-Confidence (OO-EPC) Method

### Community 4 - "Favourite-Longshot Bias Adjustments"
Cohesion: 0.40
Nodes (6): Draw Bias Phenomenon, FL-GLM (Favourite-Longshot Bias Adjusted GLM), Property 5, Property 6, Proposition 7 (Log-Loss and Profitability), Two Power Constants FL-GLM Extension

### Community 5 - "Logit Match Outcome Prediction"
Cohesion: 0.40
Nodes (5): Soccer Draw Prediction Problem, Elo Rating Difference (E_ij), Multinomial Logit Regression (MLR), Ordered Logit Regression (OLR), Proportional Odds Assumption

### Community 6 - "重点 1：【周一002 西甲】赫塔费 vs 塞尔塔（全天平局第一核心）"
Cohesion: 0.12
Nodes (15): 2026-09-07 周一体彩平局精算推演与机构操盘深度报告, Capa 1 [ODDS]：市场底牌, Capa 1 [ODDS]：市场底牌与倍率背离, Capa 2 [IND]：历史交锋基因, Capa 3 [API]：战术绞杀与白卷特征, Capa 4 [IND]：综合泊松验证, Capa 5 & 8：战意动机与决策, Capa 5 [IND]：庄家利益与杀多赔少心理 (+7 more)

### Community 7 - "Tactical Play Style Evaluation"
Cohesion: 0.67
Nodes (3): Success Score DNN Predictor, Success Score Metric, Tactical Play Styles Framework

### Community 8 - "四、未来平局精算推演：全新“六维加权决策模型”（100分制）"
Cohesion: 0.12
Nodes (15): 1. 真实防范型（实防阻赔 · 占 44.4%）, 1. 维度一：中场绞杀与粗暴犯规率（权重：25% · 第一物理阻断器）, 2026-09-06（周日）中国体彩 9 场平局全景深度复盘与机构控盘手法精算报告, 2. 维度二：机构赔率与盘口结构（权重：25% · 机构底牌透视）, 2. 阻盘诱两头型（高平假象通杀 · 占 55.6%）, 3. 极速打脸的血泪教训：周日019【阿拉维斯 5:2 奥萨苏纳】为什么崩盘？, 3. 维度三：终结匮乏与射门转化软脚率（权重：20% · 破门难度量化）, 4. 维度四：保守保分战意与教练博弈心理（权重：15% · 动机驱动） (+7 more)

### Community 9 - "重点 2：【周一006 意甲】乌迪内斯 vs 拉齐奥（均势绞杀盘）"
Cohesion: 0.33
Nodes (6): Capa 1 [ODDS]：市场底牌, Capa 2 & 3 [API]：球队画像与微观主角, Capa 4 & 5：泊松计算与庄家动机, Capa 6：六维平局评分, Capa 7 & 8：决策落点, 重点 2：【周一006 意甲】乌迪内斯 vs 拉齐奥（均势绞杀盘）

### Community 10 - "Q: 2026-09-06 中国体彩周日平局预测赛果复盘"
Cohesion: 0.50
Nodes (3): Answer, Outcome, Q: 2026-09-06 中国体彩周日平局预测赛果复盘

### Community 11 - "Q: 2026-09-06 9场平局全景深度复盘与机构操盘手法"
Cohesion: 0.50
Nodes (3): Answer, Outcome, Q: 2026-09-06 9场平局全景深度复盘与机构操盘手法

## Knowledge Gaps
- **58 isolated node(s):** `Answer`, `Outcome`, `Answer`, `Outcome`, `一、昨日 9 场平局全景盘面与机构操盘手法定性` (+53 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 63 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `8 Capas Betting Inference Model` connect `8 Capas Betting Inference Model` to `Literature Index & Methodology Map`, `Bayesian Football Match Modeling`, `Betting Market Efficiency Modeling`, `Favourite-Longshot Bias Adjustments`, `Logit Match Outcome Prediction`, `Tactical Play Style Evaluation`?**
  _High betweenness centrality (0.314) - this node is a cross-community bridge._
- **Why does `Football Quantitative Betting & Prediction Guide` connect `8 Capas Betting Inference Model` to `四、未来平局精算推演：全新“六维加权决策模型”（100分制）`, `Literature Index & Methodology Map`?**
  _High betweenness centrality (0.182) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `8 Capas Betting Inference Model` (e.g. with `Hybrid Bayesian Network for Asian Handicap (Constantinou)` and `Shin's Insider Trading Model`) actually correct?**
  _`8 Capas Betting Inference Model` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `2026-09-06 Sporttery Draw Actuarial Analysis Archive` (e.g. with `Shin's Insider Trading Model` and `Draw Bias Phenomenon`) actually correct?**
  _`2026-09-06 Sporttery Draw Actuarial Analysis Archive` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Answer`, `Outcome`, `Answer` to the rest of the system?**
  _58 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `8 Capas Betting Inference Model` be split into smaller, more focused modules?**
  _Cohesion score 0.14736842105263157 - nodes in this community are weakly interconnected._
- **Should `重点 1：【周一002 西甲】赫塔费 vs 塞尔塔（全天平局第一核心）` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._