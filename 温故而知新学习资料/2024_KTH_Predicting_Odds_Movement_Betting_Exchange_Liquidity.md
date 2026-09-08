> **文献定位**：本论文收录于 [README 学习资料索引与经典论文导读](./README_学习资料索引与经典论文导读.md)，理论支撑 [心电图录像机](../脚本/心电图录像机.py) 与 [AGENTS 8层模型](../AGENTS.md)。

Degree Project in the Field of Technology Computer Science and Engineering and
the Main Field of Study Industrial Management
Second cycle, 30 credits
Optimizing Betting Strategies:
Utilizing Machine Learning to
Predict Odds Movement and
Maximizing Returns Based on
Technical Market Data
A Comparative Suitability Assessment for Machine Learning
Models in Predicting Odds Movement on Betting Exchanges
WILLIAM TOMCZAK

Optimizing Betting Strategies:
Utilizing Machine Learning to
Predict Odds Movement and
Maximizing Returns Based on
Technical Market Data
A Comparative Suitability
Assessment for Machine Learning
Models in Predicting Odds
Movement on Betting Exchanges
William Tomczak
Master’s Programme, Industrial Engineering and Management.
Master’s degree in Computer Science and Computer Engineering
Date: 2024-07-06
Supervisor: Arvind Kumar
Examiner: Pawel Herman
School of Electrical Engineering and Computer Science
Host company: 021 Edge AB
Swedish title: Optimering av spelstrategier: Användning av
maskininlärning för att förutsäga oddsrörelser och maximera
avkastning baserat på teknisk marknadsdata
Swedish subtitle: En jämförande lämplighetsbedömning av
maskininlärningsmodeller för att förutsäga oddsrörelser på spelbörser

IntroductionAbstract | 3
© 2024 William Tomczak

Abstract | i
Abstract
Betting exchanges constitute one area of the sports betting industry. A betting exchange is a
marketplace where individuals can bet against each other. The odds (probability of outcome) on
betting exchanges are therefore determined by the market, in this case several individuals. These
exchanges are therefore different compared to traditional sports betting, where bookmakers set the
odds and individuals can then choose to bet on the bookmakers’ odds.
The problem with betting exchanges is that the odds can fluctuate extensively and trends in the
liquidity on the betting exchanges influence the odds. The target is to make a comparative analysis
between state-of-the-art machine learning (ML) models to successfully indicate if the odds will
change and understand the impact on predictive performance between different levels of liquidity.
In addition, betting exchanges share similar characteristics as financial stock markets in terms of
pricing and liquidity, therefore financial trading formulas are implemented to assess the
performance of ML models more securely in the domain of betting exchanges.
There have been many different implementations for ML in the domain of sports betting, with
varying levels of performance. There are very few studies on the utilization of ML in the field of
betting exchanges. Related work in betting exchanges has been about building a trading algorithm.
This thesis takes an experimental approach and implement and evaluate state-of-the-art
solutions to understand the suitability of ML and financial trading formulas under different
amounts of liquidity in the field of betting exchanges.
The result in this study indicates that the predictive performance in general is very low and that
a financial trading algorithm performed better than the best ML algorithm for some classes, and
vice versa, ML algorithms performed better for classification on other classes. This result therefore
presents observations on when each respective model performs better and can establish a
foundation for future optimization of the models. However, this thesis cannot define with certainty
the most optimal model in predicting odds movements in betting exchanges.
Keywords
Sports betting, Odds prediction, Machine learning, Betting exchanges, Financial trading formulas

Sammanfattning | iii
Sammanfattning
Spelbörser utgör ett område inom sportbettingindustrin. En spelbörs är en handelsplats där
individer kan lägga spel mot varandra. Oddset (sannolikheten för ett utfall) på spelbörser bestäms
därav av marknaden, som i detta fall består av flera individer. Dessa spelbörser är därför skilda från
traditionella vadhållare, där vadhållaren sätter oddsen och individer kan välja om de vill spela på
dessa odds.
Problemet med spelbörser är att oddset fluktuerar kraftigt och trender i likviditet på spelbörsen
påverkar oddset. Målet med detta arbete är att genomföra en komparativ analys mellan
maskininlärningsalgoritmer och finansiella tradingformer för att framgångsrikt indikera om oddset
kommer att ändras. I tillägg kommer den prediktiva prestandan att jämföras baserat på olika nivåer
av likviditet på marknaden. Spelbörser har många likheter med aktiebörser i termer av prissättning
och likviditet, därav kommer finansiella tradingformer att implementeras för att grundligt och
säkrare förstå och bedöma prestandan för maskininlärningsmetoder inom spelbörser.
Flera implementationer med maskininlärning inom sportbetting har genomförts, där det även
framgår att maskininlärningsmetoder kan vara ett framgångsrikt verktyg för att öka vinster.
Däremot, finns det väldigt få studier inom spelbörser. Relaterade arbeten inom spelbörser har
främst utvecklat och implementerat tradingalgoritmer.
Detta arbete tillämpar en experimentell forskningsmetod, samt implementera och utvärdera
moderna maskininlärningsmetoder och finansiella handelsformler för att förstå lämpligheten under
olika nivåer av likviditet inom spelbörser.
Resultatet av denna studie indikerar att den prediktiva prestandan generellt är låg och att
finansiella handelsformler presterar bättre än maskininlärningsalgoritmer i vissa klasser och vice
versa, presterar maskininlärningsmetoder bättre för andra klasser. Resultatet lägger endast en
grund för framtida arbeten vad gäller att visa vilken modell som presterar bättre eller sämre. Detta
arbete kan inte med säkerhet avgöra vilken modell som är bäst på att förutspå oddsrörelser inom
spelbörser.
Nyckelord
Sportbetting, Odds prediktion, Maskininlärning, Spelbörs, Finansiella handelsformler

Acknowledgments | v
Acknowledgments
I want to thank Oskar Hansson for providing me the oppurtiounty to work on this project.
I also want to thank my supervisor and examiner at KTH for their support and freeing time from
their tight schedules.
Stockholm, July 2024
William Tomczak

Table of contents | vii
Table of contents
1 Introduction ......................................................................................... 1
1.1 Background....................................................................................................... 1
1.2 Problem ............................................................................................................. 1
1.3 Purpose and Problem Statement .................................................................... 2
1.4 Objectives ......................................................................................................... 2
1.5 Delimitations ..................................................................................................... 2
1.6 Structure of the thesis ..................................................................................... 3
2 Background ......................................................................................... 5
2.1 Odds and betting exchanges ........................................................................... 5
2.1.1 Odds .................................................................................................... 5
2.1.2 Betting Exchanges .............................................................................. 5
2.2 Predictive Modelling ......................................................................................... 6
2.3 Selection of Features for ML Models .............................................................. 7
2.4 ML Modelling Techniques ................................................................................ 8
2.5 Financial Trading Formulas ............................................................................. 8
2.6 Related work ..................................................................................................... 9
2.6.1 ML in Sports Betting ............................................................................ 9
2.6.2 ML in Betting Exchanges ................................................................... 10
2.6.3 Time Series Analysis in Betting Exchanges ...................................... 10
2.6.4 In-play Betting Predictions ................................................................. 10
2.6.5 Trading Software Tool in Betting ....................................................... 11
2.7 Summary ......................................................................................................... 11
3 Methods ............................................................................................ 13
3.1 Dataset ............................................................................................................ 13
3.1.1 Data Sampling ................................................................................... 13
3.1.2 Sample Size ...................................................................................... 13
3.2 Experimental Design ...................................................................................... 13
3.2.1 Data Pre-processing .......................................................................... 13
3.2.2 Vectorization...................................................................................... 14
3.2.3 Feature Selection .............................................................................. 15
3.2.4 ML Models ......................................................................................... 15
3.2.5 Financial Trading Formulas ............................................................... 16
3.2.6 Software ............................................................................................ 16
3.2.7 Hardware ........................................................................................... 16
3.3 Evaluation framework .................................................................................... 16
3.3.1 Datasets ............................................................................................ 16
3.3.2 K-fold Cross Validation ...................................................................... 17
3.3.3 Performance Metrics ......................................................................... 17
4 Results............................................................................................... 19
4.1 Model Performance ........................................................................................ 19
4.2 Liquidity Correlation ...................................................................................... 21
5 Discussion ........................................................................................ 24
Chapter 5 ................................................................................................. 24
Discussion ............................................................................................... 24

5.1 Performance and Evaluation ......................................................................... 24
5.2 Critical Reflections ......................................................................................... 25
5.2.1 Dataset .............................................................................................. 25
5.2.2 Optimization of Models ...................................................................... 25
5.2.3 Societal Impact and Relation to Literature ......................................... 25
5.3 Ethics and Sustainability ............................................................................... 26
6 Conclusions and Future Work ......................................................... 27
6.1 Conclusions .................................................................................................... 27
6.2 Future work ..................................................................................................... 28
References .............................................................................................. 29
Appendix A: Model Performance ........................................................... 31
Appendix B: Liquidity analysis .............................................................. 32

List of Figures | ix
List of Figures
Figure 2-1: Illustrative figure showing back and lay on an outcome of Draw. ............... 6
Figure 2-2: Screenshot from Betfair on the Market for Match Odds between
Manchester United and Everton ................................................................. 6
Listing 3-1: Structure of all market data for one timestamp ......................................... 14
Listing 3-2: Structure of only match odds data ............................................................ 14
Figure 4-1: This panel of figures demonstrates average accuracy, precision,
recall, and F-score for models implemented and the two feature
selection algorithms. Classification models are utilized on both feature
selection algorithms and the average of those is demonstrated. For
the feature selection algorithms, the average between all classification
models is demonstrated. A and B show normal liquidity, C and D
show the lowest liquidity, E and F show the highest liquidity, and G
and H show the markets with the highest liquidity. ................................... 20
Figure 4-2: This panel of graphs show average accuracy (graph A), precision (B),
recall (C), and F-score (D) for implemented models on the different
amounts of liquidity. The average for the two feature selection
algorithms is showed for all metrics and for all the models. ...................... 22
Figure 4-3: Performance of Random Forest for the different amounts of liquidity,
demonstrated per class. ........................................................................... 23
Figure 4-4: Performance of SMA for the different amounts of liquidity,
demonstrated per class. ........................................................................... 23

