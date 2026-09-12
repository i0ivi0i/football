> **学术知识网络导航**：[系统大脑 AGENTS.md](../AGENTS.md) · [文献总索引与导读](README_学习资料索引与经典论文导读.md) · [实战总复盘总结](../分析复盘记录/总复盘总结.md) · [战绩胜率看板](../分析复盘记录/总准确率.md) · [最新赛前推演](../分析复盘记录/2026-09-12_预测.md)

---

Success Score: A Deep Learning Framework for
Predicting Football Match Outcomes and Evaluating
Team Performance

Farzam Manafzadeh

Shahid Beheshti University

Changiz Eslahchi

Shahid Beheshti University

Hadi Nobari

Universidad Politécnica de Madrid

Article

Keywords:

Posted Date: October 20th, 2025

DOI: https://doi.org/10.21203/rs.3.rs-7736577/v1

License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License

Additional Declarations: No competing interests reported.

Success  Score:  A  Deep  Learning
Framework for Predicting Football Match
Outcomes
Team
Performance

Evaluating

and

Farzam Manafzadeh1, Changiz Eslahchi1, Hadi Nobari2

1Department of Computer Science, Shahid Beheshti University, Tehran, Iran
2LFE Research Group, Department of Health and Human Performance, Faculty of Physical Activity and Sport Science (INEF), Universidad Politécnica
de Madrid, Madrid, Spain.

Corresponding author: Hadi Nobari (e-mail: Hadi.Nobari1@gmail.com)

This work received no support.

ABSTRACT

This study presents a novel predictive framework for estimating football match outcomes and assessing team
performance through a new metric called the Success Score. This metric integrates Expected Goals (xG) with
actual  scoring  results  to  provide  a  comprehensive  evaluation  of  both  opportunity  creation  and  offensive
execution. A Deep Neural Network (DNN) was trained on three seasons (2020–2021, 2021–2022, 2022–
2023) of match data from four major European leagues, incorporating features such as tactical play styles,
rolling  performance  averages,  and  team  quality  indicators.  The  model  demonstrated  strong  predictive
performance,  achieving  a  Mean  Absolute  Error  (MAE)  of  0.3142  and  an  R²  score  of  0.8592  in  cross-
validation. It also generalized effectively to out-of-sample matches from the 2024–2025 season. Furthermore,
the  Success  Score  allowed  for  the  classification  of  outcomes,  enabled  outcome  prediction  with  73.30%
accuracy for Win vs. Not Win and 75.13% for Lose vs. Not Lose. Beyond predictive accuracy, the framework
offers
revealing  patterns  of  overperformance  and
underperformance. Case studies of FC Barcelona and Manchester United illustrate their practical utility for
tactical  analysis  and  strategic  planning.  This  scalable,  data-driven  approach  advances  modern  football
analytics by supporting continuous performance monitoring and informed decision-making.

team  dynamics,

interpretable

insights

into

INTRODUCTION

Predicting match outcomes in football remains a challenging task for coaches, analysts, and fans. This complexity arises from the
interaction of various tactical styles, team dynamics, and situational factors, such as player form. Additionally, football differs
from other team sports like basketball or ice hockey due to its low frequency of scoring attempts and goals, which amplifies its
inherent unpredictability [1]. The fascination of football largely stems from its inherently complex nature. A multitude of factors,
both on and off the field, interact to influence match outcomes, showcasing the sport’s intricate and dynamic character. Off-field
factors, such as travel fatigue, home-crowd advantage, and players’ psychological states, significantly influence match outcomes.
Buchheit  et  al.  analysed  over  61,000  football  matches  and  demonstrated  that  travel  distances  influence  match  outcomes,
underscoring the importance of off-field dynamics [2]. On-field factors,  such as team formations, player quality, and tactical
decisions, also play a major role in determining the result of a game. Yeung et al. emphasized the significance of team formations
and FIFA player ratings in predicting match outcomes, highlighting the importance of tactical choices and player capabilities [3].
FIFA provides comprehensive data about football teams and player ratings. Nouraie et al. utilized the FIFA (SoFifa) dataset, also
used in our study, to develop an intelligent player selection system. By leveraging neural networks and the Hungarian algorithm,
they  optimized  starting  line-ups  based  on  player  ratings,  demonstrating  the  potential  of  machine  learning  in  refining  team
formations and strategic decisions [4]. Nouraie and Eslahchi further contributed to this area by identifying key attributes that
influence a player’s success in specific positions. Their study offers a data-driven approach to assist teams in optimizing player
selection  and  positioning,  thereby  enhancing  overall  team  performance  [5].  In  football  statistics  and  data  science,  team
performance is evaluated using a wide range of parameters collected through advanced technologies such as computer vision and
manual monitoring. Platforms like FBref provide extensive match data, including metrics such as passes, pass accuracy, long

1

balls, and shots. From this data, we have categorized tactical play styles by grouping related statistics into coherent patterns. In
our  analysis,  we  adopted  a  framework  of  ten  primary  football  tactics,  each  representing  a  distinct  strategic  approach.
Understanding these tactical profiles is essential in football analysis, as they shape how teams approach matches, leverage their
strengths, and respond to their opponents. Strategic adaptability, whether to exploit a weakness or maintain control, often defines
the outcome of a game. For example, Plakias et al. conducted a systematic review to  identify soccer players’ playing styles,
focusing on their positions within team formations [6]. Building on this understanding of tactics and individual contributions, we
present a structured summary of common tactical play styles and their associated measurable features. Table 1 outlines ten distinct
tactical styles, each capturing a unique strategic approach in football. These styles can be quantified using specific performance
metrics extracted from match data. For example, Possession Play emphasizes maintaining control through short passes and patient
build-up, while Counter-Attack relies on quick transitions and exploiting space with long balls. High Press is characterized by
intense pressure in advanced areas to regain possession, whereas Direct Play bypasses the midfield through rapid, vertical passing.
By  associating  tactical  styles  with  measurable  indicators,  we  can  incorporate  tactical  dimensions  into  predictive  models,
improving both their accuracy and real-world applicability.

Recently,  metrics  like  Expected  Goals  (XG)  have  been  introduced  to  offer  a  statistical  measure  of  the  quality  of  scoring
opportunities, enabling a deeper understanding of team and player performance beyond final results [20]. Such measures have
proven instrumental in bridging the gap between raw match outcomes and the underlying dynamics of gameplay. However, while
XG provides valuable insights into scoring probabilities, it does not fully account for the influence of tactical styles and  team
strategies. Studies such as those by Fernandez-Navarro et al. [21] have highlighted the importance of including contextual and
tactical variables such as pressing intensity, counter-attacking tendencies, and positional play into performance evaluations.

