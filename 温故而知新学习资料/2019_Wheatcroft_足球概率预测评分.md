# Evaluating probabilistic forecasts of football matches: The case against the Ranked Probability Score

> **认知网络导航**：[项目宪法 AGENTS.md](../AGENTS.md) · [习惯塑形芯片](../分析复盘记录/总复盘总结.md) · [最新复盘审计](../分析复盘记录/2026-09-13_复盘.md) · [文献总库](./README.md#review-papers)
> 原文 Markdown 转换版；保留英文内容，非译文、非摘要。
> [原始 PDF](./2019_Wheatcroft_足球概率预测评分.pdf) · [一手来源](https://arxiv.org/abs/1908.08980) · [论文索引](./README.md#review-papers)
> 共 29 页；页码按 PDF 物理页序。使用 PyMuPDF4LLM 1.28.2 转换，2026-09-14。
> 正文可检索；5 个识别为独立公式的区域已逐条看图转写为 LaTeX，并保留原图；表格同时附版面截图。表格内部公式及行内数学尚未全部逐符核对。文字模型无法读取图像内容，涉及公式、图表或精确数值时，须使用具备图像阅读能力的 AI 并核对 PDF。
> 双栏、跨页段落和行内上下标仍可能存在转换误差；此版本不保证无损还原。



---

<a id="pdf-page-1"></a>

## PDF 第 1 页

[回查原始 PDF 第 1 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=1)

# Evaluating probabilistic forecasts of football matches: The case against the Ranked Probability Score 

Edward Wheatcroft 

London School of Economics and Political Science, Houghton Street, London, United Kingdom, WC2A 2AE. 

August 27, 2019 

#### **Abstract** 

A scoring rule is a function of a probabilistic forecast and a corresponding outcome that is used to evaluate forecast performance. A wide range of scoring rules have been defined over time and there is some debate as to which are the most appropriate for evaluating the performance of forecasts of sporting events. This paper focuses on forecasts of the outcomes of football matches. The ranked probability score (RPS) is often recommended since it is ‘sensitive to distance’, that is it takes into account the ordering in the outcomes (a home win is ‘closer’ to a draw than it is to an away win, for example). In this paper, this reasoning is disputed on the basis that it adds nothing in terms of the actual aims of using scoring rules. A related property of scoring rules is locality. A scoring rule is local if it only takes the probability placed on the outcome into consideration. Two simulation experiments are carried out in the context of football matches to compare the performance of the RPS, which is non-local and sensitive to distance, the Brier score, which is non-local and insensitive to distance, and the ignorance score, which is local and insensitive to distance. The ignorance score is found to outperform both the RPS and the Brier score, casting doubt on the value of non-locality and sensitivity to distance as properties of scoring rules in this context.


---

<a id="pdf-page-2"></a>

## PDF 第 2 页

[回查原始 PDF 第 2 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=2)

## **1 Introduction** 

Probabilistic forecasting of sporting events such as football matches has become an area of considerable interest in recent years. One reason for this is that forecasting can help inform gambling decisions and therefore has the potential to support the identification of profitable betting strategies. Probabilistic forecasting has also grown in popularity in the sports media. In some media outlets, for example, estimated probabilities are routinely disseminated in match previews and even in-play. An obvious implication of the growth of probabilistic forecasting in sport is the need for effective methods of forecast evaluation. This is particularly true in the case of gambling where ‘beating the bookmaker’ is a difficult task which typically requires highly informative predictions. However, even when the forecasts are used for purposes other than gambling, there is often still an incentive for the forecasts to be informative, or at least to be perceived as such. There is therefore a need for objective measures of forecast performance. This paper is concerned with the question of how to evaluate probabilistic forecasts of events such as football matches with three or more possible outcomes. 

Evaluation of probabilistic forecasts is typically performed using scoring rules, functions of the forecast and corresponding outcome aimed at assessing forecast performance. A large number of scoring rules have been defined over the years and there is considerable debate surrounding which are the most appropriate. A common approach with which to differentiate candidate scoring rules is to identify desirable properties and favour scores that have them. There is often debate, however, surrounding which properties are (most) desirable and hence a lack of consensus remains. As a result, in fields such as weather forecasting, a wide range of different scores are often presented. 

One property of scoring rules that is perhaps the most widely agreed upon is called propriety. A score is proper if, in expectation, it favours a forecast that consists of the distribution from which the outcome is drawn, i.e a perfect probabilistic forecast. This paper is concerned primarily with two more contentious properties. One of those properties is locality. A score is _local_ if it only considers the probability at the outcome and disregards the rest of the distribution. A _non-local_ score therefore takes at least some of the rest of the forecast distribution into account. The other property of interest concerns whether a scoring rule takes ordering into account. Events with discrete outcomes can be divided into two categories: nominal and


---

<a id="pdf-page-3"></a>

## PDF 第 3 页

[回查原始 PDF 第 3 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=3)

ordinal. Ordinal events have a natural ordering. For example, a question on a survey asking an interviewee to rate a service might have a set of potential responses ranging from ‘very poor’ to ‘very good’. It is clear that ‘very good’ ranks higher than ‘good’, whilst ‘good’ ranks higher than ‘poor’. Nominal events, on the other hand, have no natural ordering. For example, there is no obvious way to rank a set of colours or nationalities. The outcomes of football matches can be considered to be ordinal (along with matches in other sports in which a draw is allowed). A home win is closer to a draw than it is to an away win. As such, there is a question of whether a scoring rule should take into account this ordering. A paper by Constantinou and Fenton argues that forecast probability placed on potential outcomes close to the actual outcome should be rewarded and therefore ordering should be taken into account ( _Constantinou and Fenton_ [2012]). Therefore, if the match outcome is a home win, probability placed on a draw should be rewarded more than probability on an away win. Scoring rules that have this property are referred to as being ‘sensitive to distance’. One scoring rule that has this property is the ranked probability score (RPS). Constantinou and Fenton therefore argue that the RPS is the appropriate score for the evaluation of probabilistic forecasts of football matches. As a result, the RPS has become perhaps the most popular and widely used scoring rule for this purpose. In this paper, the view that sensitivity to distance in a scoring rule is beneficial is disputed along with Constantinou and Fenton’s suggestion that the RPS should be widely used to evaluate football forecasts. 

Three scoring rules are considered in this paper: the RPS, which is both non-local and sensitive to distance, the Brier score, which is non-local but insensitive to distance and the ignorance score, which is local and therefore also insensitive to distance. It is argued that the ignorance score is the most appropriate out of these three candidate scores and evidence is presented in the form of two experiments demonstrating that the ignorance score is able to identify a set of perfect forecasts quicker than the other two scoring rules. 

The question of how probabilistic forecasts of discrete events should be evaluated is one with a long history. An early contribution to the literature was the introduction of the Brier score ( _Brier_ [1950]). The Brier score considers the squared distance between the forecast probability and the outcome for each possible category in which the outcome could fall (the category in which the outcome falls is represented with a one and all other categories with a zero). Whilst the Brier score is most commonly applied to binary events, it was originally formulated more generally such that it can be ex-


---

<a id="pdf-page-4"></a>

## PDF 第 4 页

[回查原始 PDF 第 4 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=4)

tended to events with more than two possible outcomes. The ignorance score ( _Good_ [1992]; _Roulston and Smith_ [2002]), often referred to as the logarithmic score, takes a different approach by simply taking the logarithm of the probability placed on the outcome. The rationale behind the ignorance score is in information theory and is closely related to other information measures such as the Kullback-Leibler Divergence ( _Br¨ocker and Smith_ [2007]). The ranked probability score ( _Epstein_ [1969]) is closely related to the Brier score but compares the cumulative distribution function of the forecast and the outcome rather than the probability mass function. Other proposed scoring rules include the spherical score, which combines the probability placed on the outcome with a correction term to ensure that it is proper ( _Friedman_ [1983]) and the quadratic score which simply takes the mean squared distance between the forecast and the outcome ( _Selten_ [1998]). This paper, however, is concerned only with the ignorance score, Brier score and RPS. These scoring rules were chosen because we are principally interested in the properties of locality and sensitivity to distance. The RPS is both non-local and sensitive to distance, the Brier score is non-local and insensitive to distance and the ignorance score is local and insensitive to distance (the ignorance score is in fact the only local and proper scoring rule ( _Bernardo_ [1979]). 

A range of other properties of scoring rules have been proposed, many of which have been suggested as desirable in some way. Propriety, as mentioned above is perhaps the most well known property and it stipulates that, in expectation, a scoring rule should favour the distribution from which the outcome was drawn over all others ( _Br¨ocker and Smith_ [2007]). Another property is locality. A score is local if only the probability at the outcome is taken into account ( _Parry et al._ [2012]). Other properties of scoring rules include those that are equitable, defined as those that ascribe the same score, in expectation, to constant forecasts as they do to a random forecast, regular, those that only ascribe an infinite score to a forecast that places zero probability on the outcome ( _Gneiting and Raftery_ [2007]), and feasible, those that assign bad scores to forecasts that give material probability to events that are highly unlikely ( _Maynard_ [2016]). 

A number of authors have commented on the value of sensitivity to distance in scoring rules. _Jose et al._ [2009] recommended the use of scoring rules that are sensitive to distance, including for forecasts of football matches. They provide generalisations of existing scoring rules to make them sensitive to distance. _Sta¨el von Holstein_ [1970] also recommended that scoring rules should be sensitive to distance and suggest a family of scoring rules based


---

<a id="pdf-page-5"></a>

## PDF 第 5 页

[回查原始 PDF 第 5 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=5)

on the RPS that also have this property. _Murphy_ [1970] compared the formulation of the RPS and the Brier score and recommended that the RPS should at least be used alongside the Brier score when the event of interest is ordered. _Bernardo_ [1979], on the other hand commented that “when assessing the worthiness of a scientist’s final conclusions, only the probability he attaches to a small interval containing the true value should be taken into account.” arguing for locality as a desirable property. 

There is a steadily increasing literature describing methodology for the construction of probabilistic forecasts of sporting events such as football matches ( _Diniz et al._ [2019]). In many of these, scoring rules have been deployed to attempt to assess the quality of those forecasts. For example, _Forrest et al._ [2005] use the Brier score to compare probabilistic forecasts derived from bookmakers’ odds and from a statistical model. _Spiegelhalter and Ng_ [2009] use the Brier score to assess the performance of their Premier League match predictions. The ranked probability score has also been widely used. For example, _Koopman and Lit_ [2019] use the RPS to evaluate their dynamic multivariate model of football matches, _Baboota and Kaur_ [2019] use the RPS to evaluate their machine learning approach to football prediction and _Schauberger et al._ [2016] use the RPS alongside cross-validation to select a tuning parameter in their model. The ignorance score appears to be less widely used than the Brier score and the RPS. _Diniz et al._ [2019] compare the performance of a number of predictive models using the ignorance score alongside the Brier score and the spherical score whilst it also has been used by _Schmidt et al._ [2008] alongside the Brier score to assess the probabilistic performance of a prediction market for the 2002 World Cup. 

This paper is organised as follows. In section 2, formal definitions of the scoring rules and their properties are given. In section 3, the arguments of Constantinou and Fenton are presented and disputed. In section 4, the question of how scoring rules are used in practice is discussed. The philosophical difference between a perfect and imperfect model scenario is discussed in section 5. The performance of the Brier score, Ignorance score and RPS are compared in a model selection experiment using examples from Constantinou and Fenton’s paper in section 6. A similar experiment is performed in section 7 using forecast probabilities derived from bookmakers’ odds of actual matches. Finally, section 8 is used for discussion and conclusions.


---

<a id="pdf-page-6"></a>

## PDF 第 6 页

[回查原始 PDF 第 6 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=6)

## **2 Background** 

### **2.1 Definitions of Scoring Rules** 

The three scoring rules considered in this paper are defined as follows. For an event with _r_ possible outcomes, let _pj_ and _oj_ be the forecast probability and outcome at position _j_ where the ordering of the positions is preserved. The Brier score, generalised for forecasts of events with _r_ possible outcomes, is defined as 


![PDF 第 6 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0006-03.png)

LaTeX 转写（对照上图，沿用原文符号）：

$$
\mathrm{Brier}=\sum_{i=1}^{r}(p_i-o_i)^2.\tag{1}
$$


The ranked probability score is defined as 


![PDF 第 6 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0006-05.png)

LaTeX 转写（对照上图，沿用原文符号）：

$$
\mathrm{RPS}=\sum_{i=1}^{r-1}\sum_{j=1}^{i}(p_j-o_j)^2.\tag{2}
$$


The ignorance score is defined as 


![PDF 第 6 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0006-07.png)

LaTeX 转写（对照上图，沿用原文符号）：

$$
\mathrm{IGN}=-\log_2\bigl(p(Y)\bigr)\tag{3}
$$


where _p_ ( _Y_ ) is the probability placed on the outcome _Y_ . 

### **2.2 Properties of Scoring Rules** 

Throughout a long history of research, a large number of properties of scoring rules have been defined. Here, those that are relevant to the arguments and experiments in this paper are described. 

Perhaps the most well known property of scoring rules is _propriety_ . A score is _proper_ if it is optimised, in expectation, with the distribution from which the outcome was drawn. As such, a proper scoring rule always favours a perfect probabilistic forecast in expectation. It is widely held that scoring rules that do not have this property should be dismissed ( _Br¨ocker and Smith_ [2007]). Each of the scoring rules described above are proper. A perfect probabilistic forecast is rarely, if ever, expected to be possible to achieve in practice. Therefore, in expectation, whilst a proper scoring rule will always rank a perfect forecast more favourably than an imperfect one, different proper scores will often rank pairs of imperfect forecasts differently. 

Another property of scoring rules is locality. A score is _local_ if it only takes into account the probability at the outcome. If any of the rest of the


---

<a id="pdf-page-7"></a>

## PDF 第 7 页

[回查原始 PDF 第 7 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=7)

distribution is taken into account by the score, it is non-local. The ignorance score is local whilst the Brier Score and RPS are both non-local. 

For discrete events, another property concerns whether the score takes into account the ordering of a set of potential outcomes. Scores that do this are defined as _sensitive to distance_ . For sporting events, for example, a draw and a home win can be considered to be closer together than a home win and an away win. An scoring rule that is sensitive to distance will therefore reward probability placed on an event closer to the actual outcome. Whilst the RPS is sensitive to distance, the ignorance and Brier Scores are not since they do not take into account the ordering of the possible outcomes. 

## **3 A Rebuttal of Arguments in Favour of the RPS** 

The popularity of the RPS for evaluating probabilistic forecasts of football matches is largely due to a paper written by Constantinou and Fenton, published in the Journal of Quantitative Analysis in Sports in 2012 ( _Constantinou and Fenton_ [2012]). The crux of the argument in that paper is that probability placed on potential outcomes ‘close’ to the actual outcome should be rewarded more than probability placed on those that are ‘further away’. If the home team is currently winning by one goal, it would take the away team to score one more goal for the match to end in a draw and two more goals for it to end in an away win and, therefore, the potential outcomes are, in a sense, ordered. The authors claim that, in light of this, only scoring rules that are sensitive to distance should be considered. A natural choice is therefore argued to be the RPS. 

With the aim of presenting further evidence towards the suitability of the RPS, Constantinou and Fenton define five hypothetical football matches, each with a specified outcome (i.e. a home win, a draw or an away win). For each match, they define a competing pair of probabilistic forecasts and use general reasoning to argue that, given the defined outcome, one is more informative than the other. They then show that the RPS is the only scoring rule out of a number of candidates that assigns the best score to their favoured forecast in each case, and argue that this provides evidence of its suitability. We dispute the validity of this reasoning. We argue that the approach by which the performance of the scores is compared under a specific outcome of


---

<a id="pdf-page-8"></a>

## PDF 第 8 页

[回查原始 PDF 第 8 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=8)

|Match|Forecast|p(H)|p(D)|p(A)|Result|‘Best’|Forecast|
|---|---|---|---|---|---|---|---|
|1|_α_|1|0|0|H|_α_||
||_β_|0.9|0.1|0||||
|2|_α_|0.8|0.1|0.1|H|_α_||
||_β_|0.5|0.25|0.25||||
|3|_α_|0.35|0.3|0.35|D|_α_||
||_β_|0.6|0.3|0.1||||
|4|_α_|0.6|0.25|0.15|H|_α_||
||_β_|0.6|0.15|0.25||||
|5|_α_|0.57|0.33|0.1|H|_α_||
||_β_|0.6|0.2|0.2||||





> 表格版面核对：以下截图保留原始单元格关系，合并单元格及复杂表头以截图为准。

![PDF 第 8 页表格原貌](./论文配图/wheatcroft-2019/wheatcroft-2019-p08-table-00.png)

Table 1: Match examples defined by Constantinou and Fenton. In each case, forecast _α_ is described as superior to forecast _β_ by the authors. 

the match is flawed. Instead, scores should be compared by considering the underlying probability of each possible outcome, thereby taking into account the underlying probability distribution of the match. This is a much more difficult task. 

To provide a setting with which to illustrate the arguments of Constantinou and Fenton and to provide counterarguments, details of the five hypothetical matches used as examples in that paper are reproduced. The outcome of each match, the two forecasts and an indicator of Constantinou and Fenton’s favoured forecast ( _α_ or _β_ ) are shown in table 3. 

The reasoning given by the authors for favouring each forecast is as follows. For match one, forecast _α_ predicts a home win with total certainty and must outperform any other forecast (including _β_ ). For match two, forecast _α_ places more probability on the outcome than forecast _β_ and therefore provides the most informative forecast. For match three, the only match in which the outcome is defined to be a draw, it is argued that, although both forecasts place the same probability on the outcome, forecast _α_ should be favoured because the probability placed on a home win and an away win are evenly distributed and therefore ‘more indicative of a draw’. For match four, it is argued that forecast _α_ should be favoured because, although both forecasts place the same probability on the outcome, _α_ places more probability ‘close’ to the home win, i.e. on a draw, than _β_ and therefore is more favourable. Finally, for match five, which is described as the most contentious


---

<a id="pdf-page-9"></a>

## PDF 第 9 页

[回查原始 PDF 第 9 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=9)

case, whilst _β_ places more probability on the outcome than _α_ , the authors argue that forecast _α_ is, in fact, more desirable than _β_ because it is ‘more indicative of a home win’ due to the greater probability placed on the draw. To provide further justification for favouring forecast _α_ , they give an example in which a gambler uses the forecast to inform a bet on the binary event of whether the match ends with any outcome other than an away win (commonly known as a lay bet). Since the sum of the probabilities on the home win and the draw are higher for forecast _α_ than for forecast _β_ , they suggest that _α_ is more desirable for that purpose. 

Our main counterargument to the reasoning of Constantinou and Fenton concerns their assertion that forecast _α_ outperforms forecast _β_ in each case. In fact, it is impossible to say which of the two forecasts should be preferred in each case without considering the underlying probability distribution of the match (which is unknown in practice). Consider match one. Here, they argue that forecast _α_ should be rewarded more than any other forecast since it predicts the outcome with absolute certainty. This seems entirely reasonable since no forecast is able to place more probability on the outcome. However, it does _not_ follow from this that _α_ is the best forecast. To illustrate this, consider the case in which _β_ represents the true underlying probability distribution of the match; i.e. the match will end with a home win with probability 0.9, a draw with probability 0.1 and an away win with probability 0. It is not contentious to state that _β_ is the best forecast in this setting and we argue that it would be deeply flawed to claim otherwise. Forecast _α_ should not be considered to be the best forecast simply because the match happened to end in a home win (which would happen with 90 percent probability in this case). In a succession of football matches in which the underlying probability is represented by _β_ and the forecast is _α_ , a draw would eventually occur, with forecast _α_ placing zero probability on that event. The same logic can be applied if the underlying probability distribution is represented by forecast _α_ , in which case, _α_ can objectively be considered to be the best forecast. In summary, without knowing the underlying probability distribution of the match, the answer to the question of which forecast is best can only be ‘it depends’. In practice, of course, it is never possible to know the underlying distribution and therefore we cannot distinguish the performance of the two forecasts on the basis of a single match. 

The effect of the probability distribution of the match on the favoured forecast under each score is now demonstrated. For a given probability distribution, the expected score of each of forecasts _α_ and _β_ are calculated, in order


---

<a id="pdf-page-10"></a>

## PDF 第 10 页

[回查原始 PDF 第 10 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=10)

|Colour|Ignorance|RPS|Brier|
|---|---|---|---|
|Green|_α_|_β_|_β_|
|Blue|_β_|_α_|_β_|
|Red|_β_|_β_|_α_|
|Turquoise|_α_|_α_|_β_|
|Brown|_α_|_β_|_α_|
|Purple|_β_|_α_|_α_|
|Yellow|_β_|_β_|_β_|
|Black|_α_|_α_|_α_|





> 表格版面核对：以下截图保留原始单元格关系，合并单元格及复杂表头以截图为准。

![PDF 第 10 页表格原貌](./论文配图/wheatcroft-2019/wheatcroft-2019-p10-table-00.png)

Table 2: Colour scheme for figures 1 and 2. 

to determine which is preferred by each scoring rule. This is repeated for a large number of randomly selected underlying probability distributions. This is demonstrated for match five in figure 1. Here, each dot represents a different probability distribution of the match with the probability of a home win and a draw on the _x_ and _y_ axes respectively. Each dot is coloured according to which of the two candidate forecasts is preferred under the three scoring rules. The colour scheme is defined in table 3. For example, if a point is coloured blue, the RPS prefers _α_ whilst the ignorance and Brier scores prefer _β_ under that distribution. Whilst the colour scheme might seem difficult to interpret at first, it becomes much clearer when it is considered that points coloured green, blue and red represent distributions in which only the ignorance, RPS and Brier score prefer _α_ and that the colours of overlapping regions are defined by mixing those colours. Note that, for this particular match, there are no green areas, that is there are no underlying distributions in which the ignorance score prefers _α_ and the RPS and Brier score prefer _β_ . 

The first conclusion to be drawn from figure 1 is that, clearly, as previously discussed, the forecast favoured by each scoring rule depends on the underlying probability distribution. Moreover, the choice of scoring rule impacts which of the two forecasts is preferred. We can look at each of the regions and try to understand how and why the three scoring rules differ. Consider the blue region in the bottom right of the figure. A point located in the very bottom right represents a probability distribution which places a probability of one on a home win and therefore zero on both a draw and an away win. Here, the RPS is the only score that favours _α_ over _β_ . This seems somewhat counterintuitive and can be argued to be a weakness of the scoring rule. Here, the RPS rewards probability placed on a draw, regardless


---

<a id="pdf-page-11"></a>

## PDF 第 11 页

[回查原始 PDF 第 11 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=11)

of the fact that that outcome _cannot_ happen. The cost of doing this is that, out of the two forecasts, the one that places less probability on the outcome is favoured. 


![PDF 第 11 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0011-01.png)


Figure 1: Randomly chosen probability distributions of match five coloured according to which forecast ( _α_ or _β_ ) is preferred by each of the three scoring rules. The colour scheme is described in table 3. 

The same information as shown in figure 1 for match five is shown for matches one to four in figure 2. This reinforces the importance of the underlying probability distribution and how the choice of forecast depends heavily on the scoring rule. 

In practice, scoring rules are usually used to assess the performance of forecasting _systems_ rather than individual forecasts. A forecasting system is a set of rules that is used to generate forecasts of different events in some common way. For example, a forecasting system might be built on the basis of


---

<a id="pdf-page-12"></a>

## PDF 第 12 页

[回查原始 PDF 第 12 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=12)

![PDF 第 12 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0012-00.png)


Figure 2: Randomly chosen probability distributions of matches one to four coloured according to which forecast ( _α_ or _β_ ) is preferred by each of the three scoring rules. The colour scheme is described in table 3. 

an individual model, a combination of models or the judgement of a particular person and can be applied to generate forecasts of a range of events (e.g. football matches). Forecasting systems are then evaluated by taking the average score over many events according to some scoring rule. This provides a basis with which to select a forecasting system for the prediction of future events. 

Before moving on, it is of interest to address two particular points made by Constantinou and Fenton in favour of forecast _α_ for match five. Firstly, they describe a situation in which the forecasts are used to inform a ‘lay’ bet on an away win. They argue that, since the combined probability placed


---

<a id="pdf-page-13"></a>

## PDF 第 13 页

[回查原始 PDF 第 13 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=13)

on a home win or a draw is higher for forecast _α_ than for forecast _β_ , _α_ is a better forecast, given this outcome. There is a simple counterargument to this. If a gambler intends to use the forecasts to make lay bets such as the one described, the resulting binary forecasts formed by adding the home win and draw probabilities should be evaluated separately. This is because the new binary forecasts take a different form and have a different aim. It does not makes sense during evaluation to attempt to pre-empt how the forecasts might be used to create other forecasts of a different nature. In fact, the original match outcome forecasts and the binary forecasts might even favour a different forecasting system. For example, one forecasting system might be poor at distinguishing a home win from a draw but good at estimating the probability of an away win. Tying one’s hands to create and use a one size fits all forecast seems unnecessary and counterproductive in this case. 

The second point of contention regards the ‘indicativeness of a home win’ in match five. The authors argue that despite the fact that forecast _β_ places more probability on the outcome than forecast _α_ , forecast _α_ is more indicative of a home win, due to the increased probability placed on the draw. It should be noted here that, were the probability on the draw reduced to 0.3 and the probability on the away win increased to 0.23, the RPS would favour forecast _β_ and thus the ‘indicativeness’ of a home win is somewhat arbitrary. 

The primary claim of Constantinou and Fenton is that probability placed on possible outcomes that are ‘close’ to the actual outcome should be rewarded more than probability placed on outcomes that are ‘further away’. Furthermore, they argue that the RPS provides a scoring rule that does this and is therefore suitable for evaluating forecasts of football matches. However, as described above, by not considering the underlying distribution of the match, it is not possible to state that one forecast is better than another and therefore the reasoning given in support of the RPS does not provide a compelling argument. We therefore consider the question of which forecast is assigned the best score, when conditioned on a single outcome, to be moot and we do not consider it further. Instead, we define potential goals of using scoring rules and ask whether the sensitivity to distance property offered by the RPS has any value in achieving them.


---

<a id="pdf-page-14"></a>

## PDF 第 14 页

[回查原始 PDF 第 14 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=14)

## **4 What are Scoring Rules For?** 

The principle intention of this paper is to assess the value of scoring rules that are non-local and sensitive to distance in the context of forecasts of football matches. In order to attempt to assess the merits of these properties, it is useful to consider the aims behind the deployment of scoring rules. For the properties of interest to have value, there should be some practical benefit in terms of achieving those aims. Here, we discuss the aims behind the application of scoring rules with a view to assessing whether the non-local and sensitivity to distance properties help to achieve them. 

One obvious aim of scoring rules is to provide a means of comparison between competing forecasting systems. There are many contexts in which one might want to make such comparisons. One might have a finite set of competing probabilistic forecasts of the same events and be looking to determine which is the most informative. For example, a broadcaster may want to decide which forecasts are most useful to show in its sports coverage or a gambler may wish to decide which forecasting service to subscribe to in order to aid their betting decisions. A means of comparison can also be important in the context of model development. A forecaster looking to improve the performance of their forecasting system by, for example, increasing the number of factors included in the model, may want to assess whether these changes result in improved forecasts. Parameter selection also falls under the umbrella of forecast comparison since each set of parameter values will lead to a different set of forecasts. Since parameters usually take continuous values, parameter selection can be considered to be a comparison between an infinite number of sets of forecasts. 

Whilst selecting one of two or more sets of forecasts may be considered to be important in a range of settings, this alone does not give an indication of the magnitude of the difference in skill. An additional question of interest concerns how much more informative one set of forecasts is over another and whether this difference is significant. Typically, two sets of forecasts are compared using the difference in their mean score ( _Wheatcroft_ [2019]). Resampling techniques can then be used to determine if that difference is significant. An interesting question concerns whether the difference in scores has an interpretation in terms of the relative performance of the forecasting systems of interest. In fact, to our knowledge, only one of the scoring rules considered in this paper has a useful interpretation when considered in this way and that is the ignorance score. The difference between the mean


---

<a id="pdf-page-15"></a>

## PDF 第 15 页

[回查原始 PDF 第 15 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=15)

ignorance scores of two forecasting systems represents the difference in information provided by each one expressed in bits. This means that calculating 2 to the power of the mean relative ignorance between forecasting systems one and two yields the mean increase in probability density placed on the outcome by the former over the latter. 

Whilst scoring rules are useful tools for evaluating and comparing forecasting systems, it is important to acknowledge their limitations. Often, a set of forecasts are used with a specific purpose in mind. In sports forecasting, this might be to aid a decision whether to place a bet on a certain outcome, whether to select a certain player for a match or which play to make during a game. It is therefore crucial to determine whether the forecasts are fit for that specific purpose. For example, a set of forecasts may successfully incorporate important information and therefore score better than alternative forecasts that do not incorporate this information yet still not be fit for a specific purpose. For example, using a set of forecasts to choose whether to place bets may result in a substantial loss which would have been avoided had the bets not been placed at all. 

## **5 Perfect and imperfect model scenarios** 

Philosophical approaches to the comparison of scoring rules typically consider two distinct settings: the perfect model scenario, in which one of the candidate forecasting systems coincides with the probability distribution that generated the outcome (often referred to as the data generating model (DGM)) and the imperfect model scenario, in which each candidate forecasting system is imperfect ( _Judd and Smith_ [2001, 2004]). In the perfect model scenario, there should be no ambiguity as to which set of forecasts is most desirable; a perfect forecasting system is always better than an imperfect one. In the latter, on the other hand, the ‘best’ forecasting system is subjective and the question of which one is the most desirable is also subjective. 

In the perfect model setting, there are two directly linked questions of interest. Firstly, ‘does the scoring rule always favour the perfect forecasting system in expectation?’ Scoring rules that do this are called proper and it is generally considered that a chosen scoring rule should have this property ( _Br¨ocker and Smith_ [2007]). As discussed in section 2.2, each of the three scoring rules considered in this paper are proper and thus they cannot be distinguished in this way. A closely linked means of comparison for scoring


---

<a id="pdf-page-16"></a>

## PDF 第 16 页

[回查原始 PDF 第 16 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=16)

rules assumes that each one is proper and assesses how many past forecasts and outcomes are required to have a given probability of selecting the perfect forecasting system. Requiring fewer forecasts and outcomes to do this means that the information is used more efficiently and therefore that there is a better chance of selecting the best forecasting system for future events. This observation forms the basis of the experiments presented in this paper. 

In practice, one can never expect any of the candidate forecasting systems to be perfect and therefore the perfect model case is generally accepted to be only a theoretical construct. It can nonetheless be argued that the performance of scoring rules in this context is important. If, in expectation, a scoring rule does not favour a perfect forecasting system over all others, one should be uneasy about the ability of that scoring rule to favour useful imperfect forecasting systems over misleading ones. Similarly, the efficiency in which a scoring rule uses the information in past forecasts and outcomes ought to tell us something about the way in which each scoring rule uses the information provided to it. For example, in the context of non-local scoring rules that are sensitive to distance, if these properties are truely useful, we might expect that that extra information should be capable of distinguishing perfect and imperfect forecasting systems more quickly. 

In practical situations, since none of the candidate forecasting systems are expected to be perfect, all exercises in forecasting system selection fall into the imperfect category. In this setting, unlike the perfect model case, proper scores will often favour different imperfect forecasting systems. Distinguishing the scoring rules is then a question of identifying which type of imperfect forecasts should be preferred. Other than the analysis demonstrated in figures 1 and 2, this question is left as future work. 

## **6 Experiment one - Repeated outcomes of the same match** 

In this experiment, the five pairs of forecasts defined by Constantinou and Fenton and shown in table 3 are used to assess the probability that each of the three candidate scoring rules identifies a perfect forecasting system over an imperfect one for a given number of past forecasts and outcomes. For a given pair of forecasts, define the outcomes of a series of _n_ matches by drawing from forecast _α_ or forecast _β_ with equal probability 0.5. Define two forecasting


---

<a id="pdf-page-17"></a>

## PDF 第 17 页

[回查原始 PDF 第 17 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=17)

systems as follows. The _perfect forecasting system_ always knows which of the two distributions from which the outcome is drawn and therefore always defines the correct distribution as the forecast. The _imperfect forecasting system_ , on the other hand, always issues the alternative distribution as the forecast. A scoring rule is defined to ‘select’ a forecasting system if it is assigned the lowest mean score over _n_ forecasts. The probability that each scoring will select the perfect forecasting system is calculated for different values of _n_ and the experiment is carried out using each of the forecast pairs in table 3. 

### **6.1 Results** 

Perhaps the most interesting of the five examples defined by Constantinou and Fenton is match five. Here, both forecast _α_ and forecast _β_ place similar probability on a home win but forecast _α_ places more probability on the draw. The probability of each scoring rule identifying the perfect forecasting system in this case is shown as a function of _n_ in figure 3. Here, the ignorance score outperforms both the Brier score and the RPS for almost every tested value of _n_ , whilst there is little difference in the performance of the Brier score and RPS. 

The results for matches one to four are shown in figure 3. For match one, the ignorance score clearly outperforms both the Brier score and the RPS for relatively large values of _n_ , whilst the difference is minimal for lower values. The non monotonic nature of the probabilities under the RPS and Brier scores may seem surprising at first but, in fact, can easily be explained. All three scoring rules punish the imperfect forecasting system when the outcome is a draw, since the forecast in this case predicts a home win with certainty. The overall probability of a draw for a given realisation is 0.05 since the probability that the outcome is drawn from _β_ is 0.5 and the probability of a draw given _β_ is 0.1. For all values of _n_ less than 20, once a draw has occurred, no combinations of other outcomes can result in the imperfect forecasting system being assigned a better mean score than the perfect forecasting system. When _n_ is greater than 20, on the other hand, the imperfect forecasting system can still ‘recover’ from such a situation as long as there is only one such occurrence. The probability for the ignorance score, on the other hand, is monotonic and this is because the ignorance score assigns an infinitely bad score to a forecast that places zero probability on an outcome. Therefore, once such a case has been observed, the imperfect


---

<a id="pdf-page-18"></a>

## PDF 第 18 页

[回查原始 PDF 第 18 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=18)

forecasting system cannot achieve a better score than the perfect forecasting system and, since the probability of observing such a case increases with _n_ , the probability is monotonically increasing. 

For match two, whilst the probabilities of selecting the perfect forecasting system are similar for each score, the ignorance score slightly outperforms the other two scores for all values of _n_ . In terms of the Brier score and the RPS, neither appears to be systematically better than the other. 

For match three, the ignorance score tends to outperform the other two scores for all _n_ greater than three, whilst, again, there is no obvious systematic difference between the performance of the RPS and Brier scores. For very small _n_ , the ignorance score achieves a lower probability of selecting the perfect forecasting system. However, caution should be applied in such cases since scoring rules are designed with a relatively large number of forecast pairs in mind, that is, if the aim were to apply them to small _n_ , they might be designed differently. 

Match four provides perhaps the most interesting results. In this case, _α_ and _β_ differ only in the probabilities placed on a draw and an away win. There is therefore only a small difference between the perfect and imperfect forecasting systems. This is reflected in the fact that the probability of choosing the perfect forecasting system increases relatively slowly with _n_ . Here, whilst the ignorance and Brier scores perform similarly well, there is a distinct advantage for both over the RPS. Whilst the RPS performs relatively well for low _n_ , the value of increasing _n_ is far lower than for the ignorance and Brier scores, i.e. the RPS does not make good use of the extra information provided by increasing the number of forecasts and outcomes. 

Overall, from these results, there is no evidence that the RPS outperforms either the Brier or ignorance scores and, in fact, there is some evidence that the opposite is true. The RPS does not typically make good use of additional sample members in comparison to the other two scores. Looking more closely at the results, the stark difference in performance in match four, and to some extent match five, suggests that the biggest difference in performance might be in cases in which the difference between the two candidate forecasts is relatively small and this observation provides a motivation for the design of experiment two. Experiment one considers only a case with repeated forecasts from one of two candidate distributions. In practice, there is usually interest in forecasts of different events rather than a large number of realisations of the same event. In experiment two, the performance of the three candidate scoring rules is compared in the context of forecasts of a wide


---

<a id="pdf-page-19"></a>

## PDF 第 19 页

[回查原始 PDF 第 19 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=19)

range of different football matches generated from actual bookmakers’ odds. 


![PDF 第 19 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0019-01.png)


Figure 3: Probability of each scoring rule selecting the perfect forecasting system as a function of _n_ for match 5. 

## **7 Experiment two - forecasts based on match odds** 

In experiment two, the aim is to assess the effectiveness of each scoring rule in terms of distinguishing a ‘perfect’ forecasting system from an ‘imperfect’ one in a more realistic setting in which each match has a different probability distribution. To do this, artificial pairs of forecasts are created in which one represents the true distribution and the other is imperfect. The aim is then to estimate the probability that each scoring rule selects the set of true distributions. 

To obtain sets of forecasts that are realistic in terms of actual football matches, bookmakers’ odds on past matches are used which are converted


---

<a id="pdf-page-20"></a>

## PDF 第 20 页

[回查原始 PDF 第 20 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=20)

![PDF 第 20 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0020-00.png)


Figure 4: Probability of each scoring rule selecting the perfect forecasting system as a function of _n_ for matches 1 to 4. 

into probabilistic forecasts. These are taken from the repository of football data at `football-data.co.uk` which supplies free-to-access data from a range of European leagues. Details of the data and how the odds are used to generate probabilistic forecasts are given in the appendix. Odds from a total of 39,343 matches are available and form the basis of a set of candidate probability distributions. We seek _n_ pairs of forecasts such that one represents the true distribution of the outcome, and therefore a perfect forecast, whilst the other represents an imperfect forecast. In order to test the effect of different levels of imperfection, we define a method of controlling it. To create a perfect forecast and corresponding outcome, a distribution is randomly drawn from the candidate set and defined to be the perfect forecast. A random draw from that distribution is then taken and defined to be the outcome. Next, we seek an alternative, imperfect forecast from the candidate set. Here, we apply a condition on the similarity of the candidate forecasts with the perfect fore-


---

<a id="pdf-page-21"></a>

## PDF 第 21 页

[回查原始 PDF 第 21 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=21)

cast. Let the perfect forecast be defined by _{ph_ , _pd_ , _pa}_ where _ph_ , _pd_ and _pa_ represents the forecast probability of a home win, draw and away win respectively. For each forecast in the candidate set, define the ‘distance’ from the true probability distribution to be 


![PDF 第 21 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0021-01.png)

LaTeX 转写（对照上图，沿用原文符号）：

$$
\epsilon=\frac{1}{3}\left(|\tilde p_h-p_h|+|\tilde p_d-p_d|+|\tilde p_a-p_a|\right).\tag{4}
$$


We define some threshold value _δ_ , find all forecasts for which _ϵ_ is less than _δ_ (excluding the perfect forecast itself) and randomly draw the imperfect forecast from that set. This process is repeated _n_ times such that there are a total of _n_ pairs of forecasts. We define the ‘perfect forecasting system’ to be the system that always issues the perfect forecast from the pair and the ‘imperfect forecasting system’ to be such that the alternative, imperfect forecast is always issued. The experiment is repeated for multiple values of _n_ and different levels of the parameter _δ_ , which governs the imperfection. 

### **7.1 Results** 

The effect of different levels of imperfection, governed by the selected value of _δ_ , is demonstrated in figure 5. Each blue dot represents a perfect forecast, with the _x_ and _y_ axes representing the probability of a home win and a draw respectively. The grey line links each of these with the corresponding imperfect forecast. Increasing the value of _δ_ tends to result in more distinct pairs of forecasts and therefore a higher level of imperfection. 

The proportion of forecast pairs in which the perfect forecasting system is selected over the imperfect forecasting system is shown for each score and value of _δ_ as a function of log2( _n_ ) in figure 6. The red, blue and green lines represent this proportion for the Brier score, Ignorance score and RPS respectively for the stated value of _δ_ . For higher levels of imperfection, that is when _δ_ is high, there does not appear to be much difference in the performance of the scoring rules. However, for the lowest level of imperfection, in which _δ_ = 0.1, there appears to be a notable difference with the RPS outperformed by both the ignorance and Brier scores. From this graph alone, however, it is not clear whether these differences are statistically significant. Given that each of the scores are calculated on the same sets of forecast pairs, the scoring rules can be compared pairwise with a total of three different comparisons (ignorance vs RPS, ignorance vs Brier and RPS vs Brier). These differences are shown as a function of log2( _n_ ) in figure 7, with each panel representing a


---

<a id="pdf-page-22"></a>

## PDF 第 22 页

[回查原始 PDF 第 22 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=22)

different value of _δ_ . The error bars represent 95 percent resampling intervals of the mean difference and hence, if the intervals do not contain zero, there is a significant difference in the performance of that pair of scoring rules. 

For the two lowest levels of imperfection ( _δ_ = 0.01 and _δ_ = 0.025), there is a clear hierarchy in terms of the efficacy of each score in identifying the perfect forecasting system. The ignorance score tends to outperform the Brier score which tends to outperform the RPS. This difference is most stark for larger values of _n_ . For the two larger levels of imperfection ( _δ_ = 0.05 and _δ_ = 0.1), the difference is less clear and, in general, there is no significant difference between the Brier score and the RPS. The ignorance score, on the other hand, still tends to perform significantly better than both other scores. These results therefore provide clear support for the ignorance score and little support for the RPS. 


![PDF 第 22 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0022-02.png)


Figure 5: Examples of forecast pairs for different levels of imperfection. The probability placed on a home win and a draw is represented by the _x_ and _y_ axes respectively. The grey lines join pairs of forecasts for the purpose of the experiment.


---

<a id="pdf-page-23"></a>

## PDF 第 23 页

[回查原始 PDF 第 23 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=23)

![PDF 第 23 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0023-00.png)


Figure 6: The proportion of cases in which the perfect forecasting system is selected by each scoring rule system as a function of log2( _n_ ) for different values of _δ_ . 

## **8 Discussion** 

The aim of this paper is to reopen the debate surrounding the use of scoring rules for evaluating the performance of probabilistic forecasts of football matches. The reasoning presented by Constantinou and Fenton supporting the use of the RPS over other scoring rules has been shown to be oversimplistic and the conclusion questionable. With this in mind, two experiments have been conducted with the aim of assessing the performance of each scoring rule in the context of identifying a perfect forecasting system using a finite number of past forecasts and outcomes. The ignorance score has been found to outperform both the RPS and the Brier scores whilst, to a lesser extent, the Brier score has been shown to perform better than the RPS in this context. 

The results in this paper may seem surprising at first. After all, both the Brier score and the RPS are non-local and take into account the entire


---

<a id="pdf-page-24"></a>

## PDF 第 24 页

[回查原始 PDF 第 24 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=24)

![PDF 第 24 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0024-00.png)


Figure 7: Pairwise differences in the proportion of cases in which the perfect forecasting system is selected between the ignorance and RPS (blue), ignorance and Brier score (red) and Brier score and RPS (yellow) as a function of log2( _n_ ) with 95 percent resampling intervals of the mean. 

forecast distribution rather than just the probability at the outcome whilst the RPS is sensitive to distance and therefore also takes into account the ordering of the potential outcomes. It would be easy to conclude from this that, since both scores take more of the distribution into account, they are more informative. However, it should be stressed that this would only be the case if those extra aspects are genuinely useful in terms of assessing the performance of the forecasts. In practice, we only ever gain limited knowledge regarding the true distribution, even once the outcome is revealed. If, for example, the outcome is a home win, this tells us little or nothing about the probability of a draw or an away win. In fact, knowing the outcome reveals relatively little about its probability, other than it is greater than zero. Given this, we argue that the probability placed on potential outcomes that didn’t happen are irrelevant. We know nothing about the true probabilities


---

<a id="pdf-page-25"></a>

## PDF 第 25 页

[回查原始 PDF 第 25 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=25)

and therefore cannot reward probability placed on such outcomes. On the other hand, we _know_ that the actual outcome occurred. Moreover, the more likely that event was deemed by the forecast, the better prepared we could have been for the occurrence of that outcome. We therefore argue that the probability placed on the outcome can be the only aspect of interest in evaluating probabilistic forecasts. Given that the ignorance score is the only proper and local score ( _Br¨ocker and Smith_ [2007]), this leads to it being a natural preference. 

In summary, this paper has both argued for and provided empirical evidence in favour of the ignorance score over both the Brier score and RPS. It should be noted, however, that this paper has only touched upon the question of which types of imperfect forecasts are favoured by different scores. Useful future work would be to attempt to understand better where different scoring rules favour different types of forecasts. A preference for the types of forecasts favoured by the Brier score or RPS would then need to be weighed up against the unfavourable results demonstrated in this paper. Regardless, we hope that the arguments and results in this paper are successful in reopening the debate surrounding the choice of scoring rule for evaluating forecasts of football matches. From the evidence presented in this paper, we strongly recommend the ignorance score for this purpose.


---

<a id="pdf-page-26"></a>

## PDF 第 26 页

[回查原始 PDF 第 26 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=26)

## **A Data** 

Experiment two makes use of bookmakers’ odds on actual football matches to form probabilistic forecasts. These odds are taken from the data set available at `www.football-data.co.uk` which supplies free-to-access match-bymatch data on 22 European Leagues dating back as far back as the 1993/1994 season. Here, data from the top five English leagues are used and are summarised in table 3. 

|League|First available season|Number of matches|
|---|---|---|
|English Premier League|2005/2006|6460|
|English Championship|2005/2006|6624|
|English League One|2005/2006|6624|
|English League Two|2005/2006|6624|
|English National League|2005/2006|6488|





> 表格版面核对：以下截图保留原始单元格关系，合并单元格及复杂表头以截图为准。

![PDF 第 26 页表格原貌](./论文配图/wheatcroft-2019/wheatcroft-2019-p26-table-02.png)

Table 3: Football league data used in this paper. 

## **B Match probabilities from odds** 

Let _Oh_ , _Od_ and _Oa_ be the decimal odds on a home win, draw and away win respectively for a given match. The multiplicative inverse of the odds on each outcome represents the ‘implied’ probability. However, due to the profit margin of the bookmakers, the implied probabilities will generally sum to a value greater than one. To remove the profit margin, the implied probabilities are divided through by their sum and therefore a probabilistic forecast is formed by 


![PDF 第 26 页原文图像（图形或公式）](./论文配图/wheatcroft-2019/2019_Wheatcroft_足球概率预测评分.pdf-0026-06.png)

LaTeX 转写（对照上图，沿用原文符号）：

$$
\begin{aligned}p_h&=\frac{1/O_h}{1/O_h+1/O_d+1/O_a},\\p_d&=\frac{1/O_d}{1/O_h+1/O_d+1/O_a},\\p_a&=\frac{1/O_a}{1/O_h+1/O_d+1/O_a}.\end{aligned}\tag{5}
$$


Forecasts are formed using the maximum odds (over all bookmakers given) in each case.


---

<a id="pdf-page-27"></a>

## PDF 第 27 页

[回查原始 PDF 第 27 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=27)

## **References** 

- Baboota, R., and H. Kaur, Predictive analysis and modelling football results using machine learning approach for english premier league, _International Journal of Forecasting_ , _35_ (2), 741–755, 2019. 

- Bernardo, J. M., Expected information as expected utility, _the Annals of Statistics_ , pp. 686–690, 1979. 

- Brier, G. W., Verification of forecasts expressed in terms of probability, _Monthly weather review_ , _78_ (1), 1–3, 1950. 

- Br¨ocker, J., and L. A. Smith, Scoring probabilistic forecasts: The importance of being proper, _Weather and Forecasting_ , _22_ (2), 382–388, 2007. 

- Constantinou, A. C., and N. E. Fenton, Solving the problem of inadequate scoring rules for assessing probabilistic football forecast models, _Journal of Quantitative Analysis in Sports_ , _8_ (1), 2012. 

- Diniz, M. A., R. Izbicki, D. Lopes, and L. E. Salasar, Comparing probabilistic predictive models applied to football, _Journal of the Operational Research Society_ , _70_ (5), 770–782, 2019. 

- Epstein, E. S., A scoring system for probability forecasts of ranked categories, _Journal of Applied Meteorology_ , _8_ (6), 985–987, 1969. 

- Forrest, D., J. Goddard, and R. Simmons, Odds-setters as forecasters: The case of english football, _International journal of forecasting_ , _21_ (3), 551– 564, 2005. 

- Friedman, D., Effective scoring rules for probabilistic forecasts, _Management Science_ , _29_ (4), 447–454, 1983. 

- Gneiting, T., and A. E. Raftery, Strictly proper scoring rules, prediction, and estimation, _Journal of the American Statistical Association_ , _102_ (477), 359–378, 2007. 

- Good, I. J., Rational decisions, in _Breakthroughs in statistics_ , pp. 365–377, Springer, 1992.


---

<a id="pdf-page-28"></a>

## PDF 第 28 页

[回查原始 PDF 第 28 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=28)

- Jose, V. R. R., R. F. Nau, and R. L. Winkler, Sensitivity to distance and baseline distributions in forecast evaluation, _Management Science_ , _55_ (4), 582–590, 2009. 

- Judd, K., and L. A. Smith, Indistinguishable states i: The perfect model scenario, _Physica D: nonlinear phenomena_ , _151_ (2-4), 125–141, 2001. 

- Judd, K., and L. A. Smith, Indistinguishable states ii: The imperfect model scenario, _Physica D: nonlinear phenomena_ , _196_ (3-4), 224–242, 2004. 

- Koopman, S. J., and R. Lit, Forecasting football match results in national league competitions using score-driven time series models, _International Journal of Forecasting_ , _35_ (2), 797–809, 2019. 

- Maynard, T., Extreme insurance and the dynamics of risk, Ph.D. thesis, London School of Economics and Political Science, 2016. 

- Murphy, A. H., The ranked probability score and the probability score: A comparison, _weather_ , _81_ , 82, 1970. 

- Parry, M., A. P. Dawid, S. Lauritzen, et al., Proper local scoring rules, _The Annals of Statistics_ , _40_ (1), 561–592, 2012. 

- Roulston, M. S., and L. A. Smith, Evaluating probabilistic forecasts using information theory, _Monthly Weather Review_ , _130_ (6), 1653–1660, 2002. 

- Schauberger, G., A. Groll, and G. Tutz, Modeling football results in the german bundesliga using match-specific covariates, 2016. 

- Schmidt, C., M. Strobel, and H. O. Volkland, Accuracy, certainty and surprise: a prediction market on the outcome of the 2002 fifa world cup, 2008. 

- Selten, R., Axiomatic characterization of the quadratic scoring rule, _Experimental Economics_ , _1_ (1), 43–61, 1998. 

- Spiegelhalter, D., and Y.-L. Ng, One match to go!, _Significance_ , _6_ (4), 151– 153, 2009. 

- Sta¨el von Holstein, C.-A. S., A family of strictly proper scoring rules which are sensitive to distance, _Journal of Applied Meteorology_ , _9_ (3), 360–364, 1970.


---

<a id="pdf-page-29"></a>

## PDF 第 29 页

[回查原始 PDF 第 29 页](./2019_Wheatcroft_足球概率预测评分.pdf#page=29)

- Wheatcroft, E., Interpreting the skill score form of forecast performance metrics, _International Journal of Forecasting_ , _35_ (2), 573–579, 2019.