List of Tables | xi
List of Tables
Table 3-1: Vectorized variables from match odds data .............................................. 15
Table 3-2: Implemented ML models .......................................................................... 15
Table 3-3: Software used in project ........................................................................... 16

List of acronyms and abbreviations | xiii
List of acronyms and abbreviations
AI Artificial Intelligence
ML Machine Learning
MLP Multilayer Perceptron
RFE Recursive Feature Elimination
RSI Relative Strength Index
SMA Simple Moving Average
SVM Support Vector Machine

Introduction | 1
1 Introduction
Chapter 1
Introduction
This chapter describes the specific problem that this thesis addresses, the context of the problem,
the goals of this thesis project, and outlines the structure of the thesis.
This project is carried out in the area of sports betting, and in particular betting exchanges. The
thesis comprises a comparative analysis of best performing machine learning (ML) models for
predictive modelling in betting exchanges under different amounts of liquidity.
1.1 Background
Sports betting has for a long time been a popular entertainment, attracting millions of users with
global revenues of approximately 242 billion USD [1]. Sports betting refers to placing a monetary
wager on the outcome of a sporting event. These events can include the whole season or specific
events within a game [2]. A betting exchange is a revolutionary concept in sports betting. Betting
exchanges allow individuals to bet against each other instead of traditional betting against a
bookmaker. Bookmakers set their own odds where individuals can choose to bet against them. [3]
Betting exchanges therefore allow individuals to price the odds without the interference of
bookmakers and their margins.
Odds is a proxy for the probability of an outcome. The more accurate probability, the more
accurate odds [4]. Betting exchanges share similar characteristics as stock exchanges – both form
decentralized marketplaces where prices/odds are determined by users buying or selling [3, 5]. In
betting exchanges, it is possible to bet on an outcome (back) and bet against the outcome (lay).
Betting exchanges have shown high predictive accuracy [6, 7]. However, as mentioned the odds is
determined by the market and therefore limited liquidity can affect the market consensus of the
price and could in some cases wrongly reflect an accurate probability. Extensive amounts of data
enable the use of ML models and may thus be a useful way of predicting odds movement within
betting exchanges.
1.2 Problem
One problem with betting exchanges is that the liquidity in the market can be limited. The liquidity
within a market refers to the amount of money in the market and the available amount that can be
matched on the market. The liquidity depends on reasons such as popularity, media coverage and
the specific betting exchange.
This thesis has conducted research on Betfair market data. Betfair is the largest betting
exchange in the world. On highly liquid markets the odds have a higher possibility to reflect the
actual probability of an outcome [8].

2 | Introduction
Betting exchanges have higher liquidity closer to game start than, for instance, two weeks before
game start. Hence, trends in market liquidity have to be analysed to predict odds movement and
possibly indicate the most optimal timing for placing a bet on the exchange.
Betting exchanges share similarities with financial stock markets, however there are some
important differences. For instance, there can be many different markets within a single sporting
event and betting exchanges have a defined period of life. In general, financial stock markets are
more standardized compared to betting exchanges [8]. The similarity of financial stock markets and
betting exchanges therefore leads us to examine whether financial trading formulas will perform
better or worse than ML models in the domain of betting exchanges, and the effect liquidity may
cause.
1.3 Purpose and Problem Statement
The main purpose of this thesis is to investigate the use of ML in the domain of betting exchanges to
predict odds movement. In addition, this thesis contributes to the existing research within
adaptation of ML models in the domain of sports betting. In the thesis the application of financial
trading formulas to predict odds in real-time on betting exchanges is examined. Furthermore, both
financial trading formulas and ML models are evaluated with different amounts of liquidity.
This thesis makes valuable contributions to further research to understand if odds provided by
bookmakers are fair for individual bettors. The research aimed at answering the following research
questions:
1. How does liquidity affect the performance of ML models and financial trading formulas
in predicting odds movement in betting exchanges?
2. How do feature selection algorithms influence the performance of ML models?
1.4 Objectives
To successfully answer the research questions and create an understanding of the interplay between
liquidity, feature selection, and model performance these objectives were set:
1. Ensure that the relevant data is identified, cleaned, and pre-processed.
2. Evaluate the ML models and financial trading formulas’ performance in predicting odds
movements based on feature selection algorithm and liquidity.
3. Identify trends and observations from the results to deliver valuable insights.
1.5 Delimitations
The scope of this project does not include creating new models. It is a comparative analysis between
state-of-the-art models in the field of ML and financial trading formulas. The comparative analysis
does not cover all models available, rather just a few selected commonly used models. No interviews
were conducted – this project relies on existing literature and insights from the company
supervisor. The project is limited to analysing data within one betting exchange. It has not been
feasible to find the best possible parameter combination and therefore the aim is to create a
platform for further research and a direction towards the most optimal models and parameters. The
work did not implement a statistical significance analysis framework, but rather identifies trends
and observations from the results. Therefore, the results of this work do not suggest the most
optimal model.

Introduction | 3
1.6 Structure of the thesis
• Chapter 2: Background
Presents relevant information about the project and includes information about the domain of
betting exchanges and more extensively related work, and theory of the models that is tested.
• Chapter 3: Methods
Presents the implementation and method used to solve the problem.
• Chapter 4: Results
Presents the results from the thesis.
• Chapter 5: Discussion
Reasoning about aspects regarding the thesis, limitations, societal impact and ethics and
sustainability.
• Chapter 6: Conclusions and Future Work
Describes conclusions and reflections for future work.

Background | 5
2 Background
Chapter 2
Background
This chapter describes sports betting and betting exchanges. This chapter also covers ML models
and financial trading formulas. A description of related work within adoption of ML models and
financial trading formulas in the domain of betting exchanges and sports betting is included too.
2.1 Odds and betting exchanges
2.1.1 Odds
Odds ratio within sports betting is a proxy for the probability of an outcome [9]. There are three
main odds formats. Those are European format (decimal odds), UK format (fractional odds) and
American format (moneyline odds) [10, 11].
1. Decimal odds: Shows the ratio in decimal format between placed bet and the full
payout. It is calculated according to formula 1.
1
𝐷𝑒𝑐𝑖𝑚𝑎𝑙 𝑜𝑑𝑑𝑠= (1)
𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦
2. Fractional odds: Is the ratio between placed bet and win. 4:1 meaning that the win will
be 4x the wagered amount, demonstrated in formula 2.
𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦
𝐹𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑎𝑙 𝑜𝑑𝑑𝑠= (2)
1 − 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦
3. Moneyline odds: Has two possibilities, either negative or positive. Positive reflects the
win on the wagered amount, and negative expresses the stake needed to win 100 units.
Therefore +200 in Moneyline odds is equivalent to 2:1 in fractional odds and -200
equals 1:2 in fractional odds.
In the area of sports betting bookmakers craft their own odds and offer them to bettors. The
bettors can only back the odds, thus the bookmaker lays the odds. When bookmakers set their odds
they factor in a margin to ensure they will be profitable in the long run [12].
2.1.2 Betting Exchanges
There are multiple betting exchanges with examples such as Betfair, Betdaq and Smarkets. Betfair is
the largest and the most well-known one. Betting exchanges are platforms where individual bettors
can both back and lay against each other, totally decentralized from a bookmaker. The odds on the
market is based on the opinions of individual bettors, and generally groups of individuals vary more
than bookmakers and therefore, the odds on betting exchanges are mostly more beneficial for
bettors [8].

6 | Background
Figure 2-1 demonstrates how betting exchanges work. Betting exchanges allow individuals to
offer back or lay on certain odds for a specific market. A betting exchange works as an intermediator
where individuals can offer their odds to others, where the betting exchange takes a commission on
the win. Betfair usually takes 5% in commission [13]. Figure 2-1 demonstrates how this works. In
this case the odds (decimal) are 2,0 respectively for both back and lay on draw in this illustrative
game. Liability refers to the amount that is at risk of being lost. Lay options have a higher liability
because they bet against this outcome and consequently cover all the other possible outcomes.
Figure 2-1: Illustrative figure showing back and lay on an outcome of Draw.
Figure 2-2 is a screenshot from Betfair that shows a Premier League game between Manchester
United and Everton. Each sporting game has many different markets shown as “Available Markets”.
The liquidity can vary substantially between markets within a game, but match odds almost every
time have the most liquidity. Every game has different selections shown as “Selections”, where
bettors can make their pick. “Back overround” and “Lay overround” refers to the amount of money
that will be won or lost if every selection is backed respectively lay. A value of 100,9% therefore
implies an overround of 0,9%.
Figure 2-2: Screenshot from Betfair on the Market for Match Odds between Manchester United and Everton
2.2 Predictive Modelling
Predictive modelling refers to the process of creating a mathematical model that generates a
prediction. To create predictive models, it is crucial to have historical data to successfully predict
future cases. The big interest with predictive modelling is to accurately predict the changes that
something will occur or not occur [14].

