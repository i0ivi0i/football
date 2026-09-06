ProgressinArtificialIntelligence(2026)15:189–202
https://doi.org/10.1007/s13748-025-00395-8
REGULAR PAPER
Predicting draws and number of fouls in football matches using
Bayesian network classifiers
Nicolás Pérez-Blanco1·Antonio Salmerón1,2
Received:23January2025/Accepted:27July2025/Publishedonline:1September2025
©TheAuthor(s)2025
Abstract
Thisstudyproposesaunifiedapproachtopredictingtwospecificeventsinfootball-thenumberoffoulscommittedandthe
probabilityofadraw-usingNaiveBayes(NB)classifiersoptimizedthroughdiscretizationstrategiesaimedateffectiveclass
separation.First,amodelisintroducedtoanticipatethenumberoffoulsinamatch,discretizedintointervalsdeterminedby
historicalpercentiles,therebycapturingtheordinaldistributionoftheseinfractions.Toevaluatetheclassificationperformance,
the RPS is employed. The proposed discretization attains an overall RPS = 0.0093, outperforming k-means (0.0098) and
Fayyad-Irani(0.0098).Second,thepredictionofdrawsisaddressedbyincorporatingsubjectivefactorssuchasthesignificance
ofregionalderbiesandteams’historicalrankings.Giventheclassimbalanceinherentinthistask,weightedaccuracy(WAP)and
weightedrecall(WAR)metricsareused.OurmodelreachesWAP=0.424andWAR=0.565,versus0.413/0.539withk-means
and0.406/0.539withFayyad-Irani.TheseresultsshowthatdiscretizationsspecificallydesignedforNBsubstantiallyimprove
the performance of both models compared to other standard discretizers, providing a comprehensive and computationally
efficientframeworkformodelingrareeventsinthefootballdomain.
Keywords Bayesiannetworkclassifiers·Clustering·Balancedclassification·Imbalancedclassification·Footballforecasting
1 Introduction oriented, univariate discretization rules can unlock the full
efficiency of a lightweight Naive Bayes classifier, keeping
The prediction of specific events in the sports domain has the model transparent while rivaling more complex learn-
gainedmomentuminacademicliterature,fueledbythegrow- ers.Thisworkoriginatesfromtheproposalofdiscretization
ing availability of data and the increasing sophistication of strategiesthatenhancetheperformanceofNaiveBayes(NB)
sportsanalyticstools.Inthiscontext,footballprovidesfertile classifiersfortwospecificcases:(1)predictingthenumber
groundforexploringpredictivemodelsthataddressvarious offoulsinafootballmatch,and(2)predictingdrawsbased
aspectsofthegame,rangingfromthenumberofgoalsscored onvariablessuchasgoals,teamrankings,andtheintensity
toless-studiedindicatorssuchasfoulscommittedormatch inherentinregionalderbies.
outcomes (win, draw, or loss) and mirroring the success of First,predictingfoulsinfootballisjustifiedbytheimpact
lightweightneuralmodelsinotherpredictiondomainssuch theseinfractionshaveonthecourseofamatch.Foulsreflect
as energy- and agricultural-commodity prices [1, 2]. Our not only the aggressiveness or intensity of each team but
mainmotivationismethodological:weinvestigatehowclass- alsotheirdefensiveandoffensivestrategies,shapingtheflow
of the game and even the availability of players. Although
B otheraspectssuchasfinalmatchoutcomes[3,4]oroverall
AntonioSalmerón
team performance [5–7], have received considerable atten-
antonio.salmeron@ual.es
tion,thereisanotablegapintheliteratureregardingmodels
NicolásPérez-Blanco
specificallydesignedtoanticipatethenumberoffouls.This
npb063@inlumine.ual.es
gap is significant because fouls can alter match dynamics,
1 DepartmentofMathematics,UniversityofAlmería,Almería influence the psychological state of teams, and generally
04120,Spain affect the probability of specific events (e.g., red cards or
2 CenterfortheDevelopmentandTransferofMathematical injuries).
ResearchtoIndustry,UniversityofAlmería,Almería04120,
Spain
123

190 ProgressinArtificialIntelligence(2026)15:189–202
ThefirstunifiedapproachpresentedherefocusesonanNB scorestheimportanceoftailoringdiscretizationtotheneeds
classifiertopredictthe“fouls”variable,dividingitintofour ofNBclassifiers[23,24]sothattheresultingsegmentation
classesbasedonintervalsderivedfromhistoricalpercentiles. bettercapturesdistributionaldifferencesamongtheclassesof
The goal is to show how suitable discretization-rather than interest[25].Inthecaseoffouls,thisisachievedbyassigning
model complexity-drives the gain in predictive accuracy. relativemembershiplevelstoeachteambasedonitsdistance
Theoriginalityliesinthediscretizationmethodused,which tothecentroids,allowingforamoreaccuraterepresentation
differsfromstandardclusteringprocesses.Ratherthanmax- of teams’ heterogeneous behavior and their propensity to
imizing within-cluster homogeneity, the proposed strategy commit or induce fouls. For draws, the proposed approach
assigns relative membership levels to each team according implements a clustering process whose primary goal is to
to its proximity to cluster centroids. This approach lever- maximize distributional divergence between matches that
agesthediscretenatureofteamclassificationsandenhances endinadrawandthosethatendinawinorloss.
themodelingofvariabilityamongteams,therebyincreasing Therefore,thisarticle’scontributionliesinunifyingthese
theaccuracyofprobabilisticassignmentsforeachclass.To two methods and demonstrating that a suitable discretiza-
assessclassificationperformance,theRankProbabilityScore tionofcomponentsiscrucialforimprovingtheperformance
(RPS)isemployed-ametricrecommendedforordinal-class of Bayesian classifiers when predicting specific events.
scenarios [8–10]. RPS compares the predicted probability Although the applications differ-fouls in the first case and
distributions with the observed outcome, weighting suc- draws in the second-the underlying philosophy is similar:
cesses in each category and suitably penalizing errors that to exploit the flexibility of NB classifiers, which can han-
deviatesignificantlyfromreality. dle uncertainty, together with data-segmentation strategies
Incontrast,thesecondapproachaddressestheprediction geared toward class differentiation. In doing so, we aim to
of draws in football, a problem requiring a distinct treat- provideacomprehensiveoverviewofhowprobabilisticmod-
ment compared to home or away wins. Numerous studies elscanbeappliedtospecificphenomenainfootball.
usePoissondistributionstomodelgoalsscoredbyeachteam The remainder of this article is organized as follows. In
andderivematchresults[11,12].However,therelativerar- Section2wedelvedeeperintorelatedstudiesonsportsevent
ityofdrawsamongallpossibleoutcomeshaspromptedthe prediction using Bayesian networks (BN) and NB, as well
developmentofspecificmodelsthataccountforclassimbal- asmodelevaluationmetricsanddiscretizationproposalsfor
ance[13,14].Otherprobabilisticmodelshavebeenproposed imbalanced orordinalclasses.Section 3thoroughly details
usingteamrankings[15–17],groupingteamsbasedontheir thestrategiesemployedforpredictingthenumberoffoulsin
likelihood of winning. In this context, criticism arises that amatchandforcalculatingtheprobabilityofamatchending
Poissondistributionsdonotalwaysfitwellwhenmodeling inadraw.InSection4,wepresentthescoresachievedbythe
draws[4,18],thusmotivatingthesearchforalternativesthat proposedmodelsintermsofpredictivequalityandcompare
explicitlyincorporatefactorsfavoringanaccurateestimation them to the performance of other similar models. Finally,
ofdrawprobabilities. wereflectonthefindingsdiscussedthroughoutthearticlein
Inthedraw-predictionmodelpresentedhere,factorsasso- Section5.
ciated with goal production and team performance (both
current and historical) are combined with more subjective
elements, such as the significance of regional derbies [19, 2 LiteratureReview
20]. These rivalries foster a more intense atmosphere that
can influence player performance and, consequently, affect Whathasbeenachieved.Theliteratureonpredictingmatch
theprobabilityofamatchendinginadraw[21].Theorigi- outcomesandspecificeventsinfootballcanbedividedinto
nalityofthisapproachliesinthecreationofclustersthrough severalprimaryapproaches.Onesetofstudiesusesclassical
a second NBclassifier,which serves to discretize the com- statisticalmodelstopredictgoalsandthusestimatethefinal
ponentsoftheprimaryNBclassifier.Moreover,themodelis resultasahomewin,draw,orawaywin[3,4].Theseworks
evaluatedusingmetricsthataddresstheimbalancebetween commonlyrelyonthePoissondistributionandassumeacer-
the“draw”classandthe“win”or“loss”classes,providinga taindegreeofindependencebetweeneachteam’soffensive
morepreciseunderstandingofthemodel’spredictivepower anddefensiveperformance.However,ithasbeenarguedthat
underhighlyskeweddatadistributions. this assumption may not fully capture less frequent events,
Hence, the key factor in both unified approaches of this such as draws [4, 18] or more heterogeneous phenomena,
work is the role of discretizing continuous variables. For suchasfoulscommittedduringamatch[26].
predicting both fouls and draws, traditional discretization Anothergroupofresearchershasfocusedonteam-based
methods(e.g.,k-meansclustering)arenotalwaysoptimal,as ranking models, positing that league standings sufficiently
theytendtoprioritizewithin-clusterhomogeneityratherthan reflectateam’soverallperformanceovertime[15–17].Inthis
effectivelyseparatingtheclasses[22].Theliteratureunder- approach, teams are grouped according to their probability
123