With the advent of machine learning, predictive modelling in football has experienced a significant transformation. Researchers
have explored a variety of algorithms and frame- works to improve the accuracy of prediction. Ren and Susnjak [22] applied the
Kelly index to classify matches based on predictive difficulty, benchmarking machine learning models against bookmaker odds.
Constantinou  [23]  introduced  the  Dolores  framework,  a  hybrid  Bayesian  network  that  integrates  dynamic  ratings  to  predict
outcomes across multiple leagues. Mills et al. [24] employed logistic regression, XGBoost, and neural networks to predict results
in multiple leagues, emphasizing data augmentation and feature selection. Huba´ek et al. applied gradient-boosted trees to predict
soccer match outcomes using relational data, demonstrating improved predictive accuracy compared to traditional models [25].
Ievoli  and  Palazzo  [26]  demonstrated  that  passing  network  indicators  that  quantify  player  interactions  improved  forecasting
models.  These  studies  highlight  the  growing  role  of  machine  learning  in  predicting  football  outcomes  and  its  potential  to
outperform traditional statistical methods.

Building  on  these  advances,  our  study  focuses  on  integrating  tactical  data  with  outcome  prediction  by  introducing  a  new
scalable  statistical  parameter,  the  Success  Score.  This  continuous  metric  estimates  a  team’s  probability  of  success  against  a
specific opponent by combining Expected Goals with Actual Goals Scored. By capturing both the quality and the realization of
scoring chances, the Success Score offers a more nuanced assessment of team performance. Using match data from 2021 onward,
we  incorporate  this  metric  into  a  modeling  pipeline  that  reflects  the  evolving  dynamics  of  modern  football.  This  approach
transforms traditionally qualitative aspects, such as team strength and tactical efficiency, into quantifiable predictive features.

Table 1. Tactical play styles and their associated metrics.
Summary of the ten tactical play styles used in this study and the match statistics used to compute each style score (metrics sourced
from FBref). Abbreviations: xG, expected goals. References informing definitions: [7–19].

Tactical Play Styles
Possession Play

Counter-Attack

High Press

Direct Play

Wing Play

Set Piece Focus
Creative Playmaking

Identified Features from Data
Ball possession, total passes, pass accuracy (%), own half
passes, XG from open play
Low ball possession, big chances created, ac- curate long
balls, opposition half passes, off- sides, shots inside the
box
Fouls committed, opposition half passes, shots inside the
box, corners, advanced throw-ins
Accurate  long  balls,  shots  inside  the  box,  big  chances
created, offsides
Accurate crosses, shots inside the box, corners, advanced
throw-ins
XG from set plays, corners, accurate crosses
Pass accuracy (%), big chances created, ac- curate long

References
[7, 8]

[9]

[10]

[11]

[12, 13]

[14]
[15]

2

Playing Out from the Back

Low Block

High Defensive Line

balls, opposition half passes
Accurate short passes, accurate long balls, build-up play
from defensive third
Blocked shots, own half entries, fouls com- mitted, shots
conceded from outside the box
Offsides forced, opposition half passes, fouls committed,
shots inside the box conceded

[16, 17]

[18]

[19]

METHODS
In this study, we develop a predictive model to estimate the success score, a novel performance metric designed to quantify and
differentiate the performance of two competing football teams before a match occurs. This model leverages machine learning
techniques and incorporates various tactical, statistical, and contextual features to generate pre-match predictions.

A. DATA SETS
To  support  this  research,  we  utilized  two  key  datasets:  FBref  Match  Data  and  SoFIFA  Team  Attributes,  which  together
provided a rich foundation for feature engineering and model development. We used data from 97 teams across four leagues:
La Liga (Spain), Premier League (England), Bundesliga (Germany), and Serie A (Italy) for three seasons (2020–2021, 2021–
2022, 2022–2023)

The FBref dataset contains match-level statistics from the top four European football leagues during three seasons (2020–
2021,  2021–2022,  2022–2023).  Key  attributes  include:  Match  Details:  Team  names,  final  scores,  and  (XG).  Performance
Metrics: Shots, ball possession, fouls, corners, and passes, among others.
This dataset served as the primary source for calculating the Success Score and other match-specific metrics, forming the core
inputs for the predictive model.

The  SoFIFA  dataset  provides  detailed  team-level  attributes,  including:  Overall  and  Positional  Ratings:  Ratings  for  attack,
midfield, and defence. Prestige Indicators: Measures of domestic and international prominence.

These attributes added contextual information about team quality and were instrumental in feature engineering.

B. SUCCESS SCORE DEFFENITION
The Success Score is a performance metric designed to evaluate a football team’s effectiveness in a match. By combining
actual goals scored with Expected Goals (XG)- which estimate the probability of a shot resulting in a goal based on various
features of the shot- the Success Score provides a more comprehensive assessment of performance. This dual approach reflects
both outcomes (goal-scoring efficiency) and opportunities (quality of chances created). The Success Score is calculated in
three main steps:

I.

Offensive Performance Metric: For each team, an offensive performance score is calculated as:

𝑀((cid:1834))   =  (cid:1833)((cid:1834))   +  (cid:1850)(cid:1833)((cid:1834))   +  (cid:2010)

             (2)

             (1)

Where:
G(H) and G(A) denote the actual goals scored by the home and away teams.
XG(H) and XG(A) denote the expected Goals for the home and away teams.
β = 0.5 is a base value added to ensure minimum contributions for all teams.

𝑀((cid:1827))   =  (cid:1833)((cid:1827))   +  (cid:1850)(cid:1833)((cid:1827))   +  (cid:2010)

II.

Sigmoid Scaling: The offensive metrics are then scaled using a sigmoid function to avoid extreme values:

(cid:1845)((cid:1834)) =

1+(cid:3032)

1

−(cid:3286)((cid:3262)((cid:3257))−(cid:3299)0)

                       (3)

3

                       (4)

1

1+(cid:3032)

−(cid:3286)((cid:3262)((cid:3250))−(cid:3299)0)

(cid:1845)((cid:1827)) =

Where:
k is sigmoid steepness. Sigmoid steepness controls how smoothly values transition. A lower k value (e.g., k = 0.8) results in
smoother transitions.
x0 = 2 is the transition point chosen based on the expected range of offensive metrics.
The sigmoid function addresses two key challenges:
Amplifying Small Values: Ensures meaningful contributions, particularly for teams with low goals or XG.
Flattening Large Values: Avoids extreme dominance by scaling down outliers.
Additionally, the inclusion of a base parameter  β = 0.5 in the offensive performance metric ensures fairness by preventing
negligible contributions from teams with zero goals or XG
III.