Background | 7
There are many common reasons why predictive models is not performing well [14]:
1. Lacking pre-processing of data
2. Faulty model validation
3. Unjustified extrapolation, which refers to use of the model on data that is within a space
which the model has not ever been trained on
4. Over-fitting the model to specific dataset
The goal with predictive modelling is to successfully create a mathematical function that
calculates the relationship between future values and the target variable. The target variable can be
both categorical and continuous, which is termed as classification respectively regression [15]. For
datasets where the target variable is known and there is an extensive set of pre-labelled data,
supervised ML is a common method to use in predictive modelling. The algorithm then learns on
the dataset and how the model should predict the target variable [16]. Later this model is applied on
the unseen data, which is the part that is evaluated.
There are many factors involved that determine the most appropriate modelling technique to
produce the best results. Data complexity and volume are important factors to scrutinize. There are
algorithms that perform better on large datasets and those that perform better on small sets of data.
Furthermore, some algorithms perform better on complex datasets than others [17]. One way to
understand and evaluate the performance of an algorithm to a dataset is to use cross-validation.
Cross-validation is a widely used data resampling method that helps assess the predictive models
generalization ability and prevent the model from overfitting [18, 19]. One commonly used
technique is k-fold cross-validation, this method divides the whole datasets into subsets. The model
is trained on k -1 subsets and the remaining 1 subset is referred to as validation set, meaning that
the model is evaluated on the validation set. This process is redone k times and every time with a
new validation set, which means it can help prevent overfitting and successfully determine the
performance of the model [20].
2.3 Selection of Features for ML Models
It is important that features with more significant information are used when creating predictive
ML models. The performance and effectiveness of the model can be increased by selecting
appropriate features.
When the feature vectors are large, the learning process becomes significantly slower and the
model is more likely to overfit [21]. It is important to both keep the dimensions appropriate and not
include irrelevant information – these aspects are therefore important for efficiency and
performance. There are many feature selection algorithms available, however some are very
extensive and intractable [22]. Applying feature selection algorithms may also increase data
understanding and visualize the data, meaning that it can help understand what data is rewarding to
collect in the future [23].
The extensive amount of feature selection algorithms can be generalized to three types of
algorithms; filter model, wrapper model, and hybrid model [24].
Filter algorithms work by searching through the feature space and evaluate every subset with an
independent measure and compares this subset to the previously best subset. Because filter
algorithms evaluate every subset independently there can be no problem with inherited bias, in
addition these algorithms are also computationally efficient. Wrapper algorithms are similar to filter
algorithms, however these do not have an independent measure – they adopt a mining algorithm
[24]. Wrapper algorithms tends to perform better, however it is computably more costly and more
likely to overfitting [25]. Hybrid algorithms combine the methods from filter and wrapper. It uses

8 | Background
an independent measure to evaluate every subset and a mining algorithm to successfully choose the
best feature subset. The hybrid model is more relevant when there is a more complicated and large
dataset [24].
2.4 ML Modelling Techniques
There are many different ML models, where each model has its advantages and disadvantages. The
purpose of ML models is to find correlations and patterns inside a dataset and depending on the
dataset and the application of the ML models, some perform better than others.
Decision trees is supervised learning method used for classification and regression problems.
Decision trees use a recursively splitting technique on the input data that is based on features and
hence create a tree-like structure. Decision trees are non-linear and continues to be refined and
more specific the further the depth of the three. Decision trees can overfit, and therefore techniques
such as pruning may be needed [26]. Random Forest is also a classification model that can be used
to select the optimal parameter value from each node within the decision tree, which helps with
overfitting, for example, by using a random selection of features [27].
Support Vector Machine (SVM) is a commonly used technique in classification problems. SVM
identifies the most optimal hyperplane, that best can separate two categories within a dataset. SVM
can be linear or a hyperplane. This hyperplane has decision boundary referred to as margin, that
makes the model successfully determine if a specific datapoint corresponds with the positive or
negative class. Therefore, to maximize performance of the model it needs to successfully determine
the most optimal hyperplane that maximizes the margin [28].
Artificial neural networks (ANN) are widely used for both classification and regression
problems. ANNs are composed of interconnected nodes (“neurons”) arranged in layers. These layers
are input, hidden, and output, from which these form the network. ANN is a non-linear model, and
each node connection is associated with a weight and these weights are continuously improved to
maximize the precision [29]. Multilayer Perceptrons (MLP) is one form of ANN that is frequently
used in ML. MLP is trained on supervised learning and there are multiple important parameters
such as learning rate, number of hidden layers etc., which are crucial to consider when designing the
model [30].
2.5 Financial Trading Formulas
There are numerous financial trading formulas where two of the most widely used formulas are
Simple Moving Average (SMA) and Relative Strength Index (RSI) [31, 32].
SMA is calculated by:
𝑆𝑀𝐴 = 1 ∑𝑘 𝑃 (1)
𝑛 𝑛 𝑡=𝑘−𝑛+1 𝑡
The variable n stands for the number of periods considered for the average, k denotes the
current period’s relative position and lastly P is the price at the given time t. SMA smooths out price
t
fluctuations to better understand trends in the data. If the current price is above SMA it implies that
the price is trending to higher prices, and respectively, if it is lower, the trend suggests that the price
is trending downwards [31].
RSI is calculated by:
𝑅𝑆𝐼 =100− 100 / (1+ RS) (2)

Background | 9
RS is the average gain divided by the average loss. The average gain and the average loss are
calculated by the sum of gains over the past n periods and the sum of losses over n periods. If the
value of RSI is larger than 70 it implies that the asset is overbought and if the value of RSI is lower
than 30 it implies that the asset is being oversold [32].
SMA and RSI are both used in stock markets as technical analysis formulas. They are used to
identify trends and give indication of when an asset should be sold or bought on the stock exchange.
SMA weighs each period equally, therefore assuming that older prices are justly as interesting as
more recent prices. This is also a limitation compared to other adaptive models or formulas because
some other adaptive formulas such as Adaptive Moving Average (AMA) can automatically change
the length of the average. Therefore it could theoretically respond better to changing market
circumstances based on for example the extent of volatility on the market [31].
RSI is a momentum oscillator that calculates price movements and the speed and change of it. It
is one of the most popular and frequently used technical indicators for momentum. In the stock
exchanges RSI uses days as periods meaning that it calculates the gains or loss during a full trading
day. It can be used for short term trading, for example 9 days, or long term investments where for
example 100 days may be used [32].
2.6 Related work
Relevant literature and previous studies are analysed.
2.6.1 ML in Sports Betting
ML in the field of sports betting is not something new – many studies have been conducted in this
area. Already in 1996 Purucker [33] introduced an artificial neural network (ANN) that was created
to determine the most superior team to predict results in the American National Football League.
The accuracy from Purucker study was 61% and it emphasizes the importance of feature selection to
successfully build efficient models. This study was very early, and the dataset was limited, however
it showed the potential of using ML in the fields of sports betting.
Another study conducted in 2008 by McCabe et al. [34] implemented Multilayer Perceptron
(MLP) with both backward propagation and conjugative gradient descent. They implemented this in
four different sports where the best average accuracy was almost 68%.
Furthermore, in a study conducted 2010 by Huang et al. [35] they predicted the probability for
two teams to win the game using MLP and backward propagation with binary classification. This
study accomplished an impressive accuracy of about 77%.
Also in 2010 Miljković et al. [36] implemented the classification algorithms Naive Bayes,
Decision trees, K-nearest neighbours and SVM. They used feature selection techniques and
normalization to improve the results. The dataset contained National Basket Association (NBA)
games and the best performing algorithm was Naïve bayes, which achieved 67%.
The previously mentioned studies highlight the fact that ML in sports betting perform well,
however other authors of studies such as Štrumbelj [37] suggest that the chosen model is not the
most important dimension in achieving high accuracy. The most important was how the data
attributes were being handled and computed. The implemented feature selection and normalization
techniques to achieve higher prediction accuracy for ML models.

10 | Background
2.6.2 ML in Betting Exchanges
From what can be found, there are very few studies on adoption of ML in the domain of betting
exchanges. However, there are some studies on outcome and price movements.
Santos [38] implemented a trading agent that utilizes ML to improve the performance at horse
racing markets within a Betfair betting exchange. The results showed a significant improvement
when ML was implemented, however in the long run the trading agents still made a loss. Santos’s
work focused on market fluctuations and tried to back and lay simultaneously at moments where
the odds increase or decrease, and if the odds are priced correctly, it will guarantee a win. However,
the problem was that in some cases the odds could not be matched because liquidity was not
sufficient at certain odds, and therefore the trading algorithms could not deliver a profit in the long
run.
In 2008 Øvregård [39] examined the use of an in-play trading algorithm at betting exchanges
for tennis markets. The researcher implemented multiple Artificial Neural Networks (ANN) to
create a profitable trading algorithm. In addition, he implemented a custom cost function, which
was benchmarked against standard cost functions. The data parameters that were used included the
amount to be matched on both back and lay for both players, plus the back and lay price at every
time segment. With the implementation of the custom cost function Øvregård achieved a yield of
about 0,21%, showing the potential of ML in betting exchanges.
Another important related work was conducted by Dzalbs et al. [40] where the authors
implemented Cartesian Genetic Programming (CGP) and ANN to forecast price movements within
betting exchanges and especially in horse racing markets. They used this information to create a
trading algorithm and they successfully achieved a Return on Investment (ROI) of 83% during a
historical period of one month.
Lastly, In 2019 Gonçalves et al. [41] implemented a short-term forecasting system to predict
price movements within a Betfair betting exchange. The authors implemented Deep NN Classifier
(DNNC), Long Short-Term Memory (LSTM) and Convolutional NN (CNN) to predict the odds
movements before race start on horse racing markets. In addition, they also implemented an
automated trading algorithm, that resulted in profits for all models during a 30-day period, where
CNN achieved the highest profit.
2.6.3 Time Series Analysis in Betting Exchanges
There has also been related work that includes studies about time series analysis in betting
exchanges. One example is the study made by Bunyan [42] in 2014 where he implemented time
series analysis to forecast the winner with in-play odds within a betting exchange. The result from
this study showed an accuracy of less than 20%. They used linear regression, Gausiann Processes
and SMOreg (Support Vector Machine).
2.6.4 In-play Betting Predictions
There have also been studies in predicting in-play outcomes, mainly in tennis. Klaassen et al. [43]
already in 2001 implemented a method to forecast the winner of a tennis mach. They proposed a
statistical analysis method to calculate probabilities based on information before the game and
during the game, such as who is serving and who won the earlier point.
In 2012 Madurska [44] further investigated a mathematical method to predict the outcome for a
tennis match, on a set-by-set analysis. The author implemented Markov-chains to perform the
prediction and implemented the method for a trading algorithm. The results successfully achieved
an ROI of 19,6%.