ProgressinArtificialIntelligence(2026)15:189–202 191
of winning, which allows for predictions without explic- Nevertheless,measuringthequalityofthedraw-prediction
itlymodelinggoalsoroffensiveanddefensiveperformance. modelinvolvestheissueofhighlyimbalancedclasses.The
Althoughthesemethodshaveprovedeffectiveingeneralcon- literature has long emphasized the importance of selecting
texts,ithasbeenobservedthatdrawsarenotpredictedwith appropriate evaluation metrics for such cases. Historically,
thesameaccuracyaswinsorlosses,leadingtomorespecial- measureslikeprecision,accuracy,orrecallhavedominated
izedmodelsdesignedspecificallytoaddresstiedoutcomes. model evaluation, but their validity diminishes when class
An additional lineof research concentrates on BNs and, distribution is highly skewed or when there is an intrinsic
more specifically, NB classifiers, which have been shown ordertothecategories[13,14].Consequently,inevaluating
to be effective tools for classification tasks in football [10, drawprediction,weemployweightedaccuracyandweighted
27, 28]. The appeal of NB lies in its simplicity and its recall.
probabilistictreatmentofuncertainty,assumingconditional Another aspect that has garnered attention is the role of
independence among predictor variables given the class. contextualandsubjectivefactorsinmatchprediction,asevi-
Although perfect independence is rarely achieved in prac- denced by regional derbies [19, 20]. Derbies introduce an
tice, numerous studies have found that NB often produces additional emotional dimension for both players and fans,
goodresultsevenunderpartialdependencies[25]. potentiallyalteringmatchdynamicssignificantly[21].This
However,theeffectivenessofNBhingessignificantlyon characteristichasbeenincorporatedintosomemodelsasan
howcontinuousvariablesarediscretized[24].Theliterature additionalcomponentthatadjuststheprobabilityofadraw,
indicates that traditional discretization methods, such as k- based on the hypothesis that local rivalries lead to more
means orequidistantcut-points,arenotalwaysoptimalfor intensely contested matches and, in certain cases, a higher
enhancingclassseparation,astheyaredesignedtomaximize likelihoodofatiedresult.
within-clusterhomogeneityratherthanhighlightdifferences
Whatispresentedhere.Inresponsetotheseopenissues,the
between categories of the target variable [22]. Among the
present study evaluates dedicated discretization rules-both
mostcitedsuperviseddiscretizers,theMDLalgorithm[29]
entropy-based [29] and a novel class-separation scheme-
standsout.ThealgorithmbyFayyad&Iraniis,infact,the
withinaunidimensionalNBframeworkappliedtofouland
canonical implementation of supervised entropy-based dis-
cretization(informationgain),usingaχ2 testandanMDL drawprediction.Inconclusion,theliteraturereviewsuggests
thatpredictingspecificeventsinfootball-beitthenumberof
criteriontodeterminethecutpoints.Itgeneratesoptimalcut
foulsordraws-requiresmethodsthatcombinetheflexibility
pointsandhasbecomeabenchmarkforevaluatingdiscretiza-
ofBayesianmodelswithdiscretizationandevaluationtech-
tionmethodsforBayesianclassifiers.
niquessuitedtoeachproblem.Thereisagrowingconsensus
thatalthoughPoisson-basedapproachesareuseful,theyare
What remains to be addressed. Despite the progress out-
not always sufficient for capturing rarer or more complex
linedabove,twogapsarestillevident:(i)thelimitedattention
phenomena[4,18],andthatincorporatingteamrankingsor
to rare-event targets such as fouls and draws, and (ii) the
contextual factors broadens predictive scope. Still, the key
lackofsystematicanalysisonhowsupervised,class-oriented
liesindesigningdiscretizationproceduresthathighlightdis-
discretization can unlock the full efficiency of simple NB
tributionaldifferencesbetweenclasses,asdemonstratedby
classifiers. For draw prediction, for example, the challenge
clustering methods focused on inter-class separation rather
istodistinguishbetweenmatchesthatendinadrawandthose
thanwithin-clusterhomogeneity[22,25].
thatendinawinorloss-anobjectivethatcallsformaximiz-
Accordingly, this research follows the trend of prioritiz-
ingdistributionaldivergenceratherthanclustercompactness
ingclassificationimprovementsthroughthecarefulselection
[13,14].Infoulprediction,asimilarsituationarises:captur-
ofmetricsanddata-segmentationstrategiestomodelscenar-
ingvariabilityamongteams-someconsistentlycommitmore
ioswithimbalancedand/orordinalclasses.Byunifyingthe
infractions,whileotherspromptopponentstocommitthem-
approaches to predict fouls and draws into a single study,
is essential to achieving a realistic probability of a match
it becomes evident that NB classifiers can effectively han-
outcomethatincludesfouls.
dle various football-related tasks, while the choice of data
In studying fouls, we employ the RPS to gauge model
segmentationiscriticallyimportantformodelingtheunique
performance, as it evaluates not only direct classification
characteristicsofeachphenomenon.
butalsothecumulative probabilitydistributionacrosseach
class[8–10].Thismetricisespeciallyusefulwhenthecate-
goriesfollowanaturalorder,suchasfoulintervals(e.g.,0-10,
11-20,21-30,over30).RPSpenalizesmisclassificationsin 3 Proposedmethodology
distantcategories more severely than thoseinadjacent cat-
egories,providingmoreinformativefeedbackthanasimple Thedatasetutilizedinthisstudyspansfromthe2010-2011
success/failuremetric. season to the 2021-2022 season of the Spanish La Liga.
123