Success Score Calculation: The final Success Score is calculated as an interdependent metric:

(cid:3020)((cid:3009))

(cid:1845)(cid:1845)((cid:1834)) =

(cid:3020)((cid:3009))+(cid:3020)((cid:3002)) × 10

                       (5)

                      (6)

This interdependent calculation measures not only offensive strength but also includes defensive contributions, as stronger
defences reduce the opposing team’s Success Score.

(cid:1845)(cid:1845)((cid:1827)) = 10 − (cid:1845)(cid:1845)((cid:1834))

FEATURE ENGINEERING
While the actual Success Score can be calculated after a match based on a team’s performance in terms of Expected Goals and
goals scored, its real value lies in being able to estimate it before a match is played. A reliable pre-match prediction enables
teams, analysts, and decision-makers to assess the likely performance of a team against a specific opponent, aiding in tactical
planning, player selection, and match preparation. To make this possible, we engineered a comprehensive set of features that
encapsulate team dynamics and match context. These features were derived from tactical play styles, rolling averages of recent
performance metrics, and static team attributes. By leveraging both contextual and statistical information, the model aims to
provide a robust and interpretable forecast of team performance.

A. Tactical Play Style Scores
The Tactical Play Style Score quantifies a team’s performance based on various tactical approaches during a match. Each score
is calculated using the average of relevant match metrics associated with a specific tactical play style as outlined in  Error!
Reference source not found.. The general formula for calculating the Tactical Play Style Score (Tstyle) is:

style

(cid:3041)

Where:
Tstyle is the score for a specific tactical play style (e.g., Possession Play, Counter Attack, etc.).

(cid:1846)

=

∑ (cid:1850)(cid:3036)                                      (7)
(cid:3036)=1

1
(cid:1866)

Xi represents the value of the i-th metric associated with that tactical play style.

n is the total number of metrics considered for the given play style.

For  each  match,  the  Tactical  Play  Style  Scores  are  calculated  separately  for  the  home  and  away  teams.  These  scores  are
represented as vectors:

Where:

HOME

(cid:1846)
AWAY

(cid:1846)

= [(cid:1846)1

′
= [(cid:1846)1

(cid:1846)2

′
(cid:1846)2

(cid:1846)3

′
(cid:1846)3

(cid:1846)4

(cid:1846)5

(cid:1846)6

(cid:1846)7

(cid:1846)8

(cid:1846)9

(cid:1846)10]

′
(cid:1846)4

′
(cid:1846)5

′
(cid:1846)6

′
(cid:1846)7

′
(cid:1846)8

′
(cid:1846)9

′
(cid:1846)10

]

T₁ and T₁′ denote the Possession Play Score. T₂ and T₂′ denote the Counter-Attack Score. T₃ and T₃′ denote the High Press

4

Score. T₄ and T₄′ denote the Direct Play Score. T₅ and T₅′ denote the Wing Play Score. T₆ and T₆′ denote the Set Piece Focus
Score.T₇ and T₇′ denote the Creative Playmaking Score.T₈ and T₈′ denote the Playing Out from the Back Score. T₉ and T₉′
denote the Low Block Score. T₁₀ and T₁₀′ denote the High Defensive Line Score.

B. Rolling Averages
To capture both short-term fluctuations and long-term trends in team performance, we calculate rolling averages for 14 metrics
derived from Tactical Play Style Scores and Performance Outcome Metrics. These metrics include: Tactical Play Style Scores:
10 scores corresponding to various tactical approaches (e.g., Possession Play, Counter-Attacks, High Press, etc.). Performance
Outcome Metrics: Success Scores, Goals Scored, Goals Conceded, and Points Earned.

Rolling averages allow the model to analyse both recent form and overall season consistency, providing a dynamic view of
team performance. Short-term rolling averages capture fluctuations in performance over the last five matches, while long-term
averages  reflect  sustained  trends  over  the  season.  This  dual  approach  ensures  that  the  model  accounts  for  evolving  team
dynamics and contextual factors, offering a nuanced understanding of team readiness and potential performance in upcoming
games. The rolling averages for each team are calculated starting from the second game of the season, as at least one match is
required to compute these metrics. For teams that have not yet played five matches, the rolling averages are computed using
the  available  number  of  matches  until  the  required  window  size  is  reached.  The  general  formulas  for  calculating  rolling
averages are:

short

t

long

t

Where:
t is the current match week; Mi is a performance metric and:

Mt

=

1
5

∑ Mi
i=t−4

,

Mt

=

1
t − 1

∑ Mi
i=2

         (8)

 shows the short-term rolling average over the last five matches.

long shows the long-term rolling average over all previous matches in the season.
short

Mt
Mt
Mi shows the value of a performance metric in the i-th match.
t shows the current match week.

C. Dynamic Feature Vectors
For each match, we construct four feature vectors short-term and long-term vectors for both the home and away teams. These
vectors encapsulate the 14 rolling average metrics for each team. The home and away feature vectors are structured as follows:

[(cid:1845)(cid:1846){ℎ(cid:3042)(cid:3040)(cid:3032)},

(cid:1838)(cid:1846){ℎ(cid:3042)(cid:3040)(cid:3032)},

(cid:1845)(cid:1846){(cid:3028)(cid:3050)(cid:3028)(cid:3052)},

(cid:1838)(cid:1846){(cid:3028)(cid:3050)(cid:3028)(cid:3052)}]

Each vector includes:
10 rolling averages of Tactical Play Style Scores. 4 rolling averages of Performance Outcome Metrics (Success Scores, Goals
Scored, Goals Conceded, and Points Earned).
Rolling  averages  offer  several  key  advantages:  Smoothing  Variances:  They  reduce  short-term  variability  and  emphasize
consistent trends in team performance. Dynamic Insights: By combining both short-term and long-term trends, rolling averages
provide a dynamic understanding of team strengths and weaknesses across different phases of the season. Studies by Oliva-
Lozano et al. (2020) [27] demonstrated the effectiveness of rolling averages in identifying worst-case scenarios in professional
soccer,  while  Griffin  et  al.  (2021)  [28]  highlighted  their  advantages  over  exponentially  weighted  moving  averages  for
performance analysis. By integrating these metrics dynamically, our model captures the evolving nature of team performance
and contextualizes tactical effectiveness and stability over time.