Background | 11
In 2017 Bebbington [45] investigated in-play price fluctuations on horse racing markets and
implemented a statistical arbitrage betting algorithm to trade in-play. The author’s conclusion was
that the market was efficient in pricing the statistical probability of an outcome, especially initial
odds on the top ranked horses. However, the market was not as efficient in pricing odds on the low
ranked horses.
2.6.5 Trading Software Tool in Betting
In 2014 Tsirimpas developed an automated trading software tool for betting exchanges. To the
author’s knowledge there was not a publicly available trading research platform like the one they
developed. The aim with automated trading software is that users can create their own strategies
and back-test the solutions to understand how the strategy will perform in action [8]. This work
shows that even though there has been research in sports betting prediction, betting exchanges are
still relatively new.
2.7 Summary
This chapter presented relevant information of the space of betting exchanges, relevant methods to
implement, and how these methods can be evaluated.
Relevant reference work was presented. An extensive number of studies in the field of ML in
sports betting have been performed, although very few in the area of betting exchanges. The dataset
is also completely different since ML in the field of sports betting in general use historical data from
the teams to determine the chance of winning. In contrast, this study focuses only on the betting
exchange and potential price movements based on trends in liquidity and odds.
To the best knowledge of the author, soccer odds and price movements in betting exchanges
have not been investigated.

Methods | 13
3 Methods
Chapter 3
Methods
Section 3.1 focuses on the dataset used for this research. Section 3.2 describes the experimental
design. Finally, Section 3.3 describes the framework selected to evaluate the ML models and
financial trading formulas.
3.1 Dataset
The data has been given by the host company and they retrieved the data from Betfair. This section
explains the dataset.
3.1.1 Data Sampling
The dataset contains about 50 different categories of datapoints, but this project focuses on the
variables that are linked to the odds, this work therefore only focuses on the betting exchange
specific information such as liquidity, price, etc.
3.1.2 Sample Size
The dataset contains data from May and June of 2020 on ~700 soccer match odds markets (winner
of soccer game) and between ~250 to ~20,000 timestamps for every minute where it has been a
market change. The data contains information with specific market data for every market (such as
liquidity, price etc.). There is a difference between the number of timestamps, since every market
had different amounts of changes in the market based on the number of bets (both back and lay)
and intensity.
3.2 Experimental Design
This section describes relevant areas and procedures to recreate the work of this thesis.
3.2.1 Data Pre-processing
The dataset is large and contains large amounts of data, which needed pre-processing. The match
odds were identified with a unique id. Every market change was recorded for every minute, if
changes were recorded in other markets such as half-time outcomes or number of goals. These
changes were also nested in the data corresponding to a unique timestamp demonstrated in
listening 3-1. Therefore, every row had to be iterated and information retrieved for the id:s
corresponding to the match outcome, demonstrated in listing 3-2. These were later inserted into a