| 192         |        |                  |          |      |                      |          |      |     |     | ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |
| ----------- | ------ | ---------------- | -------- | ---- | -------------------- | -------- | ---- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
| The data    | were   | freely collected |          | from | Football-Data.co.uk, |          |      |     |     |                                                  |     |     |     |     |
| a reputable | source | of               | detailed | and  | reliable             | football | out- |     |     |                                                  |     |     |     |     |
comes,ensuringthequalityandintegrityoftheinformation
| used in    | this research. | The     | initial    | two | years, 2010-2011 |        | and |       |                                                        |     |     |     |     |     |
| ---------- | -------------- | ------- | ---------- | --- | ---------------- | ------ | --- | ----- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
| 2011-2012, | are            | used to | initialize | the | proposed         | models | and |       |                                                        |     |     |     |     |     |
|            |                |         |            |     |                  |        |     | Fig.1 | AnexampleofaBayesianNetworkstructureillustratingdepen- |     |     |     |     |     |
willconstitutepartoftheaccumulatedhistoricaldata.This
denciesamongvariables
| selection  | allows    | for considering |     | seasonal   | changes,  |     | player |     |     |     |     |     |     |     |
| ---------- | --------- | --------------- | --- | ---------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| transfers, | and other | variables       |     | that could | influence |     | match  |     |     |     |     |     |     |     |
resentandanalyzethecausalrelationshipsbetweenvarious
dynamics.
factorsinfluencingfouls.Thesefactorsmayincludeteams’
Thedatasetnotonlyaddressesvariabilitybetweenteams
historicalfoulpatterns,tacticalstrategies,playerbehaviors,
| and players | but | also encompasses |     | the | tactical | and strategic |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andinteractionsbetweenopposingteams.
| diversity | characteristic |     | of La | Liga. It | includes | information |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ----- | -------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ByutilizingBNs,wecancapturetheconditionaldepen-
| from different | seasons, |     | teams, | and playing | styles, | ensuring |     |     |     |     |     |     |     |     |
| -------------- | -------- | --- | ------ | ----------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
denciesbetweenthesevariables,allowingforamoreaccurate
| that the | model can | adapt | to a | wide range | of  | situations | and |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ---- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
andinterpretablemodeloftheunderlyingprocessesthatlead
| contexts | in Spanish | football. |     | This temporal |     | focus | and the |          |     |               |            |         |       |         |
| -------- | ---------- | --------- | --- | ------------- | --- | ----- | ------- | -------- | --- | ------------- | ---------- | ------- | ----- | ------- |
|          |            |           |     |               |     |       |         | to fouls | in  | a match. This | is crucial | for our | study | because |
breadthofdatasupportstherobustnessandapplicabilityof
foulsareinfluencedbyacombinationofteam-specificchar-
thestudyintheacademicrealm.
|     |     |     |     |     |     |     |     | acteristics |     | and the dynamic | interplay | during | a game. | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --------- | ------ | ------- | --- |
probabilisticnatureofBNsenablesustoincorporateuncer-
3.1 BayesianNetworks
taintyandvariabilityinherentinsportsdata,leadingtomore
robustpredictionscomparedtodeterministicmodels.
| A BN              | is presented | as           | a concise    | representation |               |           | of the  |     |            |     |     |     |     |     |
| ----------------- | ------------ | ------------ | ------------ | -------------- | ------------- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
| joint probability |              | distribution |              | of a set       | of random     | variables |         |     |            |     |     |     |     |     |
|                   |              |              |              |                |               |           |         | 3.2 | NaiveBayes |     |     |     |     |     |
| X = {X            | ,...,X       | }, where     | independence |                | relationships |           | are     |     |            |     |     |     |     |     |
|                   | 1            | n            |              |                |               |           |         |     |            |     |     |     |     |     |
| encoded           | in the       | structure    | of an        | underlying     | directed      |           | acyclic |     |            |     |     |     |     |     |
ANBclassifierispresentedasaBNthatincludesadiscrete
| graph (DAG) | [30, | 31]. In | simple | terms, | a BN | is defined | as  |        |          |       |                    |           |           |     |
| ----------- | ---- | ------- | ------ | ------ | ---- | ---------- | --- | ------ | -------- | ----- | ------------------ | --------- | --------- | --- |
|             |      |         |        |        |      |            |     | target | variable | C and | a set of predictor | variables | (continu- |     |
(G,P),
| a pair                                               | where | G   | constitutes | a   | DAG, | and P | is a set |                |     | ,...,X |                                |     |     |     |
| ---------------------------------------------------- | ----- | --- | ----------- | --- | ---- | ----- | -------- | -------------- | --- | ------ | ------------------------------ | --- | --- | --- |
|                                                      |       |     |             |     |      |       |          | ousordiscrete) |     | X      | n .Thegoalofthisclassifieristo |     |     |     |
| ofconditionalprobabilitydistributions(CPDs).NodesinG |       |     |             |     |      |       |          |                |     | 1      |                                |     |     |     |
determinetheprobabilitythatanobjectwithobservedchar-
representrandomvariablesin X,whilelinksbetweenpairs ={x ,x ,...,x }belongstoeachclassC =c
|                                                  |     |     |     |                       |       |          |     | acteristicsx |     | 1 2               | n           |     |     | j   |
| ------------------------------------------------ | --- | --- | --- | --------------------- | ----- | -------- | --- | ------------ | --- | ----------------- | ----------- | --- | --- | --- |
| ofnodesindicatestatisticaldependencies.EachnodeX |     |     |     |                       |       |          | has |              |     |                   |             |     |     |     |
|                                                  |     |     |     |                       |       |          | i   | andreturnc   |     | ∗ ,the mo stproba | bleone[32]: |     |     |     |
|                                                  |     |     |     | p(X                   | |Pa(X | )),where |     |              |     |                   |             |     |     |     |
| anassociatedprobabilitydistribution              |     |     |     |                       | i     | i        |     |              |     |                   |             |     |     |     |
| Pa(X )denotestheparentsof                        |     |     |     | X intheDAGG.Following |       |          |     | ∗            |     |                   |             |     |     |     |
| i                                                |     |     |     | i                     |       |          |     | c =argmaxp(C |     | =c                | | x).       |     |     | (2) |
j
| thefactorizationencodedintheDAG,thejointdistribution |           |        |         |              |     |        |       |     |     | j   |     |     |     |     |
| ---------------------------------------------------- | --------- | ------ | ------- | ------------ | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| over all                                             | variables | in the | network | is expressed |     | as the | prod- |     |     |     |     |     |     |     |
uct of the CPDs associated with each node, such that for Various restricted DAG structures have been proposed to
addresspredictiontaskswiththeaimofreducingthenumber
| x ={x | ,...,x | }   |     |     |     |     |     |               |          |                 |                   |            |             |       |
| ----- | ------ | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------------- | ----------------- | ---------- | ----------- | ----- |
| 1     | n      |     |     |     |     |     |     |               |          |                 |                   |            |             |       |
|       |        |     |     |     |     |     |     | of parameters |          | to be estimated | from              | data while | maintaining |       |
|       |        |     |     |     |     |     |     | model         | accuracy | [32,            | 33]. The simplest | case       | is the      | NB, a |
(cid:2)n
p(X = x)= p(X = x |Pa(x )), (1) fixedstructurewheretheclassvariableC istheparentofall
|     |     | i   | i   | i   |     |     |     |                                |     |     |         |     |                |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ------- | --- | -------------- | --- |
|     |     |     |     |     |     |     |     | remainingexplanatoryvariablesX |     |     | ,...,X  |     | .Inotherwords, |     |
|     | i=1 |     |     |     |     |     |     |                                |     |     | 1       | n   |                |     |
|     |     |     |     |     |     |     |     | therearenlinkspointingfromC    |     |     | toeachX | i   | ,assuminginde- |     |
where Pa(x ) denotes the values of the parents of X pendence between predictors given C. Despite the strong
|     | i   |        |     |     |     |     | i   |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ={x | ,...,x | }.  |     |     |     |     |     |     |     |     |     |     |     |
expressedinx 1 n assumptionofindependence,itisoffsetbythereductionin
Figure 1 illustrates an example of a BN. In this particu- thenumberofparameterstobeestimatedfromthedata.The
larscenario,threevariables X 1 , X 2 ,and X 3 areconsidered, posteriorprobabilitydistributionovertheclassvariableC is
whereX andX directlydependonX .Thecorresponding calculatedasfollows:
|          | 2       | 3           |     |       | 1              |     |       |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ----- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| directed | acyclic | graph (DAG) |     | shows | the dependency |     | rela- |     |     |     |     |     |     |     |
(cid:2)n
tionshipsbetweenthevariables,whereeachnoderepresents
|     |     |     |     |     |     |     |     | p(C | =c  | | x)∝ p(C | =c ) p(x | |C =c | ).  | (3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     | j   |           | j        | i     | j   |     |
avariable,andarrowsindicatethedirectionofdependence.
i=1
| BNs | are particularly |     | well-suited | for | modeling | complex |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
probabilistic relationships among variables, especially in There are more elaborate structures, such as k-dependency
domainswhereuncertaintyandinterdependenciesarepromi- Bayesian classifiers (k-BD), that relax the independence
nent. In the context of predicting the number of fouls in assumption by allowing each feature to have up to k addi-
footballmatches,BNsprovideastructuredframeworktorep- tionalparentsinadditiontotheclassvariable.NBisaspecial
123

| ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |     |     |     |     |     |     |     |     |     | 193 |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
=
caseofk-BDs,wherek 0[34].Learningthestructureof stands as a valuable tool for addressing the inherent
restricted models can be done from data using constraint- uncertainty in the distribution of continuous variables,
basedtechniquesorgreedysearchtechniques[35,36].These offeringarobustapproachtoaccuratelyestimateparam-
approachescanalsobeemployedtolearnunrestrictedstruc- eters in the absence of detailed information about the
tures, i.e., those that do not distinguish a class variable. specificshapeofthedistribution.
However,thesetechniquesareoftencomputationallyexpen-
sive and more challenging to implement. Nevertheless, the 3.3 Measurementofmodelgoodness
| BN model | has consistently |     | demonstrated |     | excellent |     | perfor- |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | ------------ | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
manceinclassificationproblems. Evaluating the quality of a prediction model in the context
|     |     |     |     |     |     |     |     | of football | presents | specific | challenges | that | depend | on the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | ---------- | ---- | ------ | ------ |
•
For a discrete variable, the conditional probability is nature of the target variable. This work addresses two dis-
estimated by counting the occurrences of each value of tinctissues:(1)predictingthenumberoffouls,treatedasan
thepredictorvariablegivenaspecificvalueoftheclass ordinalvariablebysplittingitintointervals;and(2)predict-
variable. Suppose we have a discrete variable X and a ingdraws,wherethereisastrongclassimbalancebetween
classvariableC.Tocalculatetheconditionalprobability “draw” and “not draw.” The following sections outline the
p(X = x|C = c), instances in the training data where evaluationmethodologiesproposedforeachscenario,high-
X takesthevaluex andC takesthevaluecarecounted, lightingthecriteriabehindtheirselectionandhowtheyare
| and this | count | is then | divided | by  | the total | number | of  | implemented. |     |     |     |     |     |     |
| -------- | ----- | ------- | ------- | --- | --------- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
=
| occurrencesofC |     |     | c.Thisrelationshipisexpressedas |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
follows: 3.3.1 EvaluationinFoulPrediction:RankProbabilityScore
|     |     |     | (cid:3) |       |     |     |     | (RPS) |     |     |     |     |     |     |
| --- | --- | --- | ------- | ----- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     | (X      | = x,C | =c) |     |     |       |     |     |     |     |     |     |
(cid:3)
| p(X = | x|C =c)= |     |     |        | .   |     | (4) |                 |               |             |           |       |           |          |
| ----- | -------- | --- | --- | ------ | --- | --- | --- | --------------- | ------------- | ----------- | --------- | ----- | --------- | -------- |
|       |          |     |     | (C =c) |     |     |     |                 |               |             |           |       |           |          |
|       |          |     |     |        |     |     |     | When predicting |               | the number  | of fouls, | it is | essential | to use   |
|       |          |     |     |        |     |     |     | a metric        | that reflects | the ordinal | character |       | of the    | classes. |
• Inthecaseofacontinuousvariable,itisassumedthatthe
|     |     |     |     |     |     |     |     | Many probabilistic |     | models | applied | to football | adopt | eval- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------- | ----------- | ----- | ----- |
variablefollowsaspecificdistribution,suchasthenormal uation methods that do not acknowledge that their outputs
| distribution. | Instead |     | of counting | occurrences, |     | estimates |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | ----------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
representanorderedscale[15].Toaddressthisshortcoming,
oftheparametersoftheconditionaldistributionarecalcu- theRPSisused,whichisrecommendedforsettingsinvolving
latedforeachvalueoftheclassvariable.Foracontinuous
ordinalvariables[8,40].
variableX andaclassvariableC,statisticalmethodscan The“fouls”variableisdividedintofourclasses,defined
beusedtoestimatetheparametersoftheconditionaldis-
bythe25th,50th,and75thpercentilesofthenumberoffouls
tribution, such as the mean and standard deviation for recordedinthe2010-2011and2011-2012seasons.
| a normal | distribution. |     | Once | the parameters |     | have | been |        |         |         |        |          |           |       |
| -------- | ------------- | --- | ---- | -------------- | --- | ---- | ---- | ------ | ------- | ------- | ------ | -------- | --------- | ----- |
|          |               |     |      |                |     |      |      | Figure | 2 shows | how the | number | of fouls | (vertical | axis) |
estimated, the corresponding probability density func- evolvesacrossthecumulativeindexofmatches(horizontal
tioncanbeusedtocalculatetheconditionalprobability
|     |     |     |     |     |     |     |     | axis). Each | point’s | color indicates |     | the foul | range | class as |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --------------- | --- | -------- | ----- | -------- |
definedbythe25th,50th,and75thhistoricalpercentiles.
| p(X = | x|C =c)= |     | f(x|μ | ,σ ). |     |     | (5) |                                                    |     |     |     |     |     |     |
| ----- | -------- | --- | ----- | ----- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|       |          |     |       | c c   |     |     |     | Thisyieldsthefollowingintervals:0to25fouls,25to30, |     |     |     |     |     |     |
30to35,andabove35.RPSallowsforevaluatingthequality
| Here, | f(x|μ | ,σ ) | represents | the | probability |     | density |                                                      |     |     |     |     |     |     |
| ----- | ----- | ---- | ---------- | --- | ----------- | --- | ------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|       |       | c c  |            |     |             |     |         | oftheassignedprobabilitiesforeachofthesefoursegments |     |     |     |     |     |     |
|       |       |      |            | =   | μ           | σ   |         |                                                      |     |     |     |     |     |     |
function of X given that C c, and c and c are the bycomparingthepredictedprobabilitydistributionwiththe
estimatedparametersoftheconditionaldistributionasso-
observeddistributioninacumulativemanner.
=c.
| ciatedwithC    |     |          |     |              |     |          |      | ThegeneralformulaforRPSisasfollows: |     |         |     |         |     |     |
| -------------- | --- | -------- | --- | ------------ | --- | -------- | ---- | ----------------------------------- | --- | ------- | --- | ------- | --- | --- |
| • Particularly | in  | the case | of  | a continuous |     | variable | with |                                     |     |         |     |         |     |     |
|                |     |          |     |              |     |          |      |                                     |     | (cid:5) |     | (cid:6) |     |     |
an unknown distribution, one may choose to estimate (cid:4)J (cid:4)N (cid:4)N 2
1
it using the method of Mixtures of Truncated Basis RPS = H − H ˆ , (6)
|                                                      |           |              |          |             |          |     |         |        | ×   |         | ij  | ij  |     |     |
| ---------------------------------------------------- | --------- | ------------ | -------- | ----------- | -------- | --- | ------- | ------ | --- | ------- | --- | --- | --- | --- |
|                                                      |           |              |          |             |          |     |         | N      | J   |         |     |     |     |     |
| Functions(MoTBFs).Thisapproachinvolvesmodeling       |           |              |          |             |          |     |         |        |     | j=1 i=1 | i=1 |     |     |     |
| the distribution                                     |           | as a         | weighted | combination |          | of  | various |        |     |         |     |     |     |     |
| truncatedbasisfunctions,providingflexibilitytoaccom- |           |              |          |             |          |     |         | where: |     |         |     |     |     |     |
| modate                                               | different | distribution |          | shapes      | [37–39]. |     | Param-  |        |     |         |     |     |     |     |
•
eter estimation in this context is performed through N isthenumberofclasses.
advanced techniques that look for the maximum like- • J isthenumberofevents.
•
lihood,enablingeffectiveapproximationevenwhenthe H ij is the observed cumulative function for class i in
exactformofthedistributionisunknown.Thismethod event(ormatch) j
123

| 194 |     |     |     |     |     | ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
Fig.3 Dynamicthresholdusedfordrawclassificationasthehistorical
Fig.2 Scatter-plotofallLaLigamatchesinthesample.X-axis:cumu- datagrow.Thesamplecontains1136drawsand3424non-draws(IR=
| lative match  | index (chronological | order    | from 2010-11 | to 2021-22).         | 3.02:1) |     |     |     |     |     |
| ------------- | -------------------- | -------- | ------------ | -------------------- | ------- | --- | --- | --- | --- | --- |
| Y-axis: total | number of fouls      | recorded | in each      | match (larger values |         |     |     |     |     |     |
| appear lower  | on the axis because  | the      | scale is     | inverted to enhance  |         |     |     |     |     |     |
colourcontrast).Pointsarecolouredaccordingtothefoul-countinterval
makesthisratioexplicitbycolouring3424negativeinstances
definedbythe25th,50thand75thhistoricalpercentiles,whichserve
inredand1136positiveonesingreen.Thehorizontalaxis
ascut-pointsforthediscretisationdescribedinSection3.4.1
issimplythecumulativeindexofthematches,from0upto
thefinalmatchinourdataset,andtheverticalaxisrepresents
• ˆ
H isthecumulativestepfunctionpredictedbythemodel
| ij           |                 |               |         |               | thethreshold/probabilityusedforclassification. |                   |       |                     |        |            |
| ------------ | --------------- | ------------- | ------- | ------------- | ---------------------------------------------- | ----------------- | ----- | ------------------- | ------ | ---------- |
| forclassi    | inevent j.      |               |         |               |                                                |                   |       |                     |        |            |
|              |                 |               |         |               | This criterion                                 | counters          |       | the bias introduced |        | by the low |
|              |                 |               |         |               | frequency                                      | of the “draw”     | class | and yields          | a more | balanced   |
| RPS measures | the discrepancy |               | between | the predicted |                                                |                   |       |                     |        |            |
|              |                 |               |         |               | division                                       | between positives |       | and negatives       | in the | evaluation |
| and observed | cumulative      | probabilities | across  | all classes,  |                                                |                   |       |                     |        |            |
set.Asaresult,themodel’sactualcapacitytodetectmatches
| penalizing | large deviations | more | heavily | than small ones. |     |     |     |     |     |     |
| ---------- | ---------------- | ---- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
thatwillendinadrawismoreaccuratelymeasured.
| By normalizing | over the | total number | of  | events, it enables |     |     |     |     |     |     |
| -------------- | -------- | ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Toquantifythequalityofpredictionsinthisimbalanced
straightforwardcomparisonofdifferentmodels.Thismeans
scenario,twospecificmetricsareemployed:WeightedAccu-
| that the model | is not only | evaluated | on whether | it exactly |     |     |     |     |     |     |
| -------------- | ----------- | --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
racy(WAP)andWeightedRecall(WAR).Bothrelyongiving
matchesthetrueclass,butalsoonhowfaroffthepredicted
|     |     |     |     |     | greater weight | to the | minority | class, thus | offering | a more |
| --- | --- | --- | --- | --- | -------------- | ------ | -------- | ----------- | -------- | ------ |
classisfromtheobservedone,whichisparticularlyimpor-
equitablereflectionofthemodel’soverallperformance.
tantforordinalcategories.
Class-frequencyweighting.Tocompensatefortheskew,we
3.3.2 EvaluationinDrawPrediction:MetricsforImbalanced settheweightsinverselyproportionaltoclassprevalence:
Data
|     |     |     |     |     |     | N notdraw |     |     | N draw |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | ------ | --- |
|     |     |     |     |     | Pw= |           | ,   | Nw= |        | .   |
|     |     |     |     |     | N   | +N        |     | N   | +N     |     |
Drawpredictionfacesastronglyimbalancedclassproblem: draw notdraw draw notdraw
drawsaccountforasmallerfractionofallpossibleoutcomes
|                  |          |       |            |              | Withthefinalcountsabove,Pw |     |     | = 0.751andNw |     | = 0.249. |
| ---------------- | -------- | ----- | ---------- | ------------ | -------------------------- | --- | --- | ------------ | --- | -------- |
| in most football | leagues, | while | wins (home | or away) are |                            |     |     |              |     |          |
Thesameformulaisrecomputedoneachrollingwindowso
| far more frequent | [13, 14]. | In such | scenarios, | conventional |     |     |     |     |     |     |
| ----------------- | --------- | ------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
thatweightingandthresholdremainconsistentduringtem-
metricslikeaccuracycanbemisleading,astheyfailtoreflect
poralevaluation.
thedifficultyofcorrectlypredictingtheminorityclass.
Foreachmatch,wecalculatetheaveragedrawrateupto WeightedAccuracy(WAP).WAPiscomputedastheaccu-
thatpoint.Ifthemodel’spredictedprobabilityishigherthan
|     |     |     |     |     | racy for | each class | —positive | and negative— | weighted | by  |
| --- | --- | --- | --- | --- | -------- | ---------- | --------- | ------------- | -------- | --- |
thisaverage,thematchisclassifiedas“draw”(positiveclass); thatclass’sproportioninthetestset.Itisdefinedas:
otherwise,itisclassifiedas“notdraw”(negativeclass).This
dynamic threshold improves calibration by adapting to the TP×Pw
|                                      |     |     |     |     | WAP= |             |     | ,   |     | (7) |
| ------------------------------------ | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- |
| temporalevolutionofthedrawfrequency. |     |     |     |     |      | TP×Pw+FP×Nw |     |     |     |     |
Drawsrepresent24.9%ofthe4560matchesanalysed,so
| theglobalimbalanceratioisIR |     | =   | Nnotdraw | =3.02:1.Figure3 | where: |     |     |     |     |     |
| --------------------------- | --- | --- | -------- | --------------- | ------ | --- | --- | --- | --- | --- |
Ndraw
123

| ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 195 |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•
TPisthecountoftruepositives(matchesthatwereactu-
allydrawsandwereclassifiedassuch),
•
FPisthecountoffalsepositives(matchesthatwerenot
drawsbutwereclassifiedasdraws),
•
Pwistheweightassignedtothepositiveclass(draw),
• Nwistheweightassignedtothenegativeclass(notdraw).
Thismetrichighlightsthemodel’sabilitytocorrectlyidentify
| the positive | class, | taking | into | account | its | frequency | in the |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | ---- | ------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
dataset.
WeightedRecall(WAR).WARfocusesonthemodel’scapac-
ity to correctly capture the positive instances in relation to Fig.4 Relativedistancefromanelementtoeachoneoftheadjacent
| thetotaloftruepositivesandfalsenegatives: |     |     |     |     |     |     |     | centroids |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
TP×Pw
| WAR= |     |     |     | ,   |     |     |     |                                                     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|      |     |     |     |     |     |     | (8) | Conventionalclusteringalgorithmsaimtogenerategroups |     |     |     |     |     |     |     |
TP×Pw+FN×Pw
thatareashomogeneousaspossible.However,inthedevel-
opmentofaprobabilisticNBclassifier,theobjectiveisnotto
whereFNisthecountoffalsenegatives(matchesthatended
maximizewithin-grouphomogeneitybutrathertomaximize
inadrawbutwereclassifiedas“notdraw”).WARtherefore
thedifferencebetweenconsecutivegroups[25,41].
measureshowmuchoftheminorityclass(draws)themodel
Incontrasttotheseconventionalapproaches,wepropose
candetect,weightedbytheclass’simportanceinthedataset.
assigningtherelativedistancesofanelementtoitstwoadja-
| These      | weighted       | indicators |          | are | particularly | suitable | for      |               |     |       |         |                 |     |             |     |
| ---------- | -------------- | ---------- | -------- | --- | ------------ | -------- | -------- | ------------- | --- | ----- | ------- | --------------- | --- | ----------- | --- |
|            |                |            |          |     |              |          |          | cent clusters | and | using | them in | the probability |     | calculation |     |
| imbalanced | classification |            | problems |     | because      | they     | penalize |               |     |       |         |                 |     |             |     |
process.Inourproposal,weadoptadiscretizationapproach
| errors in | the | minority | class | more | heavily | and | provide a |     |     |     |     |     |     |     |     |
| --------- | --- | -------- | ----- | ---- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedonassigningrelativedistancesfromanelementtoits
morebalancedassessmentofthemodel’sperformance.Sev-
twoadjacentclusters.Wedividefoulclassificationsintoseg-
| eral studies | underscore |     | the | usefulness | of  | these | metrics in |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | ---------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
mentsofuniformmagnitude;inourcase,wehaveselected
scenarioswithasymmetricdatadistributions,suchasfraud
fiveclusters,eachwithamagnitudeoffour.Eachclusterrep-
detectionormedicaldiagnosis,andtheyareequallyvaluable
resentsaspecificrangeofaveragefoulscommittedbyteams.
forforecastingdrawsinfootball.
Byassigningateamtoaparticularcluster,wedetermineits
membershiplevelrelativetobothadjacentclustersthrough
3.4 DiscretizationofComponents
thedistancefromitsaveragefoulstoeachofthetwocluster
centroids.
| The discretization |            | of     | variables | is     | essential | in         | building a |      |           |              |     |          |            |           |     |
| ------------------ | ---------- | ------ | --------- | ------ | --------- | ---------- | ---------- | ---- | --------- | ------------ | --- | -------- | ---------- | --------- | --- |
|                    |            |        |           |        |           |            |            | This | weighting | of distances |     | reflects | the team’s | relation- |     |
| Bayesian           | classifier | (Naive |           | Bayes, | NB) or    | a Bayesian | net-       |      |           |              |     |          |            |           |     |
shiptobothclusters,yieldingamorenuanceddiscretization.
| work (BN) | aimed | at  | predicting | different |     | events | in football |                               |     |     |     |      |                  |     |     |
| --------- | ----- | --- | ---------- | --------- | --- | ------ | ----------- | ----------------------------- | --- | --- | --- | ---- | ---------------- | --- | --- |
|           |       |     |            |           |     |        |             | Figure4illustratesthis,wherec |     |     |     | andc | representthecen- |     |     |
i i+1
| (fouls or | draws). | Below, | we  | describe | two | complementary |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
troidsofthetwoclustersnearesttotheteam’saveragefouls.
| approaches  | for          | carrying | out      | this       | discretization. |           | The first |                   |          |              |            |              |               |     |        |
| ----------- | ------------ | -------- | -------- | ---------- | --------------- | --------- | --------- | ----------------- | -------- | ------------ | ---------- | ------------ | ------------- | --- | ------ |
|             |              |          |          |            |                 |           |           | The relative      | distance | of           | an element | to           | each adjacent |     | clus-  |
| focuses     | on assigning |          | relative | distances  | to              | adjacent  | clusters  |                   |          |              |            |              |               |     |        |
|             |              |          |          |            |                 |           |           | ter is calculated |          | by weighting |            | the distance | from          | the | team’s |
| to estimate | the          | number   | of       | fouls; the | second          | addresses | the       |                   |          |              |            |              |               |     |        |
averagefoulstoeachcentroid.Thisprocessprovidesamore
definitionandselectionofoptimalclustersfordrawpredic-
flexibleandadaptivediscretization,capturingdatadistribu-
tion.
|     |     |     |     |     |     |     |     | tion variability |     | based on | the team’s | specific | relationship |     | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---------- | -------- | ------------ | --- | --- |
itssurroundingclusters.
3.4.1 DiscretizationBasedonRelativeDistancetoTwo Let{c ,c ,c ,c ,c }bethecentroidsoftheclusterscon-
|     |     |     |     |     |     |     |     |     | 1 2 | 3 4 5 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Clusters(FoulPrediction)
|     |     |     |     |     |     |     |     | taining the | average | fouls | of the | 4n teams, | sorted | according |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | ------ | --------- | ------ | --------- | --- |
totheiraveragefouls.
RelativeDistanceofanElementtoTwoClusters
Toassigntherelativemembershiplevelofanelementx,
Within the framework of the addressed problem, a chal- wetakeitstwonearestclustersc andc andcalculatethe
|     |     |     |     |     |     |     |     |     |     |     |     | i   | i+1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lengeariseswhendiscretizingelementsbasedontheaverage
membershiplevelofxtoeachclusterviaitsaveragedistance
| classificationoffoulsreceivedandcommittedbyteamsinthe |     |     |     |     |     |     |     | totheircentroids: |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
NBclassifier.Assigningarankingto20teamsaccordingto
t he i r av e r a g e f o u ls is p r o p o se d , y e t th e r e i sn o s ingle,optimal | x − c | | x − c + |
|     |     |     |     |     |     |     |     | w = | i   | , w | =   | i 1 , |     |     | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
m e t ho d o l o g y f o r ca rr y i n g o u t th i s a ss i g n m e nt . i − i+1 −
|     |     |     |     |     |     |     |     | c i | c i+ 1 |     | c i | c i + 1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------- | --- | --- | --- |
123

| 196 |     |     |     |     |     |     |     | ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
wherew andw
|             | i   | i+1 sumtoone: |          |     |             |      |     |     |     |     |     |
| ----------- | --- | ------------- | -------- | --- | ----------- | ---- | --- | --- | --- | --- | --- |
|             | (x  | −c ) +        | (c +     | −x) |             |      |     |     |     |     |     |
| w +w        | =   | i             | i 1      | =1. |             | (10) |     |     |     |     |     |
| i i+1       |     |               | −        |     |             |      |     |     |     |     |     |
|             |     | c i+          | 1 c i    |     |             |      |     |     |     |     |     |
| Sensitivity | and | rationale.    | Although | the | final model | uses |     |     |     |     |     |
five foul-intervals of four teams each, we tested alterna- Fig.5 NBforclusterselectionofaNBclassifier
tivegranularitiesbetweenthreeandsevenbins.Fewerthan
fivebinsblurredtheordinalstructure,whilemorethanfive
producedverysmallcellfrequenciesandunstablelikelihood theordinaltarget,keepingthesamefourresultingintervals
whenpossible.
estimates,sothefive-intervaloptionwasretainedasthemost
| robust. This | choice | is also | grounded | on a       | hybrid | Sturges- |     |     |     |     |     |
| ------------ | ------ | ------- | -------- | ---------- | ------ | -------- | --- | --- | --- | --- | --- |
|              |        |         |          | (B = 1+log |        | N)       |     |     |     |     |     |
percentile rule: Sturges’ formula 2 gives 3.4.2 ComponentDiscretizationforDrawPrediction
| an upper | bound | of five | bins for | N = 20, | and quartile | cut- |     |     |     |     |     |
| -------- | ----- | ------- | -------- | ------- | ------------ | ---- | --- | --- | --- | --- | --- |
points ensure that each class preserves at least 20 % of the When forecasting draws, the discretization process focuses
observations-wellabovetheempiricalminimumrequiredfor ontwoNBcomponents:thehistoricalclassificationandthe
reliable NB parameter estimation. Hence, the adopted dis- current classification of teams. The main challenge is to
cretisation maximises class separability without sacrificing assignarankingto20teamsbasedontheiraveragepoints.As
statistical stability, fully aligning with the goal of boosting inthefoulsscenario,thereisnosingle,optimalmethodfor
unidimensionalNBefficiency. suchassignment;theemphasisisonmaximizingthediffer-
|             |     |             |             |     |         | w     | encebetweenconsecutivegroupsratherthanonmaximizing |     |     |     |     |
| ----------- | --- | ----------- | ----------- | --- | ------- | ----- | -------------------------------------------------- | --- | --- | --- | --- |
| Calculation | of  | Conditional | Probability |     | through | i and |                                                    |     |     |     |     |
internalhomogeneity.
| w i+1 Once         | the weights |      | that assign                  | an element | x to | its two |                        |     |     |     |     |
| ------------------ | ----------- | ---- | ---------------------------- | ---------- | ---- | ------- | ---------------------- | --- | --- | --- | --- |
| adjacentclusters(w |             | andw |                              |            |      |         |                        |     |     |     |     |
|                    |             | i    | i+1 )aredetermined,weproceed |            |      |         | ClusterQualityMeasures |     |     |     |     |
tocalculatetheconditionalprobabilityasfollows.
Acomplementarystrategyfordiscretizingthesecompo-
Let M denote the event that the element x belongs to a nentsinvolvesdefiningspecificclusteringqualitymeasures:
specifichypothesisorclass(e.g.,oneofthefoulintervals).
|     |     |     |     |     |     | P(M | |   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UnderastandardBayesianframework,wecompute
|     |     |     |     |     |     |     | • Minimumdistancebetweenclustercentroids:theaimis |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
x)byBayes’rule:
|     |     |     |     |     |     |     | to maximize | the      | distance between   | consecutive | groups’ |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------------------ | ----------- | ------- |
|     |     |     |     |     |     |     | centroids,  | ensuring | a clear separation | between     | varying |
P(x | M)P(M)
| P(M |x)= |     |          |     |               | .   |     |                                 |                |           |               |       |
| -------- | --- | -------- | --- | ------------- | --- | --- | ------------------------------- | -------------- | --------- | ------------- | ----- |
|          | P(x | | M)P(M) | +   | P(x |¬M)P(¬M) |     |     | strengthlevelsindrawprediction. |                |           |               |       |
|          |     |          |     |               |     |     | • Maximum                       | within-cluster | variance: | the objective | is to |
(11)
minimizethismaximumtoguaranteestronghomogene-
itywithineachgroup.
•
| Here, |     |     |     |     |     |     | Difference | in frequencies | between | the cluster | with the |
| ----- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------- | ----------- | -------- |
mostelementsandtheonewiththefewest:thegoalisto
| P(x | | M)=w | P(C | ∧M)+w | P(C | ∧M), |     |                                                 |     |     |     |     |
| ----- | ---- | --- | ----- | --- | ---- | --- | ----------------------------------------------- | --- | --- | --- | --- |
|       |      |     |       | i+1 | i+1  |     | avoidhighlyunbalancedclustersintermsofthenumber |     |     |     |     |
i i
ofelements.
| P(M)=w |     | P(C )+w | i+1 | P(C i+1 ), |     |     |     |     |     |     |     |
| ------ | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
i i
| w   | w   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where i and i+1 represent the relative membership of x These measures are normalized for proper comparison,
inthecentroidsc andc ,respectively(seeSection3.4.1). ensuringeachtakesavaluein[0,1].Subsequently,athree-
|     |             | i i+1 |                             |     |     |     |     |     |     |     |     |
| --- | ----------- | ----- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | P(x |¬M)and |       | P(¬M)aredefinedanalogously, |     |     |     |     |     |     |     |     |
Similarly, nodeNBclassifier(onenodeperqualitymeasure)isusedto
byconsideringthecomplementaryevent¬M. predictthe“goodness”ofeachclusteringcombination(Fig-
| Byleveragingtheproximityofx |     |     |     | toitstwoadjacentclus- |     |     | ure5). |     |     |     |     |
| --------------------------- | --- | --- | --- | --------------------- | --- | --- | ------ | --- | --- | --- | --- |
ters,theseweightsw andw letthemodelcapturelocal EachclusteringcombinationisfedintothisNBalongwith
|     |     | i   | i+1 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
variabilitymoreeffectively.Consequently,theNBclassifier itscorrespondingmeasureofmodel“goodness”(converted
incorporatesthesedistancesintotheposteriorprobabilitycal- toabinaryvariable:1ifexceedingtheaveragegoodness,0
culation,offeringgreaterflexibilityandinterpretabilitythan otherwise).Thus,theclassifierdeterminestheoptimalcluster
conventionalclustering-baseddiscretizationalone. configurationfortheNBaimingtopredictdraws.
Tohaveawidelyacceptedpointofcomparison,thesame Thehistoricalandcurrentrankingvariableswerelikewise
attributes were also discretized using the MDL algorithm discretized using the Fayyad & Irani MDL algorithm [29].
[29]. This discretizer was applied as a preprocessing filter TheimpactofthisdiscretizationonWAPandWARmetrics
beforetrainingtheclassifier,withoutusinginformationfrom wasthenevaluated.
123

| ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |     |     |                                |     |                   |                     |        | 197     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ----------------- | ------------------- | ------ | ------- |
|                                                  |     |     |     |     |     |     | 3. Discretisation.             | The | relative-distance |                     | scheme | of Sec- |
|                                                  |     |     |     |     |     |     | tion3.4.1placeseachteaminoneof |     |                   | fivefoul-propensity |        |         |
clusters(fourclubspercluster)andassignsthemember-
|     |     |     |     |     |     |     | shipweights(w | ,w i+1 | )thatquantifyitsproximitytothe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------------------------------ | --- | --- | --- |
i
twoborderingcentroids.
|     |     |     |     |     |     |     | 4. Probability | calculation. | The | NB combines |     | the eight |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | ----------- | --- | --------- |
weightedpredictors(fourfoulindicators×twoweights)
|     |     |     |     |     |     |     | plus the | two “rank vs | rank” codes | to yield | the | posterior |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ----------- | -------- | --- | --------- |
Fig.6 NBclassifierstructureforpredictingthenumberoffouls
probabilitythatthematchtotalwillfallineachofthefour
foul-intervalclassesdefinedinSection3.5.1.
3.5 ClassifierConstructionandProbability
Calculation
|     |     |     |     |     |     |     | 3.5.2 PredictionofaDrawinfootballMatches |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
Thissectiondescribeshowtheabovediscretizationmethods
integrateintoaBayesianapproachtopredict(1)thenumber Here the class variable takes the values draw / not-draw;
|     |     |     |     |     |     |     | every predictor | is recorded | for the | two rivals, | so  | the model |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ------- | ----------- | --- | --------- |
offoulsand(2)drawvs.non-drawoutcomes.
|     |     |     |     |     |     |     | always“sees”thepair | (home,away). |             |      |            |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ------------ | ----------- | ---- | ---------- | --- |
|     |     |     |     |     |     |     | Following           | the previous | discussion, | draw | prediction | is  |
3.5.1 PredictionoftheNumberofFoulsinfootballMatches
tackledviaaprobabilisticapproachcombining:
Thetargetvariableistheinterval-valuedtotalnumberof
| fouls | committed | inthe | match (home | + away), | discretised |     |                                                      |     |     |     |     |     |
| ----- | --------- | ----- | ----------- | -------- | ----------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|       |           |       |             |          |             |     | • Goalanalysis:offensive/defensivescoringcapability. |     |     |     |     |     |
intofiveordinalclasses.
|     |     |     |     |     |     |     | • Historicalandcurrentresults:teamclassifications. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
Weaddressthepredictionofthenumberoffoulsinfoot-
|      |         |                 |          |                   |     |     | • Contextualfactors:presenceofregionalderbies. |     |     |     |     |     |
| ---- | ------- | --------------- | -------- | ----------------- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| ball | through | a probabilistic | approach | that incorporates |     | the |                                                |     |     |     |     |     |
classificationsoffoulsreceivedandcommittedbytheteams.
Figure6depictsthe‘FoulsInterval’nodeatthetop,this
|     |     |     |     |     |     |     | 1. Inputvariables: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
isactuallyourclassvariable.InastandardNBstructure,this
•
classnodeactsastheparent,whilethepredictornodes(e.g., Historicalclassification:leaguepositionobtainedby
historical fouls committed, fouls suffered) are its children. thehometeam(rH )andbytheawayteam(rA );the
|     |     |     |     |     |     |     |     | hist |     |     |     | hist |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
The figure is a schematic representation emphasizing that matchisthuslabelled,forexample,as“1vs3”.
the probability of being in a certain fouls interval depends • Currentclassification:analoguepair(rH ,rA )..
|     |     |     |     |     |     |     |     |     |     |     | curr | curr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- |
•
on these predictors. Importantly, the ‘number of fouls’ is Goalestimation:modelingoffensive/defensivecapac-
not modeled as a continuous variable but rather as a cate- ity(oneoftheNBcomponents).
•
goricalvariable withfourintervals.Thus,theNBclassifier Regionalderby:abooleanvariableindicatingwhether
learnsadiscreteprobabilitydistributionP(fouls=k), k = aderbyisplayed.
1,...,4conditionedoneachpredictor’sdiscretizedorcon-
|     |     |     |     |     |     |     | 2. Discretization:asdescribedinSection3.4.2,thefocusis |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
tinuousvalues.
onmaximizinginter-clusterdifferencetocapturedistinct
|     |                    |     |                                |     |     |     | strength | levels, while | preserving | some | internal | homo- |
| --- | ------------------ | --- | ------------------------------ | --- | --- | --- | -------- | ------------- | ---------- | ---- | -------- | ----- |
| 1.  | Inputvariables.For |     | eachside wecollecttwofoul-rate |     |     |     |          |               |            |      |          |       |
geneityandbalancedclustersizes.
indicators:
|     |     |     |     |     |     |     | 3. NB classification: | all | components | are | combined | via a |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---------- | --- | -------- | ----- |
(cid:7)
NB(Figure7),assumingconditionalindependencegiven
|     | Hist.committedH, |     | Hist.sufferedH, |     |     |     |        |                |             |     |             |        |
| --- | ---------------- | --- | --------------- | --- | --- | --- | ------ | -------------- | ----------- | --- | ----------- | ------ |
|     |                  |     |                 |     |     |     | “draw” | or “not draw.” | This yields | the | probability | that a |
(cid:8)
|     | Hist.committedA, |     | Hist.sufferedA | ,   |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
matchwillendinadraw.
where“Hist.”denotestheaverageoverthetwoprevious
seasons.Thesefournumbersaretheprimitivepredictors 3.6 ConclusionoftheUnifiedMethodology
thatfeedtheNB.
2. Ranking.Usingthesamehistoricalaverageswebuilda This methodological section integrates the discretization
positionaltableforthewholeleague;thematchisthere- strategies proposed-assigning relative distances to adjacent
fore tagged as rankH vsrankA (e.g. “4 vs 12”). The clusters (for fouls) and selecting optimal clusters through
|     |     |     | hist hist |        |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | (rankH    | ,rankA | )   |     |     |     |     |     |     |     |
current-season analogue is obtained quality measures (for draws)-as well as the construction of
|     |     |     | curr | curr |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
everymatch-dayandentersthemodelinthesameway. NBclassifiersforbothproblemsettings.
123

| 198 |     |     |     |     |     | ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
Fig.7 NBtomeasure
probabilityofadraw
Table1 Modelperformancefor
|     |     |     | Training | Test | Proposal K-means | F-I | Continuous | MoTBFs | NN  |
| --- | --- | --- | -------- | ---- | ---------------- | --- | ---------- | ------ | --- |
eachseasonusingthetwo
precedingseasonsfortraining
2010-2012 2012-2013 0.0125 0.0144 0.0133 0.0124 0.1738 0.0122
2011-2013 2013-2014 0.0105 0.0139 0.0092 0.0096 0.1171 0.0102
2012-2014 2014-2015 0.0125 0.0126 0.0115 0.0124 0.1415 0.0128
|     |     |     | 2013-2015 | 2015-2016 | 0.0093 0.0113 | 0.009 | 0.0129 | 0.1134 | 0.0122 |
| --- | --- | --- | --------- | --------- | ------------- | ----- | ------ | ------ | ------ |
2014-2016 2016-2017 0.0108 0.0113 0.0098 0.0166 0.1214 0.0152
2015-2017 2017-2018 0.0121 0.0145 0.0107 0.0129 0.1285 0.0163
2016-2018 2018-2019 0.0085 0.0149 0.0081 0.0076 0.0781 0.0128
2017-2019 2019-2020 0.0130 0.0162 0.0111 0.0097 0.1025 0.0170
2018-2020 2020-2021 0.0102 0.0103 0.0094 0.0084 0.0864 0.0147
2019-2021 2021-2022 0.0099 0.0123 0.0091 0.0077 0.0636 0.0144
| •   |     |     |     |     | 4.1 PerformanceoftheFoulPredictionMethod |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
Forfoulprediction,theapproachemphasizesanordinal
| modeling, | leveraging | weights | (w ,w | i+1 ) that reflect | a   |     |     |     |     |
| --------- | ---------- | ------- | ----- | ------------------ | --- | --- | --- | --- | --- |
i
team’sproximitytodifferentfoul-averageranges. This section presents the performance of the NB classifier
• Fordrawprediction,thefocusliesonmaximizingclus- designedtopredictthenumberoffoulsinfootballmatches.
ter separability to better distinguish the minority class Following a rolling window approach, each season was
(“draw”),incorporatingfactorssuchasgoalanalysisand predictedbytrainingthemodelonthetwoimmediatelypre-
regionalderbies. cedingseasons.Table1displaystheperformancemetricsfor
eachseason,wheretheRPSwasemployedtoevaluatepre-
dictiveaccuracy.RecallthatlowerRPSvaluesindicatebetter
| This framework | provides | a   | comprehensive | overview | of  |     |     |     |     |
| -------------- | -------- | --- | ------------- | -------- | --- | --- | --- | --- | --- |
howtohandlecontinuous-variablediscretizationandthecon- performanceinordinalclassificationtasks.
Ourproposeddiscretizationapproachconsistentlyyielded
structionofBayesianclassifiersfordistinctfootballanalytics
phenomena (number of fouls and draw vs. non-draw out- lower RPS values compared to the reference methods.
|     |     |     |     |     | Specifically, | as shown | in Table 1, | the NB model with | our |
| --- | --- | --- | --- | --- | ------------- | -------- | ----------- | ----------------- | --- |
comes).
All the scripts required to reproduce the preprocessing, discretizationstrategyoutperformed:
| training | and evaluation | pipelines | are openly | provided | at  |     |     |     |     |
| -------- | -------------- | --------- | ---------- | -------- | --- | --- | --- | --- | --- |
https://github.com/naicopb/NB-Discretizations-Football. • The NB classifier relying on k-means-based discretiza-
tion,
• TheNBclassifierrelyingonFayyad-Iranidiscretization
| 4 Results |     |     |     |     | (F-I), |     |     |     |     |
| --------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
• ThecontinuousNBmodelthatassumesanormaldistri-
| Beforedelvingintothespecificfindingsforeachpredictive |     |     |     |     | bution(NPD), |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
task, this section outlines the overarching evaluation strat- • The Mixtures of Truncated Basis Functions (MoTBFs)
| egyemployedforourmodels.Webeginwiththeanalysisof |     |     |     |     | model,and |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
foulpredictiontoillustratehowourdiscretizationapproach • Aneuralnetworkusingthesameinputfeatures.
enhancestheordinalclassificationoffoulscommittedduring
amatch.Subsequently,weshiftfocustodrawprediction,a Figure8providesaconsolidatedviewoftheRPSresults
problemcharacterizedbyhighlyimbalancedclasses,where across allseasons.When predicting each match, themodel
weassesstheeffectivenessofweightedperformancemetrics. wasupdatedwiththecumulativehistoricaldataavailableup
Thefollowingtwosubsectionsdetailtheseevaluations,high- to that point. Notably, our approach achieved the smallest
lightingcomparativeresultsagainstestablishedbaselinesand overallRPSof0.00927,outperformingk-meansdiscretiza-
underscoring the improvements brought about by our pro- tion (0.00976), the Fayyad-Irani discretization (0.00977),
posedmethodology. thecontinuous(NPD)model(0.00977),theMoTBFsmodel
123

| ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |     |     |     |     |     |     |     |     |     | 199 |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•
AnNBclassifierthatemploysFayyad-Iranimethodfor
discretization(F-I).
IntermsofWAP,ourapproachachievesthehighestvalues,
anditremainscompetitiveinWARaswell.Thissuggeststhat
theproposedclusteringstrategybetterdifferentiatesbetween
drawsandnon-drawscomparedtok-means-basedsegmen-
tationorfullycontinuousmodeling.Thesefindingsconfirm
|     |     |     |     |     | the | utility | of emphasizing |     | inter-class |     | separation | when | dis- |
| --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ----------- | --- | ---------- | ---- | ---- |
cretizingcomponentsinNBclassifiers.
|     |     |     |     |     |         | To gauge | the      | specific | contribution |           | of       | this contextual |      |
| --- | --- | --- | --- | --- | ------- | -------- | -------- | -------- | ------------ | --------- | -------- | --------------- | ---- |
|     |     |     |     |     | feature |          | Regional | derby,   | we           | ran an    | ablation | in which        | the  |
|     |     |     |     |     | binary  | Regional |          | derby    | (RD)         | indicator | was      | omitted.        | Der- |
biesaccountforonly5%ofthematches,soglobalmetrics
Fig.8 OverallRPSresultsforalltheseasonsusedtodevelopthemodel
|     |     |     |     |     | changed |     | marginally. | When |     | the evaluation |     | is restricted | to  |
| --- | --- | --- | --- | --- | ------- | --- | ----------- | ---- | --- | -------------- | --- | ------------- | --- |
derbymatches,however,RDprovesuseful:WAPrisesfrom
|     |     |     |     |     | 0.369 |     | 0.398 |         |      | 0.519 | 0.534. |        |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ------- | ---- | ----- | ------ | ------ | --- |
|     |     |     |     |     |       | to  |       | and WAR | from |       | to     | Hence, | RD  |
(0.02725), and the (NN) neural network (0.11249). These addsdiscriminativepowerexactlywhereitisexpected,with-
findings emphasize the effectiveness of our discretization outaffectingoverallperformance.
strategyincapturingtheordinalnatureoffouls.
The inter-season pattern shown in Table 1 reveals that 4.2.2 ComparativeAnalysisofPredictionModels
| the advantage | of  | the proposed | scheme is preserved | even in |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | ------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
campaignswithregulatorychanges(e.g.,2016-17)oralower Finally,wecompareourforecastingapproachto:
| average number |     | of fouls (2018-19). | The fact | that the RPS |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
remainsbelow0.013innineoutoftenseasonsconfirmsthe • ATreeAugmentedNB(TAN)modelutilizingthesame
| stabilityofthedistance-basedweighting(Section3.4.1). |     |     |     |     |     | features, |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
• Aneuralnetwork-basedclassifier(NN),
4.2 PerformanceoftheDrawPredictionMethod • TheDixon-Colesmethod(D&C)[4].
We next report the results of the NB classifier trained to Figure 10 shows that our classifier obtains a higher
|             |         |      |                    |             | weighted |     | performance |     | than | these alternatives, |     | consistently |     |
| ----------- | ------- | ---- | ------------------ | ----------- | -------- | --- | ----------- | --- | ---- | ------------------- | --- | ------------ | --- |
| predict the | outcome | of a | match as “draw” or | “not draw.” |          |     |             |     |      |                     |     |              |     |
As described in Section 3.4.1, we applied our proposed detecting draws more accurately while also maintaining
strongoverallpredictiveaccuracyfortheimbalanceddataset.
clustering-baseddiscretizationforbothhistoricalandcurrent
teamclassifications.Furthermore,Section3.5.1detailshow The results highlight the relevance of our discretization-
|     |     |     |     |     | driven | NB  | approach | and | underscore |     | its superiority |     | in han- |
| --- | --- | --- | --- | --- | ------ | --- | -------- | --- | ---------- | --- | --------------- | --- | ------- |
theclassifierintegratesthesecomponentsalongwithoffen-
sive/defensive goal estimates and the presence of regional dlingordinalorskewedfootballdata.
Figure10showsthatthegaininWAPstemsprimarilyfrom
derbies.
Because of the highly imbalanced nature of the draw a reduction in false positives compared to TAN and D&C,
whiletheimprovementinWARovercontinuousNBmodels
| prediction | task, | we used | Weighted Accuracy | (WAP) and |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------- | ----------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WeightedRecall(WAR)toevaluateperformance,asdefined isduetothemodel’sabilitytocapturelow-probabilitydraws-
typicallyoccurringinderbiesormatchesbetweenteamswith
inEquations(7)and(8).Thesemetricsincorporatethehistor-
icaldrawrateateachevaluationpointtoestablishadynamic highlyunequalstrengths.ItisworthnotingthattheNNover-
fits24.9%ofdrawsandexhibitsthehighestoutputvariance,
thresholdforclassification.
whichresultsinahighWARbutpoorWAP.
|     |     |     |     |     |     | Both | experiments |     | agree | that class-oriented |     | discretisa- |     |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ----- | ------------------- | --- | ----------- | --- |
4.2.1 ComparativeAnalysisofDiscretizationMethods
|     |     |     |     |     | tion    | enhances | predictive  |        | utility | in low-frequency |     | scenarios |        |
| --- | --- | --- | --- | --- | ------- | -------- | ----------- | ------ | ------- | ---------------- | --- | --------- | ------ |
|     |     |     |     |     | (draws) |          | and ordinal | labels | (foul   | intervals).      |     | This dual | result |
Figure9comparesourdiscretizationstrategywiththreeref-
|     |     |     |     |     | supports |     | the methodological |     |     | hypothesis | proposed |     | in Sec- |
| --- | --- | --- | --- | --- | -------- | --- | ------------------ | --- | --- | ---------- | -------- | --- | ------- |
erencemodels:
tion2:improvinginter-classseparationyieldsgreaterbene-
fitsthanincreasingclassifiercomplexitywhenthevolumeof
• AnNBclassifierthatmodelscomponentsascontinuous historicaldataperteamislimited.
variables, Insummary,ourresultsdemonstratethatthediscretization
• AnNBclassifierthatemploysk-meansfordiscretization. processesspecificallytailoredforNBclassifierssignificantly
123

| 200 |     |     |     |     | ProgressinArtificialIntelligence(2026)15:189–202 |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
Fig.9 Goodnessofthemodelin
termsof(a)WAP,(b)WARfrom
applyingdifferentclustering
strategiesfortheNBclassifier
Fig.10 Goodnessofthemodel
intermsof(a)WAPand(b)
WARresultingfromapplying
differentpredictionmodels.
TAN=Tree-AugmentedNB;
NN=NeuralNetwork;D&C=
Dixon-Coles
enhancepredictiveperformanceinbothfoul-intervalclassifi- ityisextractedfordirectcomparisonwithourdiscretisation-
| cationanddraw-vs.-non-drawoutcomes.Consequently,this |                        |        |              | drivenNB. |     |     |     |     |
| ---------------------------------------------------- | ---------------------- | ------ | ------------ | --------- | --- | --- | --- | --- |
| approach                                             | represents a promising | avenue | for modeling | and       |     |     |     |     |
forecasting rare or ordinal events in the context of football (iii)TAN.Tree-AugmentedNBusingthesamediscretisation
analytics.
|     |     |     |     | assumptions | as our | NB model, | an equal-frequency | scheme |
| --- | --- | --- | --- | ----------- | ------ | --------- | ------------------ | ------ |
withfiveclusters(fourteamspercluster)isapplied,suchthat
Referencebaselines.(i)Shallowneuralnetwork.Tooffera eachteamisassignedtothecorrespondingintervalbasedon
non-Bayesian benchmark we trained a single-hidden-layer itsrankingoraveragenumberoffouls.
multi-layerperceptronwitharchitecture4:4:4(fourinputs,
| four ReLU     | units and a four-way | soft-max          | output).      | Model        |     |     |     |     |
| ------------- | -------------------- | ----------------- | ------------- | ------------ | --- | --- | --- | --- |
| parameters    | were initialised     | from U(0,1)       | and optimised | for          |     |     |     |     |
| 104 epochs    | with full-batch      | gradient descent, | categorical   | 5 Conclusion |     |     |     |     |
| cross-entropy | loss and a           | fixed learning    | rate η =      | 0.1 (see     |     |     |     |     |
GitHubrepositoryforthefullpython/NumPyscript). In this study, we presented a unified framework that lever-
|     |     |     |     | ages specialized | discretization |     | strategies | for NB classifiers |
| --- | --- | --- | --- | ---------------- | -------------- | --- | ---------- | ------------------ |
(ii) Dixon-Coles (D&C) model. The classical baseline is to predict two key events in football: the number of fouls
the bivariate Poisson formulation of [4], which adjusts the committed in a match and the probability of a draw. By
independent Poisson assumption via a low-score covari- emphasizing class-separating discretization rather than tra-
| ancetermρ | andappliesanexponentialtime-decayfactorξ |     |     |          |                |              |     |                   |
| --------- | ---------------------------------------- | --- | --- | -------- | -------------- | ------------ | --- | ----------------- |
|           |                                          |     |     | ditional | within-cluster | homogeneity, | our | approach captures |
to down-weight obsolete results. Following the original subtle distributional differences critical for accurate event
| paper,weestimatetheattack(α |     | )anddefence(β |              |              |     |     |     |     |
| --------------------------- | --- | ------------- | ------------ | ------------ | --- | --- | --- | --- |
|                             |     | i             | i )strengths | forecasting. |     |     |     |     |
for every team i, together with a global home-advantage For the fouls-prediction task, we demonstrated that dis-
γ,
parameter by maximum likelihood on the rolling two- cretizingteamsaccordingtohistoricalpercentilesandrepre-
seasonwindowthatprecedeseachtestmatch.Theresulting sentingtheirproximitytoclustercentroidsasrelativeweights
D&C log-likelihood provides the baseline probabilities for significantlyimprovesordinalclassification.Theuseofthe
{homewin,draw,awaywin},fromwhichthedrawprobabil- RPSprovedparticularlysuitableforreflectingthepenalties
123

ProgressinArtificialIntelligence(2026)15:189–202 201
associatedwithmisclassificationsatvaryingdistancesfrom (ii) Limited contextual variables. Our parsimony choice
thetruefoulsinterval. deliberately excluded referee identity, weather conditions,
Inthedraw-predictiontask,wetackledtheinherentclass traveldistance,andinjuryreportssoastoisolatethecontribu-
imbalance by employing Weighted Accuracy (WAP) and tionofranking-baseddiscretisation.Yetanecdotalevidence
Weighted Recall (WAR). Our results showed that maxi- suggeststhat,forinstance,refereeswithahistoricallystrict
mizing inter-class separation-through a second NB-based foulthresholdorwetpitchesthatslowballspeedmayinflate
selection ofoptimalclusters-boostspredictive performance thebaselinepropensityfordraws.Extending theNBgraph
when identifying this rare event. Moreover, incorporating intoahierarchicalstructure-whereclass-orientedbinsfeeda
subjectivefactors,suchastheintensityofregionalderbies, secondlevelcomprisingsuchsituationalcovariates-orcou-
providedadditionalgranularityindetectingdraws. plingitwithmixed-effectslogitlayerswouldallowthemodel
EmpiricalevaluationsovermultipleLaLigaseasonscon- toborrowstrengthacrosscontextswhileretainingtheinter-
firm the robustness of the proposed methodology. In both pretabilityofthediscretisedcore.
scenarios, discretizations specifically tailored for NB led
(iii) Sample size per cluster and external generalisability.
to higher predictive quality than standard clustering meth-
Addingdatafromothercompetitions-PremierLeague,Serie
ods and other common baselines (e.g., continuous NB,
A, Bundesliga-would roughly quintuple the sample size,
Mixtures of Truncated Basis Functions, neural networks).
enablingusto(a)performleague-specificversuspooledcal-
These findings underscore the practical utility of focusing
ibrationtests,(b)investigatewhethertheoptimalnumberof
ondiscretizationandclassseparationwhenmodelingrareor
clusters varies with playing style, and (c) quantify genuine
ordinalphenomenainsports.
between-leagueheterogeneitythroughhierarchicalBayesian
From a broader perspective, the proposed framework
shrinkage.
not only advances the state-of-the-art in football analyt-
ics but also highlights the capacity of NB classifiers to
Hybridandensembleextensions.Anaturallineofenquiry
handle nuanced data distributions when guided by context-
is to treat the calibrated NB probabilities as meta-features
awaredatasegmentation.Theadditionalcomparisonwiththe
thatfeedmoreflexiblelearners.Gradient-boostedtreescan
Fayyad-Irani discretizer confirms that, although it provides
exploit non-linear interactions among the NB outputs for
asolidbaseline,ourspecificapproachforNByieldsstatis-
fouls, goals and rankings; recurrent neural networks can
tically significant improvements in both tasks. Ultimately,
ingest the full match timeline, with NB scores serving as
ourresearchsupportsthepotentialofspecializeddiscretiza-
prior-likeanchorsateachtimestep;andthevenerableDixon-
tion within NB to provide more reliable, interpretable, and
Coles bivariate Poisson could be augmented with our draw
actionableinsightsintherealmofsportsanalytics. probabilityasaninformativeprioronthecovariancetermρ.
Limitations and future work. Although the empirical evi-
Acknowledgements ThisworkhasbeensupportedbygrantPID2022-
dence is encouraging, three methodological caveats invite
139293NB-C31fundedbyMICIU/AEI/10.13039/501100011033and
furtherinvestigationandextension. byERDFAwayofmakingEurope.
(i) Temporal trends and validation protocol. The present Funding Fundingforopenaccesspublishing:UniversidaddeAlmería/
study adopts a rolling two-season window whose hyper- CBUA.
parameter choice is motivated by the typical memory span
Open Access This article is licensed under a Creative Commons
of coaches and betting markets. Nevertheless, the assump-
Attribution4.0InternationalLicense,whichpermitsuse,sharing,adap-
tion that behavioural patterns remain reasonably stationary tation, distribution and reproduction in any medium or format, as
within that horizon could be violated by structural breaks- long as you give appropriate credit to the original author(s) and the
introduction of VAR, rule modifications on handballs, the source, provide a link to the Creative Commons licence, and indi-
cateifchangesweremade.Theimagesorotherthirdpartymaterial
recent surge in high-press systems, or even mid-season
inthisarticleareincludedinthearticle’sCreativeCommonslicence,
scheduling anomalies caused by the COVID-19 pandemic. unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterial
Tosafeguardagainstsuchnon-stationarities,futureresearch is not included in the article’s Creative Commons licence and your
will (a) incorporate exponential time-decay factors so that intended use is not permitted by statutory regulation or exceeds the
permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopy-
both cut-points and conditional probabilities are updated
rightholder.Toviewacopyofthislicence,visithttp://creativecomm
online, and (b) replace the single rolling window with ons.org/licenses/by/4.0/.
a blocked cross-validation grid (e.g., 6-month folds) or
a Monte-Carlo sliding-window resampling scheme. These
temporally-aware validation protocols will yield a distri-
References
bution of performance scores that is amenable to formal
hypothesis testing rather than the point estimates reported
1. Jin,B.,Xu,X.:Priceforecastingthroughneuralnetworksforcrude
here. oil,heatingoil,andnaturalgas.Energy,Measurement(2024)
123

202 ProgressinArtificialIntelligence(2026)15:189–202
2. Jin,B.,Xu,X.:Wholesalepriceforecastsofgreengramsusingthe 26. Fang,J.,Yeung,C.,Fujii,K.:Foulpredictionwithestimatedposes
neuralnetwork.AsianJournalofEconomicsandBanking(2024) from soccer broadcast video. arXiv preprint arXiv:2402.09650
3. Maher,M.J.:Modellingassociationfootballscores.Stat.Neerl.36, (2024)
109–118(1982) 27. Svensson, P.G.: Modelling and forecasting football attendances
4. Dixon, M., Coles, S.: Modelling association football scores and usingBayesiandynamicmodels.JournaloftheRoyalStatistical
inefficienciesinthefootballbettingmarket.J.Roy.Stat.Soc.:Ser. Society:SeriesD(TheStatistician)49,359–371(2000)
C(Appl.Stat.)46,265–280(1997) 28. Fernández, J., Salgado, L., Barro, S.: Football match prediction
5. Mackenzie,R.,Cushion,C.:Performanceanalysisinprofessional usingBayesianbeliefnetworks.In:10thInternationalConference
soccer:Playerandcoachperspectives.In:PerformanceAnalysis on Intelligent Systems and Knowledge Engineering (ISKE), pp.
ofSportIX,pp.49–57(2013) 1–6(2015)
6. Memmert,D.,Rein,R.:Matchanalysis,bigdataandtactics:current 29. Fayyad, U.M., Irani, K.B.: Multi-interval discretization of
trendsinelitesoccer.InternationalJournalofComputerSciencein continuous-valued attributes for classification learning. In: Pro-
Sport18(1),1–10(2019) ceedingsofthe13thInternationalJointConferenceonArtificial
7. Decroos,T.,Bransen,L.,VanHaaren,J.,Davis,J.:Actionsspeak Intelligence(IJCAI),pp.1022–1027(1993)
louder than goals: Valuing player actions in soccer. Journal of 30. Darwiche,A.:ModelingandReasoningwithBayesianNetworks.
SportsAnalytics5(1),1–13(2019) CambridgeUniversityPress,Cambridge,UK(2009)
8. Bradley,A.A.,Schwartz,S.S.,Hashino,T.:Distributions-oriented 31. Korb,K.B.,Nicholson,A.E.:BayesianArtificialIntelligence.CRC
verificationofprobabilityforecastsforsmalldatasamples.Mon. Press,BocaRaton(2010)
WeatherRev.142,746–754(2014) 32. Bielza,C.,Larrañaga,P.:DiscreteBayesiannetworkclassifiers:a
9. Garthwaite,P.,Kadane,J.,O’Hagan,A.:Statisticalmethodsfor survey.ACMComput.Surv.47,1–43(2014)
elicitingprobabilitydistributions.J.Am.Stat.Assoc.100,680– 33. Friedman,N.,Geiger,D.,Goldszmidt,M.:Bayesiannetworkclas-
700(2005) sifiers.Mach.Learn.29,131–163(1997)
10. Constantinou,A.C.:Bayesiannetworksforprediction,riskassess- 34. Maldonado,A.D.,Aguilera,P.A.,Salmerón,A.:Modelingzero-
ment and decision making in an inefficient association football inflatedexplanatoryvariablesinhybridBayesiannetworkclassi-
gamblingmarket.PhDthesis,HertfordshireUniversity,UK(2012) fiersforspeciesoccurrenceprediction.EnvironmentalModelling
11. Lee, W.C.: A Bayesian approach to the prediction of football &Software82,31–43(2016)
matches.J.Forecast.16,173–185(1997) 35. Farid,D.M.,Zhang,L.,Rahman,C.M.,Hossain,M.A.,Strachan,
12. Karlis,D.,Ntzoufras,I.:Bayesianmodellingoffootballoutcomes: R.:HybriddecisiontreeandnaïveBayesclassifiersformulti-class
Using the skellam’s distribution for the goal difference. IMA J. classificationtasks.ExpertSyst.Appl.41,1937–1946(2014)
Manag.Math.14,373–382(2003) 36. Scanagatta, M., Salmerón, A., Stella, F.: A survey on Bayesian
13. He,H.,Garcia,E.A.:Learningfromimbalanceddata.IEEETrans. networkstructurelearningfromdata.ProgressinArtificialIntelli-
Knowl.DataEng.21,1263–1284(2009) gence8,425–439(2019)
14. Chawla, N.V., Bowyer, K.W., Hall, L.O., Kegelmeyer, W.P.: 37. Langseth,H.,Nielsen,T.D.,Rumí,R.,Salmerón,A.:Mixturesof
SMOTE:Syntheticminorityover-samplingtechnique.Journalof truncatedbasisfunctions.Int.J.ApproximateReasoning53,212–
ArtificialIntelligenceResearch16,321–357(2002) 227(2012)
15. Goddard,J.:Regressionmodelsoffootballscores,599–614(2005) 38. Langseth,H.,Nielsen,T.D.,Salmerón,A.:Learningmixturesof
16. Forrest,D.,Goddard,J.,Simmons,R.:Oddssettersasforecasters: truncatedbasisfunctionsfromdata.SixthEuropeanWorkshopon
Thecaseofenglishfootball.Int.J.Forecast.21,551–564(2005) ProbabilisticGraphicalModels(2012)
17. Beal,R.,Norman,T.J.,Ramchurn,S.D.:Artificialintelligencefor 39. Pérez-Bernabé,I.,Maldonado,A.D.,Salmerón,A.,Nielsen,T.D.:
teamsports:Asurvey.DataMin.Knowl.Disc.33,838–866(2019) MoTBFs: An R package for learning hybrid Bayesian networks
18. Baio,G.,Blangiardo,M.,Aitkin,M.:Bayesianhierarchicalmodel using mixtures of truncated basis functions. The R Journal 12,
for the prediction of football results. J. Appl. Stat. 37, 253–264 342–358(2020)
(2010) 40. Jolliffe, I.T., Stephenson, D.B.: Forecast Verification. A Practi-
19. Forrest, D., Simmons, R.: Outcome uncertainty and attendance tioner’sGuideinAtmosphericScience,p.240.JohnWiley&Sons
demandinsport:ThecaseofEnglishsoccer.ScottishJournalof Ltd.,Chichester(2003)
PoliticalEconomy49,237–249(2002) 41. Fernández-Delgado,M.,Cernadas,E.,Barro,S.,Amorim,D.:Do
20. Cain,M.,Law,D.,Peel,D.:Thefavourite-longshotbiasandmar- weneedhundredsofclassifierstosolverealworldclassification
ketefficiencyinUKfootballbetting.ScottishJournalofPolitical problems?J.Mach.Learn.Res.15,3133–3181(2014)
Economy47,25–36(2000)
21. Lenor,S.,Lenten,L.J.A.,McKenzie,J.:Rivalryeffectsandunbal-
ancedscheduleoptimisationintheAustralianfootballleague.Rev.
Publisher’sNote SpringerNatureremainsneutralwithregardtojuris-
Ind.Organ.49,43–69(2016)
dictionalclaimsinpublishedmapsandinstitutionalaffiliations.
22. Hastie,T.,Tibshirani,R.,Friedman,J.:TheElementsofStatistical
Learning:DataMining,Inference,andPrediction.Springer,New
York(2009)
23. Liu,X.Q.,Wang,X.C.,Tao,L.,An,F.,Jiang,G.:Alleviatingcon-
ditional independence assumption of naive bayes. Stat. Pap. 65,
2835–2863(2024)
24. Flores,M.J.,Gámez,J.A.,Martínez,A.M.,Puerta,J.M.:Handling
numericattributeswhencomparingBayesiannetworkclassifiers:
doesthediscretizationmethodmatter?Appl.Intell.34,372–385
(2011)
25. Rish,I.:AnempiricalstudyofthenaiveBayesclassifier.In:IJCAI
2001WorkshoponEmpiricalMethodsinArtificialIntelligence,
vol.3,pp.41–46(2001)
123