D. Team Quality and Prestige Features
Using the SoFIFA dataset, we added features reflecting team quality and reputation:
Quality  Features  (QF):  Overall,  attacking,  midfield,  and  defensive  ratings  (on  a  100-point  scale).  Prestige  Features  (PF):
Domestic and international prestige scores (on a 10-point scale).

E. Input Vector Construction
For each match, we constructed 68-dimensional feature vectors by combining the engineered features for both the home and
away teams:

(cid:1848)  = [(cid:1845)(cid:1846)ℎ(cid:3042)(cid:3040)(cid:3032), (cid:1838)(cid:1846)ℎ(cid:3042)(cid:3040)(cid:3032), (cid:1845)(cid:1846)(cid:3028)(cid:3050)(cid:3028)(cid:3052), (cid:1838)(cid:1846)(cid:3028)(cid:3050)(cid:3028)(cid:3052), (cid:1843)(cid:1832)ℎ(cid:3042)(cid:3040)(cid:3032), (cid:1843)(cid:1832)(cid:3028)(cid:3050)(cid:3028)(cid:3052), (cid:1842)(cid:1832)ℎ(cid:3042)(cid:3040)(cid:3032), (cid:1842)(cid:1832)(cid:3028)(cid:3050)(cid:3028)(cid:3052)]

5

These vectors formed the input to our predictive model.

Model Development
We employed a Deep Neural Network (DNN) with the following structure: Input Layer: 68 features. Hidden Layers: Four
fully connected layers (256, 128, 64, 1 neurons) with Tanh activations and Dropout (0.2) regularization. Output Layer: A single
neuron with linear activation, predicting the home team’s Success Score.

A. Training Strategy
The model was trained using five-fold cross-validation. Within each training fold, we applied random oversampling to balance
the data; validation and test splits were left untouched.

B. Hyperparameter Selection
The  selection  of  hyperparameters  was  conducted  iteratively,  focusing  on  achieving  optimal  performance  and  robust
generalization. The following hyperparameters were tuned through experimentation: Learning Rate: A learning rate of 0.001
was  chosen  for  the  Adam  optimizer.  Preliminary  trials  showed  that  this  value  achieved  smooth  convergence  without
oscillations, balancing training stability and convergence speed. Epochs: The model was trained for 40 epochs. This value was
determined  as optimal  after  testing  a  range  of  20  to 50  epochs,  ensuring  stable  convergence  while  avoiding  overfitting  or
underfitting. Batch Size: A batch size of 64 was selected after evaluating options of 16, 32, and
Data augmentation and cross-validation. To address class imbalance while avoiding data leakage, random oversampling was
applied only to the training split inside each cross-validation fold. Validation and test sets were never oversampled. Five-fold
CV was used, with 80% of the data for training after within-fold oversampling and 20% held out for validation in each fold.

This  hyperparameter  configuration  was  iteratively  refined,  achieving  a  balance  between  predictive  accuracy  and  model
robustness.  The  final  setup  allowed  the  model  to  generalize  effectively  across  varying  football  match  scenarios.  Error!
Reference source not found. provides an overview of all steps of the method.

Results
This section presents a detailed evaluation of the model’s predictive accuracy, generalization capabilities, and potential for
real-world application. The analysis begins with an investigation into home and away success scores, followed by an evaluation
of the model’s performance on both test data and unseen data from the 2024–2025 season. Finally, success score ranges are
defined and optimized for classifying match outcomes, with their application demonstrated through predictions of match results
and  team-level  insights.  As  a  case  study,  the  performances  of  Manchester  United  and  Barcelona  in  different  leagues  are
analysed by comparing their predicted and actual success scores, providing a detailed discussion on their respective outcomes.

Figure 1. Overview of the modelling pipeline.

6

(A) Data acquisition from SoFIFA (team attributes) and FBref (match statistics). (B) Pre-processing and feature engineering,
including computation of tactical play-style scores, short- and long-term rolling averages, and team quality/prestige features.
(C)  Deep  neural  network  (DNN)  training  to  predict  the  home  Success  Score,  SS(H),  on  a  0–10  scale.  Abbreviations:  xG,
expected goals; DNN, deep neural network; SS(H), home Success Score; SS(A), away Success Score.

A. Statistical Analysis of Home Success Scores Across Seasons and Leagues
To quantify home-ground advantage, we performed a one-sided paired t-test comparing team Success Scores at home versus
away. The null and alternative hypotheses were H₀: μ_home ≤ μ_away; H₁: μ_home > μ_away. The test yielded t = 13.24 and
p = 3.18×10⁻³⁹, rejecting H₀ and supporting a home-ground advantage.

Building on this, we analysed how home success scores varied across leagues and seasons. The mean home success scores for
each  league  and  season  are  summarized  in  Error!  Reference  source  not  found..  The  results  reveal  distinct  league-level
dynamics. La Liga teams exhibited the highest mean success scores across all three seasons, demonstrating a particularly strong
home-ground advantage. By contrast, the Premier League and Serie A showed lower mean scores in certain seasons, reflecting
more  balanced  competition  or  potentially  weaker  home  dominance.  These  variations  highlight  the  role  of  league-specific
factors, such as fan influence, travel distances, and tactical preferences, in shaping home-ground performance. Overall, the
findings underscore the measurable and persistent impact of home-ground advantage, while also
highlighting how its magnitude can differ across leagues and evolve.

Table 2. Mean home Success Score by league and season.
Average home-team Success Scores (SS(H); 0–10 scale) across the English Premier League (ENG), La Liga (ESP), Bundesliga
(GER)  and  Serie  A  (ITA)  for  the  2020–2021,  2021–2022  and  2022–2023  seasons.  Higher  values  indicate  stronger  home
performance. SS(H), home Success Score.

Season

ENG-Premier League

ESP-La Liga

GER-Bundesliga

ITA-Serie A

2021

2223
2324

5.0482

5.3227
5.2914

5.2094

5.4103
5.3613

5.1879

5.3451
5.3255

5.1291

5.2460
5.2929