14 | Methods
new Sqlite database in which the data was labelled. The labelling was done by looking at the
previous price (both for back and lay). The data was then classified with “2” if the price had
increased, “1” if the price was unchanged and “0” if the price had decreased.
Listing 3-1: Structure of all market data for one timestamp
[{"id": "1.170483492", "rc": [{"trd": [[1.21, 177.39]], "batl": [[0, 1.21, 31.01]], "ltp": 1.21, "tv":
252.73, "id": 5851483}], "tv": 270.2},
{"id": "1.170483504", "rc": [{"batb": [[0, 1.98, 172.05], [1, 1.97, 69]], "ltp": 1.94, "tv": 4729.0,
"id": 1222344}]},
{"id": "1.170483502", "rc": [{"trd": [[40, 4.54]], "batl": [[0, 40, 30.92]], "ltp": 40.0, "tv":
18.41, "id": 6}, {"trd": [[8.2, 5.72]], "batb": [[0, 8.2, 4.91]], "ltp": 8.2, "tv": 165.73, "id": 3}], "tv":
821.31},
{"id": "1.170483499", "rc": [{"batl": [[1, 85, 3.35]], "ltp": 80.0, "tv": 47.56, "id": 11}]},
{"id": "1.170483577", "rc": [{"trd": [[22, 8.92]], "batb": [[0, 22, 2.29]], "ltp": 22.0, "tv": 21.66,
"id": 6251142}], "tv": 417.89},
{"id": "1.170483497", "rc": [{"batb": [[0, 6, 14.37]], "ltp": 7.2, "tv": 127.31, "id": 367577}]}]
Listing 3-2: Structure of only match odds data
{"trd": [[4.2, 3.88], [4.3, 20.6]],
"batl": [[0, 4.3, 18.63], [1, 4.8, 18.51], [2, 85, 24.15]],
"ltp": 4.3,
"tv": 26.48, "
totliq": 61.29}
3.2.2 Vectorization
After the data pre-processing, the information regarding the match odds had to be vectorized. The
approach that was used was to vectorize every datapoint associated with the price, such as liquidity,
availability to back and lay etc., demonstrated in table 3-1 and listing 3-2. The dimensionality of the
vectors became 42.

Methods | 15
Variable Description
The total amount traded on the market
tv
(accumulative)
ltp Last traded price
Bet available to back, three best odds and
batb
respective volume: [price, volume]
Bet available to lay, three best odds and
batl
respective volume: [price, volume]
Trades – a list with the trades at the time
trd
[price, volume]
Total liquidity to be matched on both back and
totliq
lay
Table 3-1: Vectorized variables from match odds data
3.2.3 Feature Selection
Section 2.3 shows that it is beneficial to use feature selection algorithms. This work implemented
both a filter algorithm and a wrapper algorithm. The feature selection algorithms chosen were Chi-
square test and Recursive Feature Elimination (RFE) with Random Forest estimator.
Both feature selection algorithms were executed in all datasets. The Chi-square test
demonstrated that all the features were statistically significant, with a significance level of a lower p-
value than 0,05. This indicates that the relationship between the independent variables and the
dependent variables (outcomes) is unlikely to occur by chance.
RFE was utilized with 5 selected as n. This was chosen because a low dimensionality vector
could be evaluated. As mentioned, Chi-square demonstrated that all features had statistical
significance, therefore the vectors with the whole set of features were evaluated as well.
3.2.4 ML Models
The ML models were implemented and evaluated on all the different datasets with both feature
selection algorithms. All the models are listed in table 3-2.
ML model Feature selection
Random forests Recursive feature elimination (RFE)
Random forests Chi-squared test
Support vector machine (SVM) Recursive feature elimination (RFE)
Support vector machine (SVM) Chi-squared test
Multilayer perceptron (MLP) Recursive feature elimination (RFE)
Multilayer perceptron (MLP) Chi-squared test
Table 3-2: Implemented ML models

16 | Methods
These models were chosen because they include the most used ML algorithms so that a solid
comparative analysis can be made. In section 2.8 it was also shown that these models have been
successfully implemented earlier in sports betting.
3.2.5 Financial Trading Formulas
Two financial trading formulas were implemented to further understand and compare the
performance of the ML models. The financial trading formulas used:
1. Simple Moving Average (SMA)
2. Relative Strength Index (RSI)
These are widely used technical indicators, yet simple. They therefore provide good supporting
information to truly understand whether the ML models have superior performance. As previously
mentioned in section 2.5, these models only indicated when to buy or sell, requiring the models to
be adjusted into a classification model.
SMA was implemented with an n of 10, meaning that it calculated the average price of the 10
prior datapoints. If the current price was higher or lower than the average it would classify as an
increase respectively decrease. If the price was the same, it would classify as unchanged.
RSI followed a similar approach. However, it calculated the average gain and average loss of the
14 last periods. Then, if the RSI value was over 70 or under 30, it classified as an increase
respectively decrease, while other values were classified as unchanged.
3.2.6 Software
To successfully conduct the experiment, the software shown in table 3-3 was used.
Name Type Use case
Python Programming Language Build/run the program
Pandas Software library Data handling/analysis
Scikit-learn Software library ML models
Sqlite3 Database Store all the data
Table 3-3: Software used in project
3.2.7 Hardware
A standard personal computer was used to train and evaluate the models. Therefore, the process
was significantly time consuming. The specification of computer is irrelevant for this work.
3.3 Evaluation framework
3.3.1 Datasets
Four different datasets were created to be able to successfully compare performance and answer the
research question, and these where:
1. 100 different games without filtering the data.
2. Only kept the specific data where the liquidity was over the average for that market.

Methods | 17
3. Only kept the specific data where the liquidity was under the average for that market.
4. Only kept markets where the liquidity was in the upper 25% percentile.
All the models were trained and evaluated on every dataset.
3.3.2 K-fold Cross Validation
It is important that the ML models are not overfitted and that the model’s generalization ability is
tested.
The data was divided into three subsets: training (80%), validation set (10%) and test set (10%).
In addition, K-fold cross validation was implemented with 10 splits to assure that the models’
performances were correctly validated.
Regarding the financial trading formulas there was no need to train the method since they did
not have parameters that needed to learn from the data.
3.3.3 Performance Metrics
The performance of a classification model can be evaluated using accuracy, precision and recall:
[46].
1. Accuracy: Number of correct predictions compared to the total predictions.
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒+𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒
𝐹 = (1)
𝑇𝑜𝑡𝑎𝑙 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠
2. Precision: Number of true positive predictions in ratio to classified positives.
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= (2)
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒+𝐹𝑎𝑙𝑠𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒
3. Recall: True positives in ratio to all actual positives.
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒
𝑅𝑒𝑐𝑎𝑙𝑙 = (3)
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒+𝐹𝑎𝑙𝑠𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒
4. F-score: is the harmonic mean of Recall and precision, calculated according to formula
1.
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 x 𝑅𝑒𝑐𝑎𝑙𝑙
𝐹 =2 x (4)
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
These four key metrics are therefore used to evaluate both the ML models and the financial
trading formulas. These help us understand and assess the performance of the models. It is
important to understand the performance, since if poor, incorrect information may affect decision
making negatively, and therefore also become costly in the application of sports betting. In addition,
the said metrics were also calculated for the individual classes for every model, meaning that the
prediction can be evaluated with understanding, if some class distorts the result. Lastly, the
performance of the models based on the dataset, was compared to understand the impact of
liquidity. Chance level accuracy can be interpreted as the share of labels in the majority class;
therefore it can be benchmarked against the performance of the models.

Results | 19
4 Results
Chapter 4
Results
This section is divided into two parts: The model performance for all datasets and the correlation
between performance and liquidity.
4.1 Model Performance
The classification performance is displayed for four different datasets:
1. 100 Games without filtering. (normal liquidity)
2. Filtering based on liquidity below average. (lowest liquidity)
3. Filtering based on liquidity over average. (highest liquidity)
4. Filtering based on markets where the liquidity was in the upper 25% percentile.
(markets with highest liquidity)
These four datasets are analysed to understand whether the performance is higher under certain
amounts of liquidity. Each classification model is evaluated according to the different datasets and
demonstrated independently. The ML models evaluated include Random Forest, SVM, MLP. The
financial trading formulas evaluated are RSI and SMA. Feature selection algorithms RFE and Chi-
squared are also evaluated.

20 | Results
A B
80%
60%
60%
40%
40%
20%
20%
0% 0%
Random SVM MLP RSI SMA RFE Chi-squared
Forest
Accuracy Precision Recall F-score Accuracy Precision Recall F-score
C D
80%
60%
60%
40%
40%
20%
20%
0% 0%
Random SVM MLP RSI SMA RFE Chi-squared
Forest
Accuracy Precision Recall F-score Accuracy Precision Recall F-score
E F
80%
60%
60%
40%
40%
20%
20%
0% 0%
Random SVM MLP RSI SMA RFE Chi-squared
Forest
Accuracy Precision Recall F-score Accuracy Precision Recall F-score
G H
80%
60%
60%
40%
40%
20%
20%
0% 0%
Random SVM MLP RSI SMA RFE Chi-squared
Forest
Accuracy Precision Recall F-score Accuracy Precision Recall F-score
Figure 4-1: This panel of figures demonstrates average accuracy, precision, recall, and F-score for models
implemented and the two feature selection algorithms. Classification models are utilized on both
feature selection algorithms and the average of those is demonstrated. For the feature selection
algorithms, the average between all classification models is demonstrated. A and B show normal
liquidity, C and D show the lowest liquidity, E and F show the highest liquidity, and G and H show
the markets with the highest liquidity.

Results | 21
In general, the performance varies extensively between the implemented models under the
different liquidity amounts, which is demonstrated in figure 4-1. The result shows every model’s
average performance between the two feature selection algorithms that are demonstrated and aims
to answer if any model appears to be clearly superior compared to the other models. The chance
level accuracy is ~58% and according to the observations in figure 4-1 not one single model
demonstrates a higher average accuracy than ~53%.
Some key trends and observations are identified. For example, graphs A, C, E and G show that
Random Forest tends to perform better than the other ML classificators. In addition, SVM appears
to demonstrate significant lower precision, recall, and F-score than the other ML models.
Regarding the financial trading classificators, the trend implies that SMA performs better than
RSI. It is also observed that there is no significant higher performance for ML classificators
compared to financial trading classificators. For all models, except SMA, it is observed that the
accuracy is higher than precision, recall, and F-score.
It appears in graph B, D, H and F that RFE and Chi-squared demonstrates similar performance
for all liquidity amounts, which indicates that there is not a clear superior feature selection
algorithm in this implementation. The separate analysis of feature selection algorithms was utilized
to understand if (1) the chosen feature selection algorithm could appear to have a significant impact
and (2) if one algorithm significantly outperforms the other one. The above graphs also demonstrate
the trend that accuracy is higher than precision, recall, and F-score for all amounts of liquidity.
If higher liquidity would have a big impact, it would be expected that graphs G and E showed
significant higher performance, since they include the markets and datapoints with the highest
liquidity; the correlation between liquidity and performance appears to be limited; see further
results on this in section 4.2.
4.2 Liquidity Correlation
This section compares the performance between the amounts of liquidity to evaluate whether
liquidity tends to have a significant impact on the performance of the models. Each model has been
evaluated independently based on average accuracy, precision, recall, and F-score.

22 | Results
Figure 4-2: This panel of graphs show average accuracy (graph A), precision (B), recall (C), and F-score (D)
for implemented models on the different amounts of liquidity. The average for the two feature
selection algorithms is showed for all metrics and for all the models.

Results | 23
Figure 4-2 demonstrates the performance between under different amounts of liquidity. The
observations and trends that are identified indicate that the performance varies based on the
liquidity, in some cases widely and in others marginally. A large spread between the highest
performance and lowest indicates that there is a trend between liquidity and the ability to predict
odds movement.
The largest spread observed is for accuracy in graph A and the trend for all models except SMA
is that the markets with the highest liquidity has the highest accuracy. This indicates that high
liquidity increases model performance. However, precision, recall, and F-score do not demonstrate
this trend and therefore contradicts the trend that high liquidity implies higher performance. For
example, in graph B it is demonstrated that the lowest liquidity performs best. To conclude, we
cannot clearly make observations or see trends that support the fact that the classification models
perform better with higher liquidity.
In section 4.1 it is observed that Random Forest and SMA in general obtained higher
performance. Figure 4-3 and 4.4 demonstrate the performance for each class and for all the
different amounts of liquidity for the models Random Forest in figure 4-13 and SMA in figure 4-14.
The analysis was made to understand the difference in classification for respective class between
Random Forest and SMA.
In Random Forest the trend that strikes refers to lower performance on for the class increase
with lower liquidity and improvement for the class unchanged. The results from SMA indicate that
the precision increases with higher liquidity, where the most significant increase was for the class
unchanged. However, the recall for classes decrease and increase did not improve. The main
observation is that the precision for the class unchanged for model SMA is very low and high for the
classes decrease and increase.

Numbers in %
|             |          |       |          | 78 77 |       |
| ----------- | -------- | ----- | -------- | ----- | ----- |
|             |          | 73    |          | 71    |       |
|             | 55 60 64 |       |          | 63    |       |
| 52 51 50 51 | 54       | 49 46 | 46       |       |       |
|             |          | 39    | 45 44 42 |       | 40 41 |
35
24
Precision Precision Precision Recall decrease Recall Recall increase
| decrease | unchanged | increase |     | unchanged |     |
| -------- | --------- | -------- | --- | --------- | --- |
Normal liquidity Lowest liquidity Highest liquidity Markets with highest liquidity

Figure 4-3:  Performance of Random Forest for the different amounts of liquidity, demonstrated per class.
Numbers in %
| 88       |     |             |     | 87 93 |     |
| -------- | --- | ----------- | --- | ----- | --- |
| 78 76 81 |     | 82 81 79 84 |     | 77    |     |
75
47
|     |     |     | 46 43 42 |     | 43 44 41 |
| --- | --- | --- | -------- | --- | -------- |
36
|     | 3 3 6 8 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
Precision Precision Precision Recall decrease Recall Recall increase
| decrease | unchanged | increase |     | unchanged |     |
| -------- | --------- | -------- | --- | --------- | --- |
Normal liquidity Lowest liquidity Highest liquidity Markets with highest liquidity
Figure 4-4:  Performance of SMA for the different amounts of liquidity, demonstrated per class.

24 | Discussion
5 Discussion
Chapter 5
Discussion
In this chapter I discuss the thesis, important limitations, reflections about societal impact and
ethics and sustainability. The key findings discussed include low observed performance and the
possible reasons for it, which include dataset specifics (imbalanced, Covid, etc.), dynamics of betting
exchanges (sometimes discrete, liquidity), and limited optimization of models.
5.1 Performance and Evaluation
One key limitation in evaluating the performance of the models is that a systematic statistical
significance analysis framework (null hypothesis testing) with p-values is not included. This would
create statistical evidence of performance and hence accurate insights. This thesis only presents
observations and trends identified and can therefore not determine the best model to predict price
movements with statistical evidence.
Furthermore, the models were only implemented on one dataset with k-fold cross validation. To
get a better understanding of the performance more datasets should have been evaluated and a
demonstration of the variability of mean estimates should have been included. This would have
highlighted if the evaluated dataset created unwanted results and if the data in itself was in any way
unreflective of the correct dynamics of a betting exchange, for example that it was games during
Covid.
The results are in general poor, performing below chance level accuracy. This can be explained
by a lot of reasons, for instance lack of optimization, parameter tuning of the models, the dataset.
An interesting aspect that was discussed with the company supervisor is that available odds to be
matched can be offered to the market very sporadically, and if the odds is beneficial, it will most
times be matched by a bot instantly. Therefore, in some cases it might be harder to identify trends,
because in a sense it could be seen as a discrete function, where it is believed that this would make
the models perform poorer.
SMA as an example will only classify to the class unchanged if the ten previous values are the
same, it could be possible to investigate other values of n and optimize so that certain levels of low
spread between the latest price and the average are ignored.
If I would start all over, I would have wanted to do a more thorough investigation on how the
models could have been further optimized. For example, for the models Random Forest and SMA,
but this was as mentioned not in the scope of this project. In addition, I would implement a

Discussion | 25
statistical significance analysis framework and obtain statistical significance both between feature
selection algorithms and between the dataset for every model. This would create evidence to support
whether feature selection algorithms have significant impact and if the liquidity between the
datasets truly has any impact at all.
I also believe that further collaboration with domain experts and different data scientists may
enrich the process in creating the most superior classification models.
If the models would have been very successful, they could have had significant impact on
trading strategies for both betting exchanges and within the financial stock market. The financial
stock market has always comprised of enthusiastic and motivated people trying to create a yield
based on different models. However, it is very difficult to anticipate price movements, since many
factors influence the stock market and increases complexity. The stock market and betting
exchanges have many similarities. As for the stock market, many factors influence also betting
exchanges, and therefore it is very difficult to develop a successful model for betting exchanges as
well, due to its complexity.
5.2 Critical Reflections
5.2.1 Dataset
The datasets comprised data that was measured every minute, however Betfair measures data every
second. Therefore, a different result could theoretically have been achieved since there might have
been trends that were not identified in the dataset divided by minutes compared to the dataset
divided by seconds. In addition, leagues such as the Premier League were not included, and these
leagues could demonstrate even more trends because the liquidity is higher. The length and size of
the dataset could also have a bigger impact on the models. Since it took very long time to compute
the models, this could not be investigated thoroughly.
5.2.2 Optimization of Models
One limitation is that the project does not include further optimization of the models, feature
selection algorithms, and vectorization, thus I cannot truly understand the maximum capabilities of
the model performance. This work does not describe or cover how much better the models can
become, therefore the results from this work might be misleading should the performance of the
models be extensively improved.
5.2.3 Societal Impact and Relation to Literature
ML and AI has recently boomed and has spread widely to be utilized for a range of applications. This
thesis contributes to two applications, namely betting exchanges and financial stock markets, by
investigating predictive models. Furthermore, a well working predictive model could be used to
benchmark provided odds from bookmakers to individuals and making them fairer, and in creating
trust with the individual bettors which bookmakers can utilize to promote their business. In
addition, this work provides further understanding of the predictive power in exchanges and could
therefore be utilized among other things to create economic growth. Lastly, given that there is a
growing focus towards data-driven insights for many companies, more data scientists will be
needed. This may eventually also make companies within sports betting shift towards more
automated process with AI models, creating a skill shift.
This work relates to literature by investigating a new area within betting exchanges, i.e.
prediction of odds movements. Similar, previous studies in the area of betting exchanges have been

26 | Discussion
about creating a trading bot. The key difference is that they utilize trades based on the actual odds
that are available. For example, if an arbitrage bet (guaranteed profit, bet on all outcomes) is
available it will place that bet. These studies also investigate with ML how the odds may be affected
when placing a bet, and then creating a trading algorithm around that. Therefore, this work fills a
research gap, because it only focuses on the prediction of price movements. This work can lay a
foundation before models are optimized in this domain, by helping others to focus on only
particular models, feature selection algorithms, or amounts of liquidity.
5.3 Ethics and Sustainability
Ethical considerations in sports betting have always been a highly debated. This work can lead to the
development of a model that in turn can help in many areas, such as evaluation of odds offered to
individuals, innovation of ML models in niche applications, and education. On the other hand, one
aspect that can create inequality is if only a few have access to the most optimal models, especially
when betting on exchanges, because there you bet against individuals, and could potentially earn
money from other people with less resources.
It is also important that AI models are developed so that ethical considerations are not ignored,
for example with the data it is being trained on. Therefore, it is important to have human oversight
and global regulations.
Given that a trading AI influences markets, it is crucial that it does not destabilize markets such
as betting exchanges and financial stock markets, because it can lead to vast financial consequences
for many people. For example, large transactions can create chain effects, but the benefit with
betting exchanges is that they are more isolated between betting markets. However, for public
companies there may be more substantial consequences.

Conclusions and Future Work | 27
6 Conclusions and Future Work
Chapter 6
Conclusions and Future Work
This chapter presents the conclusion of the thesis and future work.
6.1 Conclusions
To conclude, the goal of this thesis was to create a comparative analysis between ML models and
financial trading formulas’ abilities to predict odds movement under different amounts of liquidity
in the field of betting exchanges.
This thesis observed that stability and consistency performances are poor. All results presented
were evaluated and trained on the same original dataset but filtered for the purpose of
understanding the impact from liquidity, and therefore should to some extent isolate the effect of
liquidity. However, to ensure reliability, other measurements were made on smaller but different
datasets, where the results were in line with the predictive performance of the presented results,
showcasing that the performance should not increase significantly for other games. On the other
hand, the data consists of games played during Covid and therefore some of the biggest markets, for
example the British Premier League, were not available.
There is a large class imbalance, where unchanged is significantly overrepresented because most
of the time the odds would not change every minute. ~60% of the correct labels correspond with the
class unchanged. Therefore, metrics such as accuracy can be highly biased – the predictive model
could constantly classify to this class, for example. This work has therefore investigated precision
and recall as well, plus the recall and precision for individual classes.
The observation from this study indicates that Random Forest and SMA perform the best. For
SMA the identified trends are that precision improves for all classes with higher liquidity, but the
recall decreases on all classes except unchanged. For Random Forest, precision and recall only
increases for unchanged. SMA demonstrated better performance on recall for all classes and on all
amounts of liquidity, plus higher precision both for decrease and increase.
Given that the difference in some cases was very limited, and a statistical significance analysis
has not been made, and that the observation is that the best performing models perform better than
other models only for some classes, I cannot determine which is the best performing algorithm.
However, it is clear that the best performing models outperform other models in some cases, but not
throughout. Therefore, the result only establishes a base for future work, since the best model
cannot be determined.
The observations from the feature selection algorithms did not demonstrate any significant
difference, and it cannot be determined with evidence if either RFE or Chi-squared performs better

28 | Conclusions and Future Work
than the other. The conclusion is that in this work it did not seem to matter which feature selection
algorithm that was utilized.
The performance is in some cases lower than a random generator, since the overall accuracy was
lower than chance level accuracy in every case. In addition, the liquidity impact was in some cases
very limited, indicating that there might not be a very strong influence from solely the liquidity. It is
also observed that only for accuracy the trend with higher performance and higher liquidity seems
to exist, but not for recall and precision. The performance is indicated by all metrics, and thus this
work cannot conclude that higher liquidity corresponds with higher performance. This could
potentially also be explained by something else, such as different amounts of data. For instance,
Random Forest performed the best on the largest dataset. This study also highlights the complexity
of prediction and underscores that further refinement and optimization is crucial.
6.2 Future work
The most obvious potential future work is to implement a systematic statistical significance analysis
framework for ML models and the correlation between both feature selection algorithms and
between the different datasets (liquidity). It should also be an evaluation on the variability of means
estimate, which is done by evaluating on more different datasets. Another area is to further optimize
the performance of the ML models to truly understand the capabilities of them in the domain of
betting exchanges. Furthermore, more vectorization methods could be investigated. In addition,
more data analysis could be made – only some time periods could be looked at, for example. It could
include a specific time period before game start, and the models might be better in predictive
performance during some specific conditions. This work focused on the amount of liquidity,
however parameters such as the number of bets or other market dynamics could be further
investigated. Lastly, if large models are trained and a more extensive dataset is evaluated a fast
computer for computing is highly recommended, since the largest dataset took about four days to
train and evaluate for every model.

References | 29
References
[1] ‘Global Sports Betting & Lotteries - Market Size, Industry Analysis, Trends and Forecasts (2024-2029)| IBISWorld’.
[Online]. Available: https://www.ibisworld.com/default.aspx. [Accessed: 20-Feb-2024]
[2] Repairer Etuk, Tiange Xu, Brett Abarbanel, Marc N. Potenza, and Shane W. Kraus, ‘Sports betting around the world: A
systematic review’, J. Behav. Addict., vol. 11, no. 3, pp. 689–715, Sep. 2022. DOI: 10.1556/2006.2022.00064
[3] Egon Franck, Erwin Verbeek, and Stephan Nüesch, ‘Prediction accuracy of different market structures — bookmakers
versus a betting exchange’, Int. J. Forecast., vol. 26, no. 3, pp. 448–459, Jul. 2010. DOI:
10.1016/j.ijforecast.2010.01.004
[4] Leighton Vaughan Williams, ‘Information Efficiency in Betting Markets: a Survey’, Bull. Econ. Res., vol. 51, no. 1, pp. 1–
39, 1999. DOI: 10.1111/1467-8586.00069
[5] ‘What is the Betfair Exchange?’ [Online]. Available: https://betting.betfair.com/how-to-use-betfair-
exchange/beginner-guides/what-is-the-betfair-exchange-010819-51.html. [Accessed: 20-Feb-2024]
[6] Joyce E. Berg, Forrest D. Nelson, and Thomas A. Rietz, ‘Prediction market accuracy in the long run’, Int. J. Forecast.,
vol. 24, no. 2, pp. 285–300, Apr. 2008. DOI: 10.1016/j.ijforecast.2008.03.007
[7] Leighton Vaughan Williams, Information Efficiency in Financial and Betting Markets. Cambridge University Press,
2005, ISBN: 978-1-139-44540-5.
[8] Polyvios Tsirimpas, ‘Specification and Performance Optimisation of Real-time Trading Strategies for Betting Exchange
Platforms’, 2014 [Online]. Available: https://core.ac.uk/download/pdf/76996196.pdf. [Accessed: 28-Feb-2024]
[9] David A. Grimes and Kenneth F. Schulz, ‘Making sense of odds and odds ratios’, Obstet. Gynecol., vol. 111, no. 2 Part 1,
pp. 423–426, 2008.
[10] E.D. Feustel and G.S. Howard., Conquering Risk: Attacking Las Vegas and Wall Street. Academic Publishers, 2010.
[11] David Forrest, ‘Betting and the Integrity of Sport’, in Sports Betting: Law and Policy, P. M. Anderson, I. S. Blackshaw,
R. C. R. Siekmann, and J. Soek, Eds. The Hague, The Netherlands: T. M. C. Asser Press, 2011, pp. 14–26 [Online]. DOI:
10.1007/978-90-6704-799-9_3
[12] Steven D. Levitt, ‘Why are Gambling Markets Organised so Differently from Financial Markets?’, Econ. J., vol. 114, no.
495, pp. 223–246, Apr. 2004. DOI: 10.1111/j.1468-0297.2004.00207.x
[13] ‘Betfair’. [Online]. Available: https://www.betfair.se/aboutUs/Betfair.Charges/. [Accessed: 08-Mar-2024]
[14] Max Kuhn and Kjell Johnson, Applied Predictive Modeling. New York, NY: Springer New York, 2013, ISBN: 978-1-
4614-6848-6 [Online]. DOI: 10.1007/978-1-4614-6849-3
[15] Daniel Powers and Yu Xie, Statistical methods for categorical data analysis. Emerald Group Publishing, 2008
[Online]. Available:
https://books.google.com/books?hl=sv&lr=&id=EqABbeTIMj4C&oi=fnd&pg=PP1&dq=Statistical+methods+for+categ
orical+data+analysis&ots=FA96081R8J&sig=eQYN8xNU3nzPvoWn_62lVGW9_Iw. [Accessed: 09-Mar-2024]
[16] Pádraig Cunningham, Matthieu Cord, and Sarah Jane Delany, ‘Supervised Learning’, in Machine Learning Techniques
for Multimedia, M. Cord and P. Cunningham, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2008, pp. 21–49
[Online]. DOI: 10.1007/978-3-540-75171-7_2
[17] Emil Christoffersson, Beating the odds : Machine Learning for football match prediction. 2023 [Online]. Available:
https://urn.kb.se/resolve?urn=urn:nbn:se:hj:diva-61424. [Accessed: 20-Feb-2024]
[18] David G. Stork, Richard O. Duda, Peter E. Hart, and D. Stork, Pattern classification. John Wiley., 2001.
[19] Trevor Hastie, Jerome Friedman, and Robert Tibshirani, The Elements of Statistical Learning. New York, NY: Springer
New York, 2001, Springer Series in Statistics, ISBN: 978-1-4899-0519-2 [Online]. DOI: 10.1007/978-0-387-21606-5
[20] Daniel Berrar, ‘Cross-Validation’, 2018. DOI: 10.1016/B978-0-12-809633-8.20349-X
[21] Sotiris Kotsiantis, ‘Feature selection for machine learning classification problems: a recent overview’, Artif. Intell. Rev.,
vol. 42, no. 1, pp. 157–176, 2011.
[22] Kenji Kira and Larry A. Rendell, ‘A Practical Approach to Feature Selection’, in Machine Learning Proceedings 1992, D.
Sleeman and P. Edwards, Eds. San Francisco (CA): Morgan Kaufmann, 1992, pp. 249–256 [Online]. DOI:
10.1016/B978-1-55860-247-2.50037-1
[23] Włodzisław Duch, ‘Filter Methods’, in Feature Extraction, vol. 207, I. Guyon, M. Nikravesh, S. Gunn, and L. A. Zadeh,
Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2006, pp. 89–117 [Online]. DOI: 10.1007/978-3-540-35488-8_4
[24] Huan Liu and Lei Yu, ‘Toward integrating feature selection algorithms for classification and clustering’, IEEE Trans.
Knowl. Data Eng., vol. 17, no. 4, pp. 491–502, 2005.
[25] Isabelle Guyon and André Elisseeff, ‘An introduction to variable and feature selection’, J. Mach. Learn. Res., vol. 3, no.
Mar, pp. 1157–1182, 2003.
[26] Carl Kingsford and Steven L. Salzberg, ‘What are decision trees?’, Nat. Biotechnol., vol. 26, no. 9, pp. 1011–1013, 2008.

30 | References
[27] Mohammed S. Alam and Son T. Vuong, ‘Random forest classification for detecting android malware’, in 2013 IEEE
international conference on green computing and communications and IEEE Internet of Things and IEEE cyber,
physical and social computing, 2013, pp. 663–669 [Online]. Available:
https://ieeexplore.ieee.org/abstract/document/6682136/. [Accessed: 10-Mar-2024]
[28] Durgesh Srivastava and Lekha Bhambhu, ‘Data classification using support vector machine’, J. Theor. Appl. Inf.
Technol., vol. 12, pp. 1–7, Feb. 2010.
[29] Bayya Yegnanarayana, Artificial neural networks. PHI Learning Pvt. Ltd., 2009 [Online]. Available:
https://books.google.com/books?hl=sv&lr=&id=RTtvUVU_xL4C&oi=fnd&pg=PR9&dq=Artificial+neural+networks+
&ots=Ge7YylyHWD&sig=ZSBbc7iDvu2UCKD7HShpjecBFJw. [Accessed: 13-Mar-2024]
[30] Simon Haykin, Neural networks and learning machines, 3/E. Pearson Education India, 2009.
[31] Craig A. Ellis and Simon A. Parbery, ‘Is smarter better? A comparison of adaptive, and simple moving average trading
strategies’, Res. Int. Bus. Finance, vol. 19, no. 3, pp. 399–411, Sep. 2005. DOI: 10.1016/j.ribaf.2004.12.009
[32] Srinivas Gumparthi, ‘Relative strength index for developing effective trading strategies in constructing optimal
portfolio’, Int. J. Appl. Eng. Res., vol. 12, no. 19, pp. 8926–8936, 2017.
[33] M.C. Purucker, ‘Neural network quarterbacking’, IEEE Potentials, vol. 15, no. 3, pp. 9–15, Aug. 1996. DOI:
10.1109/45.535226
[34] Alan Mccabe and Jarrod Trevathan, Artificial Intelligence in Sports Prediction. 2008, p. 1197. DOI:
10.1109/ITNG.2008.203
[35] Kou-Yuan Huang and Wen-Lung Chang, A neural network method for prediction of 2006 World Cup Football Game.
2010, p. 8. DOI: 10.1109/IJCNN.2010.5596458
[36] Dragan Miljković, Ljubiša Gajić, Aleksandar Kovačević, and Zora Konjović, ‘The use of data mining for basketball
matches outcomes prediction’, in IEEE 8th International Symposium on Intelligent Systems and Informatics, 2010,
pp. 309–312 [Online]. DOI: 10.1109/SISY.2010.5647440
[37] Erik Štrumbelj, ‘On determining probability forecasts from betting odds’, Int. J. Forecast., vol. 30, no. 4, pp. 934–943,
Oct. 2014. DOI: 10.1016/j.ijforecast.2014.02.008
[38] João Pedro Araújo Santos, ‘A Trading Agent Framework Using Plain Strategies & Machine Learning’.
[39] Øyvind Norstein Øvregård, ‘Trading “in-play” betting Exchange Markets with Artificial Neural Networks’.
[40] Ivars Dzalbs and Tatiana Kalganova, ‘Forecasting Price Movements in Betting Exchanges Using Cartesian Genetic
Programming and ANN’, Big Data Res., vol. 14, pp. 112–120, Dec. 2018. DOI: 10.1016/j.bdr.2018.10.001
[41] Rui Gonçalves, Vitor Miguel Ribeiro, Fernando Lobo Pereira, and Ana Paula Rocha, ‘Deep learning in exchange
markets’, Inf. Econ. Policy, vol. 47, pp. 38–51, 2019.
[42] Andrew Bunyan, ‘Time Series Analysis and Forecasting of In-Play Odds on a Betting Exchange’.
[43] Franc JGM Klaassen and Jan R. Magnus, ‘Forecasting the winner of a tennis match’, Eur. J. Oper. Res., vol. 148, no. 2,
pp. 257–267, 2003.
[44] Agnieszka M. Madurska, ‘A set-by-set analysis method for predicting the outcome of professional singles tennis
matches’, 4th Year Softw. Eng. MEng Proj. Imp. Coll. Lond. Dep. Comput. Lond. UK, 2012 [Online]. Available:
https://www.doc.ic.ac.uk/teaching/distinguished-projects/2012/a.madurska%20.pdf. [Accessed: 10-Apr-2024]
[45] Peter Antony Bebbington, ‘Studies in informational price formation, prediction markets, and trading’, PhD Thesis, UCL
(University College London), 2017 [Online]. Available: https://discovery.ucl.ac.uk/id/eprint/1563501/. [Accessed: 10-
Apr-2024]
[46] Markus Junker, Rainer Hoch, and Andreas Dengel, ‘On the evaluation of document analysis components by recall,
precision, and accuracy’, in Proceedings of the Fifth International Conference on Document Analysis and Recognition.
ICDAR’99 (Cat. No. PR00318), 1999, pp. 713–716 [Online]. Available:
https://ieeexplore.ieee.org/abstract/document/791887/. [Accessed: 09-Mar-2024]

Conclusions and Future WorkAppendix A: Model Performance | 31
Appendix A: Model Performance
|     |     | 1.  Results 100 Games Without Filtering based on Liquidity   |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Model Feature selection Accuracy Precision  Recall F-score Precision decrease Precision unchanged Precision increase Recall decrease Recall unchanged Recall increase
| Random Forest | RFE | 50% 48% | 47% 47% | 49% | 53% | 43% | 41% | 64% | 35% |
| ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Random Forest Chi-squared 53% 52% 51% 51% 52% 55% 73% 45% 78% 40%
| SVM     | RFE         | 45% 15% | 33% 21% | -   | 45% | -   | 0%  | 100% | 0%  |
| ------- | ----------- | ------- | ------- | --- | --- | --- | --- | ---- | --- |
| SVM     | Chi-squared | 45% 23% | 28% 25% | -   | 45% | -   | 0%  | 100% | 0%  |
| MLP     | RFE         | 46% 49% | 35% 40% | 53% | 46% | 44% | 4%  | 98%  | 1%  |
| MLP     | Chi-squared | 47% 50% | 36% 42% | 50% | 46% | 49% | 8%  | 97%  | 2%  |
| RSI     | -           | 41% 26% | 31% 29% | 17% | 45% | 17% | 4%  | 86%  | 4%  |
| SMA     | -           | 45% 56% | 54% 55% | 46% | 77% | 43% | 78% | 3%   | 82% |
| Average |             | 47% 40% | 39% 39% | 45% | 52% | 45% | 23% | 78%  | 21% |
| Median  |             | 46% 48% | 35% 41% | 50% | 46% | 44% | 6%  | 92%  | 3%  |