B. Evaluation of Model performance
The model’s performance was evaluated using a dedicated test dataset composed of matches not seen during training. This
dataset included fixtures from the 2020–2021, 2021–2022, and 2022–2023 seasons, drawn from four major European football
leagues: the English Premier League, La Liga, Bundesliga, and Serie A. The original dataset consisted of 4,213 match records.
To address the limited dataset size and improve the model’s ability to generalize, we applied random oversampling as a data
augmentation strategy. This process expanded the dataset tenfold—from 4,213 to 42,130 samples—by duplicating existing
records.  Unlike  synthetic  augmentation  techniques,  this  method  preserved  the  original  feature-target  distribution  and
maintained the statistical integrity of the dataset. Random sampling ensured that all samples had an equal chance of being
selected, minimizing the risk of introducing bias while enhancing pattern learning during training.
Following augmentation, a 5-fold cross-validation strategy was used to rigorously evaluate the model’s performance. In each
fold, 80% of the data (33,704 samples) was used for training, and the remaining 20% (8,426 samples) was reserved for testing.
This procedure ensured that each sample contributed to both training and validation exactly once, enabling a comprehensive
assessment of model stability. Supplementary Figure S2 presents the training and validation loss curves across the five folds.
The steady decline in training loss, accompanied by consistently low and stable validation loss, indicates effective learning
and strong generalization capability.
To quantify model accuracy, we used three standard regression metrics: Mean Absolute Error (MAE), Mean Squared Error
(MSE), and the coefficient of determination (R2). MAE provides a straightforward measure of average prediction error, MSE
emphasizes the impact of larger errors, and R2 reflects how well the model explains the variability of the target variable.
The results, summarized in Error! Reference source not found., demonstrate the model’s robust predictive performance. The
average MAE across all folds was 0.3142 ± 0.0041, indicating low prediction error. The MSE averaged 0.2470 ± 0.0058, and
the  R2 score reached  0.8592 ±  0.0045,  highlighting  the  model’s  ability  to  capture  and explain  underlying  patterns  in  team
performance. Collectively, these results confirm the model’s high accuracy, stability, and capacity to generalize effectively to

7

unseen match scenarios.

Table 3. Cross-validation performance on the training data.
Five-fold  cross-validation  results  for  predicting  SS(H):  Mean  Absolute  Error  (MAE),  Mean  Squared  Error  (MSE)  and
coefficient of determination (R²). Values are mean ± s.d. across folds. SS(H), home Success Score.

Metric

MAE

MSE

R2

Result (Average ± Std)

0.3142 ± 0.0041

0.2470 ± 0.0058

0.8592 ± 0.0045

C. Evaluation on Unseen Data (2024–2025 Season)
The previous section evaluated the model’s performance during training and validation phases using historical data from the
2020–2021, 2021–2022, and 2022–2023 seasons. In this section, we assess the model’s ability to predict the home Success
Score (SS(H)) for matches in the 2024–2025 football season. This evaluation focuses on the model’s accuracy in estimating
SS(H) values, providing insights into its ability to generalize beyond the temporal scope of its training data.
The model was trained on match data from four major leagues—English Premier League, La Liga, Bundesliga, and Serie A—
and tested on completely unseen data from the first 11 weeks of the 2024–2025 season. As of November 1st of 2024, a total
of  382  games  had  been  played  across  these  leagues.  We  first  computed  the  actual  SS(H)  values  using  the  Success  Score
formula, then compared them to the model’s pre-match predictions to evaluate  accuracy. This evaluation simulates a real-
world deployment scenario, where accurate pre-match predictions can support decision-making in tactical planning, betting
analysis, and performance evaluation. Overall, the model exhibited robust performance in predicting SS(H), achieving a Mean
Squared Error (MSE) of 1.693 and a Mean Absolute Error (MAE) of 1.061 across all leagues. Table 4 presents the league-
specific performance metrics. The English Premier League (ENG) achieved the lowest MAE (0.959), indicating the highest
prediction accuracy for SS(H) in this league. Conversely, La Liga (ESP) recorded the highest MSE (1.862), reflecting greater
variability  in  prediction  accuracy  for  matches  in  this  league.  Ligue  1  (FRA)  was  not  included  in  training;  thus  its  results
represent out-of-domain generalization for the model.
These  results  highlight  the  model’s  capacity  to  generalize  from  historical  data  to  new  match  scenarios.  Additionally,
discrepancies between actual and predicted Success Scores across leagues offer valuable insight into context-specific factors
affecting predictive accuracy, paving the way for future refinement.

Table 4. Predictive performance on unseen 2024–2025 matches (weeks 2–11), by league.
The model was trained on matches from 2020–2021 to 2022–2023. Metrics are Mean Squared Error (MSE) and Mean Absolute
Error (MAE) for home Success Score predictions (lower is better).

League
ENG-Premier League
ESP-La Liga
FRA-Ligue 1
GER-Bundesliga
ITA-Serie A

MSE
1.553
1.862
1.876
1.578
1.561

MAE
0.959
1.107
1.160
1.054
1.030

Applications
We introduce two main applications for our parameter, the success score. The first application is evaluating team performance
by comparing the predicted Success Score, which reflects a team’s potential, with the actual Success Score achieved during
games. This comparison helps determine whether a team performed above, below, or at
their  expected  potential,  offering  a detailed  and  objective  evaluation of performance.  The  second  application  is predicting
match outcomes by analysing the relationship between Success Scores and game results. By identifying specific thresholds
within  the  Success  Score  range  that  correlate  with  outcomes  such  as  wins,  losses,  and draws,  the  model  enables  effective
classification  and  prediction  of  match  results.  This  provides  a  reliable  and  structured  approach  for  understanding  and
forecasting football match outcomes.

8

A. Team Performance Analysis Using Success Score
In this section, we analyse the performances of two teams with contrasting outcomes in the 2024–2025 season: FC Barcelona
and Manchester United. These teams were selected to highlight distinct scenarios in team performance and illustrate how the
Success Score can provide deeper evaluative insights. Manchester United faced significant challenges throughout the season,
resulting in the dismissal of their head coach, Erik ten Hag, after nine weeks. In contrast, FC Barcelona emerged as one of the
most consistent and high-performing teams, reaching the top of La Liga by week 11 and receiving widespread critical acclaim.
By comparing the actual Success Scores achieved by these teams with the predictions generated by our model, we evaluated
their performance across two categories:

I. Solid performance: This category includes matches in which a team met or exceeded its predicted potential. It is further
divided  into:  Exceeding  Expectations:  The  actual  Success  Score  is  higher  than  the  predicted  Success  Score.  Dominant
Performance: Both actual and predicted Success Scores exceed 5, indicating control and superiority over the opponent.  As
Expected in a Weaker Matchup: Both actual and predicted Success Scores are below 5, reflecting that the team met expected
performance in a difficult fixture.

II.  Poor  performance:  Matches  where  a  team  underperformed  relative  to  its  predicted  potential.  Specifically,  this  occurs
when:  Failure  to  Meet  Expectations:  The  predicted  Success  Score  is  above  5,  but  the  actual  Success  Score  falls  below  5
indicating a failure to capitalize on predicted advantage.