|     |     | 2.  Results Liquidity Over Average  |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
M o d e l F e a tu re  se le c tio n A c c u ra c y P re c isio n   R e c a ll F -sc o re P re c isio n  d e c re a se P re c isio n  u n c h a n g e d P re c isio n  in c re a se R e c a ll d e c re a se R e c a ll u n c h a n g e d R e c a ll in c re a se
R an d o m  F oo rest R F E 5 1% 4 6 % 4 5 % 4 5 % 4 3 % 5 7 % 3 8 % 3 7 % 7 0 % 2 6 %
R an d o m  F rest C h i-sq u ared 5 5 % 5 2 % 5 0 % 5 1% 5 0 %-- 6 0 % 4 6 %-- 4 4 % 7 1% 3 5 %
| SV M | R F E | 4 9 % 16 % | 3 3 % 2 2 % |     | 4 9 % |     | 0 % | 10 0 % | 0 % |
| ---- | ----- | ---------- | ----------- | --- | ----- | --- | --- | ------ | --- |
SV M C h i-sq u ared 4 9 % 3 1% 3 3 % 3 2 % 4 9 % 0 % 10 0 % 0 %
M L P R F E 3 9 % 4 0 % 3 8 % 3 9 % 3 1% 5 4 % 2 8 % 3 3 % 4 3 % 3 7 %
M L P C h i-sq u ared 4 5 % 4 6 % 4 0 % 4 3 % 3 6 % 5 5 % 3 2 % 3 8 % 6 1% 2 2 %
R SI -- 4 2 % 3 0 % 3 2 % 3 1% 2 4 % 4 8 % 18 % 11% 7 6 % 8 %
| SM A |     | 4 4 % 5 7 | % 5 5 % 5 6 % | 4 3 % | 8 7 % | 4 1% | 8 1% | 6 % | 7 9 % |
| ---- | --- | --------- | ------------- | ----- | ----- | ---- | ---- | --- | ----- |
A v e ra g e 4 7 % 4 0 % 4 1% 4 0 % 3 8 % 5 7 % 3 4 % 3 1% 6 6 % 2 6 %
M e d ia n 4 7 % 4 3 % 3 9 % 4 1% 3 9 % 5 4 % 3 5 % 3 5 % 7 1% 2 4 %