By categorizing matches in this manner, we can effectively assess how well teams like FC Barcelona and Manchester United
translated their predicted potential into actual results during the 2024–2025 season. This analysis provides insights into team
consistency and episodes of underperformance. Supplementary Table S1 presents the predicted and actual Success Scores
for both teams, alongside match outcomes and the assigned performance categories.

Manchester United: A Season of Missed Expectations
The 2024–2025 season proved to be a challenging one for Manchester United, who began the campaign with high hopes under
head coach Erik ten Hag. Despite a talented squad and strong predicted Success Scores, the team frequently failed to meet
expectations in crucial matches. This pattern of underperformance ultimately led to a leadership change. Analysing matches
from weeks 2 to 9 reveals several instances of this struggle. In Week 2, for example, United faced Brighton with a predicted
advantage but lost 1–2, resulting in a "poor" performance classification. Such outcomes highlight their recurring inability to
deliver  on  potential,  especially  in  home  games.  Tactical  rigidity  and  a  lack  of  cohesion  were  also  evident.  A  significant
proportion  of  their  matches  during  this  period  were  classified  as  "poor"  performances,  underscoring  consistent
underachievement.  This  ultimately  contributed  to  Ten  Hag’s  dismissal,  reflecting  the  club’s  urgent  need  to  reorient  its
competitive strategy.

Barcelona: A Consistently High-Performing Season
Under the guidance of new manager Hansi Flick, Barcelona has demonstrated remarkable consistency and tactical efficiency.
Despite  an  early  setback  in  a  4–2  loss  to  Osasuna,  the  team  showed  strong form  from weeks  2  to 11,  often  exceeding  its
predicted potential. One standout example occurred in Week 4 against Real Valladolid, where Barcelona not only fulfilled its
predicted dominance but exceeded it with a commanding 7–0 win. Similarly, in Week 6, they defeated Villarreal 5–1 away
from home, again outperforming their predicted Success Score. The majority of Barcelona’s matches were classified as "solid"
performances,  indicating  a  strong  alignment  between  potential  and  execution.  Their  consistent  ability  to  meet  or  exceed
expectations highlights their strategic adaptability and superior match-day execution under Flick’s leadership, driving their
ascent to the top of the La Liga table.

B. Utilizing the Relation Between Success Score and Football Match Outcomes
In this section, we aim to explore the relationship between the Success Score and football match outcomes. To achieve this,
thresholds of the actual Success Score were identified that exhibit the highest correlation with match outcomes. To determine
these thresholds, data from all matches during the 2020–2022–2023 seasons across four major football leagues was analysed.
Threshold selection. Using matches from 2020–2021 to 2022–2023, we swept candidate cut-points for SS(H) and selected
τ_low = 4.6 and τ_high = 5.3 to maximize out-of-fold macro-accuracy for the three-class mapping (Lose/Draw/Win). These
fixed thresholds were then applied, without refitting, to 2024–2025 for evaluation. and are summarized in Table 5. This table
presents the thresholds for the Success Score alongside the corresponding match outcomes. For example, 85.44% of teams
with a Success Score in the range of 0–4.6 lost their matches, 13.46% ended in a draw, and 1.10% won. Similar trends were
observed  for  other  ranges.  Overall,  using  these  thresholds,  77%  of  the  matches  from  those  seasons  ended  with  an  actual
outcome that matched their classified range.

9

Table 5. Outcome rates by actual Success Score threshold range (2020–2021 to 2022–2023).
Percentage of matches resulting in Loss, Draw or Win for three ranges of the actual SS(H): 0–4.6, 4.6–5.3 and 5.3–10. Row
percentages sum to ~100%. SS(H), home Success Score.

Threshold Range
0–4.6 (Lose)
4.6–5.3 (Draw)
5.3–10 (Win)

Loss (%)
85.44
29.57
1.10

Draw (%)
13.46
49.13
16.48

Win (%)
1.10
21.30
82.42

C. Predicting Match Outcomes Using the Predicted Success Score
In this section, we predict match outcomes using the predicted Success Score as the basis for classification. To evaluate the
model’s  performance,  match  data  from  the  2024–2025  season  was  analysed,  covering  weeks  2  to  11  across  the  top  five
European football leagues: the English Premier League (ENG), Ligue 1 (FRA), Bundesliga (GER), La Liga (SPA), and Serie
A  (ITA).  The  thresholds  5.3  and  4.6,  identified  in  the  previous  section,  were  applied  to  classify  match  outcomes.  These
thresholds define two key binary classification scenarios: "Win" vs. "Not Win" and "Lose" vs. "Not Lose." We define the
following binary classification scenarios:
Win vs. Not Win: A "Win" indicates the team won the game, while "Not Win" includes both draws and losses. Scores between
5.3 and 10 were classified as "Win," and scores below 5.3 as "Not Win." Lose vs. Not Lose: A "Lose" indicates the team lost,
with a Success Score between 0 and 4.6, while "Not Lose" includes wins and draws.

The model demonstrated strong performance in both scenarios, as summarized in Error! Reference source not found.. For
"Win vs. Not Win," the model correctly classified 280 out of 382 matches, achieving an accuracy of 73.30%. For "Lose vs.
Not Lose," 287 out of 382 matches were correctly classified, with an accuracy of 75.13%. Performance varied by league, as
shown in Error! Reference source not found.. The highest accuracy for "Lose vs. Not Lose" predictions were in Serie A
(78.21%), while Ligue 1 achieved the highest accuracy for "Win vs. Not Win" predictions (75.00%). The Bundesliga had the
lowest accuracy for "Lose vs. Not Lose" predictions (68.85%). The achieved accuracy rates of 73.30% for "Win vs. Not Win"
and  75.13%  for  "Lose  vs.  Not  Lose"  indicate  strong  predictive  performance,  especially  in  the  context  of  football  match
outcomes, which are inherently uncertain and influenced by numerous factors such as player performance, injuries, and in-
game events. Football outcomes are widely recognized as challenging to predict due to their dynamic nature and the potential
for upsets. Achieving accuracies above 70% suggests that the model successfully captures key patterns and trends in the data,
providing a reliable method for classification. Furthermore, the accuracy compares favourably to other predictive approaches
in football analytics, where models often struggle to exceed 60–70% due to the variability of match results. By leveraging the
Success Score and its optimal thresholds, this model demonstrates an ability to consistently translate predictive metrics into
actionable classifications, making it valuable for applications such as betting, performance analysis, and strategic decision-
making.

Table 6. Outcome-classification accuracy on 2024–2025 matches (weeks 2–11), all leagues combined.
Accuracy for two binary tasks using the predicted SS(H): “Win vs. Not Win” (threshold ≥ 5.3 → Win) and “Lose vs. Not
Lose” (threshold ≤ 4.6 → Lose). SS(H), home Success Score.

Metric

Win - Not Win

Lose - Not Lose

Correct Predictions / Total Predictions

Accuracy (%)

280 / 382

73.30%

287 / 382

75.13%

10

Table 7. Outcome-classification accuracy by league (2024–2025, weeks 2–11).
Per-league accuracy for “Lose vs. Not Lose” and “Win vs. Not Win,” using the SS(H) thresholds defined in Table 6. Leagues:
ENG, ESP, FRA, GER, ITA. SS(H), home Success Score.

League

ENG-Premier League
ESP-La Liga
FRA-Ligue 1
GER-Bundesliga
ITA-Serie A

Lose  -  Not  Lose  Accuracy
(%)
76.5
74.75
76.56
68.85
78.21

Win - Not Win Accuracy (%)

72.50
72.73
75.00
73.77
73.08

Discussion
The results of this study highlight the utility of the Success Score as a robust and interpretable metric for evaluating team
performance  and  predicting  football  match  outcomes.  By  integrating  actual  goals  scored  with  advanced  metrics  such  as
Expected  Goals,  the  Success  Score  provides  a  more  holistic  view  of  a  team’s  effectiveness  on  the  pitch.  The  model
demonstrated strong predictive accuracy, effectively capturing the nuanced dynamics of football matches and generalizing
well to unseen data from the 2024–2025 season. However, league-specific variations—such as higher error rates in La Liga
compared  to  the  English  Premier  League—suggest  the  influence  of  contextual  factors,  including  tactical  preferences,  fan
behaviour, and competitive balance, offering directions for further model refinement. The dual applications of the Success
Score—team performance evaluation and match outcome prediction—underscore its practical value. By comparing predicted
and  actual  scores,  the  metric  enables  analysts  to  identify  overperformance,  underperformance,  and  consistency.  This  was
exemplified in the contrasting 2024–2025 trajectories of FC Barcelona and Manchester United, where Barcelona consistently
aligned  with  model  expectations,  while  United  frequently  fell  short.  Such  analysis  can  support  coaching  evaluations,
performance diagnostics, and mid-season adjustments. For match outcome classification, the model achieved 73.30% accuracy
for "Win vs. Not Win" and 75.13% for "Lose vs. Not Lose," surpassing many benchmarks in football analytics. Given the
sport’s inherent unpredictability—driven by injuries, tactical adjustments, and in-game randomness—this level of performance
highlights the model’s ability to distil complex match dynamics into actionable insights. The use of thresholds derived from
Success Score distributions add interpretability and simplify real-world applications, including match preparation, broadcast
analysis, and betting strategies. Our analysis of home Success Scores reinforced the significance of contextual factors. The
observed home-ground advantage, especially in La Liga, suggests that incorporating features related to venue, crowd intensity,
and travel distance may further enhance model performance. Future iterations could benefit from explicitly modelling these
environmental factors.
Despite  promising  results,  several  limitations  must  be  acknowledged.  First,  while  the  dataset  spans  multiple  seasons  and
leagues, it may not capture long-term tactical evolutions or rare scenarios. Including more seasons, leagues outside Europe’s
top tier, and international competitions could improve generalizability. Moreover, while match-level data is comprehensive, it
does  not  account  for  real-time  events  such  as  injuries, red  cards,  or  tactical  substitutions,  factors  that  often  alter  a  game’s
trajectory. Future models could incorporate live data streams to support in-game forecasting and decision support. Another
avenue for refinement involves model interpretability. While neural networks are powerful, they are often viewed as black
boxes. Employing explainable AI techniques such as SHAP values or permutation importance could offer insight into which
features most influence predictions, helping analysts and coaches trust and act upon the model’s outputs. Similarly, visual tools
like confusion matrices could help diagnose model strengths and limitations in different match contexts. Finally, while fixed
thresholds were effective for outcome classification, they may need adaptive tuning across seasons or leagues to maintain
optimal accuracy. Dynamic thresholding techniques or probabilistic classification frameworks could increase robustness in
changing competitive environments.
In summary, the Success Score provides a scalable, interpretable, and effective framework for quantifying team performance
and forecasting outcomes. Its applications span strategic planning, performance tracking, and predicting.

Conclusion
This study introduced a predictive framework centered on the Success Score; a novel performance metric that blends goals
scored with Expected Goals to offer a more comprehensive evaluation of team effectiveness. Using a deep neural network
architecture trained on three seasons of match data from Europe’s top football leagues, the model achieved strong predictive

11

accuracy and demonstrated generalizability to unseen data from the 2024–2025 season. The model’s strength lies in its feature-
rich  design,  combining  tactical  play  style  indicators,  rolling  performance  averages,  and  team-level  quality  and  prestige
attributes. This multi-dimensional feature set enabled the model to capture both short-term form and longer-term consistency,
contributing to its robust forecasting performance.

The Success Score proved useful in two key applications: assessing whether teams met or missed their expected potential and
predicting match outcomes through interpretable classification thresholds. These insights have value for analysts, coaches, and
performance staff seeking to evaluate strategies, monitor trends, or prepare for opponents.

Looking ahead, future work should focus on extending the dataset to include additional leagues and competitions, incorporating
real-time data streams, and enriching the model with player-level and in-game dynamics. Adding interpretability tools could
also strengthen adoption in applied settings by making predictions more transparent and actionable.

With continued refinement, the Success Score and its predictive framework offer a powerful, scalable approach to advancing
data-driven decision-making in modern football.

Data Availability Statement

All notebooks are available at: GitHub. https://github.com/farzammnf/Success-Score

FBREF’s Dataset available at: FBREF Data. https://github.com/farzammnf/Success-Score/tree/main/Data/Fbref

SoFIFA’s Dataset available at: SOFIFA Data. https://github.com/farzammnf/Success-Score/tree/main/Data/Sofifa

Data used for the Model: Dataset. https://github.com/farzammnf/Success-Score/tree/main/Data/Model%27s%20data

REFERENCES

[1] Berrar, D., Lopes, P. & Dubitzky, W. A data- and knowledge-driven framework for developing machine learning models
to predict soccer match outcomes. Mach. Learn. 113, 8165–8204 (2024).

[2] Settembre, M. et al. Factors associated with match outcomes in elite European football – insights from machine learning
models. J. Sports Anal. 10, 1–16 (2024).