|     |     | 3.  Results Liquidity Under Average  |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Model Feature selection Accuracy Precision  Recall F-score Precision decrease Precision unchanged Precision increase Recall decrease Recall unchanged Recall increase
| Random Forest | RFE | 49% 48% | 47% 48% | 49% | 52% | 44% | 42% | 61% | 38% |
| ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Random Forest Chi-squared 52% 51% 50% 51% 51% 54% 49% 46% 63% 41%
| SVM     | RFE         | 43% 16% | 33% 22% | -   | 88% | -   | 0%  | 100% | 0%  |
| ------- | ----------- | ------- | ------- | --- | --- | --- | --- | ---- | --- |
| SVM     | Chi-squared | 43% 36% | 33% 34% | -   | 88% | -   | 0%  | 100% | 0%  |
| MLP     | RFE         | 44% 49% | 35% 41% | 52% | 44% | 49% | 5%  | 98%  | 1%  |
| MLP     | Chi-squared | 45% 48% | 36% 41% | 51% | 44% | 48% | 7%  | 97%  | 3%  |
| RSI     | -           | 39% 27% | 31% 29% | 19% | 43% | 18% | 5%  | 84%  | 5%  |
| SMA     | -           | 46% 55% | 53% 54% | 76% | 3%  | 81% | 47% | 75%  | 44% |
| Average |             | 45% 41% | 40% 40% | 50% | 52% | 48% | 19% | 85%  | 17% |
| Median  |             | 44% 48% | 35% 41% | 51% | 48% | 48% | 6%  | 90%  | 4%  |

|     |     | 4.  Results Upper 25% percentile in Terms of Liquidity  |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Model Feature selection Accuracy Precision  Recall F-score Precision decrease Precision unchanged Precision increase Recall decrease Recall unchanged Recall increase
| Random Forest | RFE | 55% 45% | 42% 44% | 42% | 61% | 31% | 32% | 77% | 17% |
| ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Random Forest Chi-squared 58% 51% 48% 49% 51% 64% 39% 42% 77% 24%
| SVM     | RFE         | 57% 19% | 33% 24% | -   | 12% | -   | 0%  | 100% | 0%  |
| ------- | ----------- | ------- | ------- | --- | --- | --- | --- | ---- | --- |
| SVM     | Chi-squared | 57% 22% | 33% 27% | -   | 12% | -   | 0%  | 100% | 0%  |
| MLP     | RFE         | 46% 39% | 36% 38% | 34% | 57% | 23% | 16% | 65%  | 28% |
| MLP     | Chi-squared | 50% 42% | 37% 40% | 33% | 59% | 22% | 27% | 72%  | 14% |
| RSI     | -           | 47% 29% | 31% 30% | 20% | 56% | 11% | 9%  | 78%  | 6%  |
| SMA     | -           | 41% 57% | 60% 58% | 42% | 93% | 36% | 88% | 8%   | 84% |
| Average |             | 51% 38% | 40% 39% | 37% | 52% | 27% | 27% | 72%  | 22% |
| Median  |             | 52% 41% | 37% 39% | 38% | 58% | 27% | 22% | 77%  | 16% |

32 | Appendix B: Liquidity analysis
Appendix B: Liquidity analysis
1.  Accuracy
|     |     |     | 1 0 0  G a%%%%%%%% m e s U n | d e r45444434  A92334596 v%%%%%%%% e r a g e | O v e r  a v%%%%%%%% | e r a g e T o p55554544 |  2 5 % |
| --- | --- | --- | ---------------------------- | -------------------------------------------- | -------------------- | ----------------------- | ------ |
RRSSMMRS a n d o mm R C R C  F o r e s tt  - -  R C Fh Ei- 5 0 5 1 5 %
| a n d o - - - - |  F o r e s         | s q u a r e d | 5 3   |       | 5 5   |     | 8 % |
| --------------- | ------------------ | ------------- | ----- | ----- | ----- | --- | --- |
| V M             | F E                |               | 4 5   |       | 4 9   |     | 7 % |
| V ML            | h i- s q u a r e d |               | 4 5   |       | 4 9   |     | 7 % |
| P               | F E                |               | 4 6   |       | 3 9   |     | 6 % |
| L P             | h i- s q u a r e d |               | 4 7   |       | 4 5   |     | 0 % |
| S I             |                    |               | 4 1   |       | 4 2   |     | 7 % |
| M A             |                    |               | 4 5   |       | 4 4   |     | 1 % |
| A v e r a g e   |                    |               | 4 7 % | 4 5 % | 4 7 % | 5   | 1 % |
| M e d i a n     |                    |               | 4 6 % | 4 4 % | 4 7 % | 5   | 2 % |

2.  Precision
|     |     |     | 1 0 0  G a%%%%%%%% m e s U n | d e r45134425  A81669875 v%%%%%%%% e r a g e | O v e r  a v%%%%%%%% | e r a g e T o p45123425 |  2 5 % |
| --- | --- | --- | ---------------------------- | -------------------------------------------- | -------------------- | ----------------------- | ------ |
RRSSMMRS a n d o mm R C R C  F o r e s tt  - -  R C Fh Ei- 4 8 4 6 5 %
| a n d o - - - - |  F o r e s         | s q u a r e d | 5 2   |       | 5 2   |     | 1 % |
| --------------- | ------------------ | ------------- | ----- | ----- | ----- | --- | --- |
| V M             | F E                |               | 1 5   |       | 1 6   |     | 9 % |
| V ML            | h i- s q u a r e d |               | 2 3   |       | 3 1   |     | 2 % |
| P               | F E                |               | 4 9   |       | 4 0   |     | 9 % |
| L P             | h i- s q u a r e d |               | 5 0   |       | 4 6   |     | 2 % |
| S I             |                    |               | 2 6   |       | 3 0   |     | 9 % |
| M A             |                    |               | 5 6   |       | 5 7   |     | 7 % |
| A v e r a g e   |                    |               | 4 0 % | 4 1 % | 4 0 % | 3   | 8 % |
| M e d i a n     |                    |               | 4 8 % | 4 8 % | 4 3 % | 4   | 1 % |

3.  Recall
|     |     |     | 1 0 0  G a%%%%%%%% m e s U n | d e r45333335  A70335613 v%%%%%%%% e r a g e | O v e r  a v%%%%%%%% | e r a g e T o p44333336 |  2 5 % |
| --- | --- | --- | ---------------------------- | -------------------------------------------- | -------------------- | ----------------------- | ------ |
RRSSMMRS a n d o mm R C R C  F o r e s tt  - -  R C Fh Ei- 4 7 4 5 2 %
| a n d o - - - - |  F o r e s         | s q u a r e d | 5 1   |       | 5 0   |     | 8 % |
| --------------- | ------------------ | ------------- | ----- | ----- | ----- | --- | --- |
| V M             | F E                |               | 3 3   |       | 3 3   |     | 3 % |
| V ML            | h i- s q u a r e d |               | 2 8   |       | 3 3   |     | 3 % |
| P               | F E                |               | 3 5   |       | 3 8   |     | 6 % |
| L P             | h i- s q u a r e d |               | 3 6   |       | 4 0   |     | 7 % |
| S I             |                    |               | 3 1   |       | 3 2   |     | 1 % |
| M A             |                    |               | 5 4   |       | 5 5   |     | 0 % |
| A v e r a g e   |                    |               | 3 9 % | 4 0 % | 4 1 % | 4   | 0 % |
| M e d i a n     |                    |               | 3 5 % | 3 5 % | 3 9 % | 3   | 7 % |

Conclusions and Future WorkAppendix B: Liquidity analysis | 33
4.  F-score
|                             | 100 Games | Under Average | Over average | Top 25% |
| --------------------------- | --------- | ------------- | ------------ | ------- |
| Random Forest - RFE         | 47%       | 48%           | 45%          | 44%     |
| Random Forest - Chi-squared | 51%       | 51%           | 51%          | 49%     |
| SVM - RFE                   | 21%       | 22%           | 22%          | 24%     |
| SVM - Chi-squared           | 25%       | 34%           | 32%          | 27%     |
| MLP - RFE                   | 40%       | 41%           | 39%          | 38%     |
| MLP - Chi-squared           | 42%       | 41%           | 43%          | 40%     |
| RSI                         | 29%       | 29%           | 31%          | 30%     |
| SMA                         | 55%       | 54%           | 56%          | 58%     |
| Average                     | 39%       | 40%           | 40%          | 39%     |
| Median                      | 41%       | 41%           | 41%          | 39%     |

www.kth.se
TRITA-EECS-EX-2024:666
Stockholm, Sweden 2024
www.kth.se