[3] Yeung, C. C. K., Bunker, R. & Fujii, K. A framework of interpretable match results prediction in football with FIFA ratings
and team formation. PLOS ONE 18, e0284318 (2023).

[4] Nouraie, M., Eslahchi, C. & Baca, A. Intelligent team formation and player selection: a data-driven approach for football
coaches. Appl. Intell. 53, 30250–30265 (2023).

[5] Nouraie, M. & Eslahchi, C. Positioning soccer players for success: a data-driven machine learning approach.  Comput.
Math. Comput. Model. Appl. 2, 24–33 (2023).

[6] Plakias, S. et al. Identifying soccer players’ playing styles: a systematic review. J. Funct. Morphol. Kinesiol. 8, 104 (2023).

[7] Casal, C. A., Anguera, M. T., Maneiro, R. & Losada, J. L. Possession in football: more than a quantitative aspect—a mixed
method study. Front. Psychol. 10, 501 (2019).

[8] Casal, C. A., Maneiro, R., Ardá, T., Marí, F. J. & Losada, J. L. Possession zone as a performance indicator in football: the
game of the best teams. Front. Psychol. 8, 1176 (2017).

12

[9] Sarmento, H. et al. Patterns of play in the counterattack of elite football teams—a mixed method approach. Int. J. Perform.
Anal. Sport 14, 411–427 (2014).

[10]  Low,  B.  Z.  W.,  Rein,  R.  &  Memmert,  D.  The  porous  high-press?  An  experimental  approach  investigating  tactical
behaviours from two pressing strategies in football. Int. J. Sports Sci. Coach. 16, 789–797 (2021).

[11] Wikipedia contributors. Long ball. Wikipedia, The Free Encyclopedia https://en.wikipedia.org/wiki/Long_ball (2025).

[12]  Boothroyd,  A.  Wing  play.  FIFA  Training  Centre  https://www.fifatrainingcentre.com/en/practice/elite-sessions/in-
possession/wing-play.php (2022).

[13]  DT  Game.  FM  tactical  styles—wing  play.  Dictate  the  Game  https://dictatethegame.com/fm-tactical-styles-wing-play/
(2022).

[14]  Meighan,  C.  Set-piece  analysis:  the  10  most  interesting  set-piece  routines  from  Euro  2020.  Total  Football  Analysis
https://totalfootballanalysis.com/article/set-piece-analysis-the-10-most-interesting-set-piece-routines-from-euro-2020-tac
(2021).

[15]  Total  Football  Analysis.  U23  superstars:  the  top  young  chance  creators  in  Europe.  Total  Football  Analysis
https://totalfootballanalysis.com/article/u23-superstars-top-young-chance-creators-in-europe-data-analysis-statistics (2023).

[16]  The  Mastermind  Site.  Playing  out
https://themastermindsite.com/2019/08/20/playing-out-from-the-back-full-session-plan-and-key-coaching-points/ (2019).

session  plan  and  key  coaching  points.

the  back:

from

full

[17]  Soccer  Blade.  Long ball  in  soccer:  when  to  use  it  and  why  it’s  effective.  https://soccerblade.com/long-ball-in-soccer/
(2023).

[18]  Coaches’  Voice.  The  low  block:  football  tactics  explained.  https://learning.coachesvoice.com/cv/low-block-football-
tactics-explained-simeone-dyche-mourinho/ (2024).

[19] Football Techniques. What is a high line in football? Should my team use it? https://footballtechniques.co/what-is-a-high-
line-in-football-should-my-team-use-it/ (2022).

[20] Mead, J., O’Hare, A. & McMenemy, P. Expected goals in football: improving model performance and demonstrating
value. PLOS ONE 18, e0282295 (2023).

[21] Fernández-Navarro, J., Fradua, L., Zubillaga, A., Ford, P. R. & McRobert, A. P. Influence of contextual variables on
styles of play in soccer. Int. J. Perform. Anal. Sport 18, 423–436 (2018).

[22] Ren, Y. & Susnjak, T. Predicting football match outcomes with explainable machine learning and the Kelly Index. Preprint
at https://arxiv.org/abs/2211.15734 (2022).

[23] Constantinou, A. C. Dolores: a model that predicts football match outcomes from all over the world. Mach. Learn. 108,
517–546 (2019).

[24] Mills, E. A., Shah, R., Xu, K., Ott, D. & Sharma, A. Data-driven prediction of soccer outcomes using enhanced machine
and deep learning techniques. J. Big Data 11, 38 (2024); 10.1186/s40537-024-00958-7.

[25] Hubáček, O., Šourek, G. & Železný, F. Learning to predict soccer results from relational data with gradient-boosted trees.
Mach. Learn. 108, 29–47 (2019).

[26] Ievoli, R., Palazzo, L. & Ragozini, G. On the use of passing network indicators to predict football outcomes.  Knowl.-
Based Syst. 218, 106997 (2021).

[27] Oliva-Lozano, J. M., Fortes, V., Muyor, J. M. & Alacid, F. Differences in worst-case scenarios calculated by fixed length
and rolling average methods in professional soccer match-play. Biol. Sport 38, 325–331 (2021).

13

[28]  Griffin,  A.,  Kenny,  I.  C.,  Moran,  D. &  Comyns,  T.  A  comparison  of  the  rolling  average  and  exponentially  weighted
moving  average  models  for  calculating  the  acute:chronic  workload  ratio:  a  systematic  review.  Sports  Med.  50,  561–580
(2020).

Author Contributions

F.M.  (Farzam  Manafzadeh)  conceived  the  study,  developed  the  methodology,  implemented  the  analyses,  and  drafted  the
manuscript. C.E. (Changiz Eslahchi) co-conceived the study, contributed to methodology and analysis verification, supervised
the research, and revised the manuscript. H.N. (Hadi Nobari) supervised the research, provided guidance, and contributed to
manuscript revision. All authors reviewed and approved the final manuscript and agree to be accountable for all aspects of the
work. H.N. is the corresponding author (Hadi.Nobari1@gmail.com).

Funding

This research received no external funding.

Acknowledgments

The authors thank FBref and SoFIFA for providing publicly accessible datasets used in this research.

Competing interests
The author(s) declare no competing interests.

Ethics statement

This study investigates publicly available performance data and involved no human participants, personal data, or intervention.
In accordance with the policies of the authors’ institution, formal ethics approval and informed consent were not required for
this research.

14

Supplementary Files

This is a list of supplementary  les associated with this preprint. Click to download.

SupplementaryInformation.docx

