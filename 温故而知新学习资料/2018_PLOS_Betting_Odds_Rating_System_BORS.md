> **学术知识网络导航**：[系统大脑 AGENTS.md](../AGENTS.md) · [文献总索引与导读](README_学习资料索引与经典论文导读.md) · [实战总复盘总结](../分析复盘记录/总复盘总结.md) · [战绩胜率看板](../分析复盘记录/总准确率.md) · [最新赛前推演](../分析复盘记录/2026-09-12_预测.md)

---

RESEARCHARTICLE
The Betting Odds Rating System: Using soccer
forecasts to forecast soccer
FabianWunderlich*,DanielMemmert
InstituteofTrainingandComputerScienceinSport,GermanSportUniversityCologne,Cologne,Germany
*f.wunderlich@dshs-koeln.de
Abstract
a1111111111
a1111111111
Bettingoddsarefrequentlyfoundtooutperformmathematicalmodelsinsportsrelatedfore-
a1111111111
a1111111111 castingtasks,howeverthefactorscontributingtobettingoddsarenotfullytraceableandin
a1111111111 contrasttorating-basedforecastsnostraightforwardmeasureofteam-specificqualityis
deduciblefromthebettingodds.Thepresentstudyinvestigatestheapproachofcombining
themethodsofmathematicalmodelsandtheinformationincludedinbettingodds.Asoccer
forecastingmodelbasedonthewell-knownELOratingsystemandtakingadvantageofbet-
tingoddsasasourceofinformationispresented.Datafromalmost15.000soccermatches
OPENACCESS
(seasons2007/2008until2016/2017)areused,includingbothdomesticmatches(English
Citation:WunderlichF,MemmertD(2018)The
PremierLeague,GermanBundesliga,SpanishPrimeraDivisionandItalianSerieA)and
BettingOddsRatingSystem:Usingsoccer
forecaststoforecastsoccer.PLoSONE13(6): internationalmatches(UEFAChampionsLeague,UEFAEuropeLeague).Thenovelbetting
e0198668.https://doi.org/10.1371/journal. oddsbasedELOmodelisshowntooutperformclassicELOmodels,thusdemonstrating
pone.0198668
thatbettingoddspriortoamatchcontainmorerelevantinformationthantheresultofthe
Editor:AnthonyC.Constantinou,QueenMary matchitself.Itisshownhowthenovelmodelcanhelptogainvaluableinsightsintothequal-
UniversityofLondon,UNITEDKINGDOM
ityofsoccerteamsanditsdevelopmentovertime,thushavingapracticalbenefitinperfor-
Received:February26,2018 manceanalysis.Moreover,itisarguedthatnetworkbasedapproachesmighthelpinfurther
Accepted:May23,2018 improvingratingandforecastingmethods.
Published:June5,2018
Copyright:©2018Wunderlich,Memmert.Thisis
anopenaccessarticledistributedundertheterms
oftheCreativeCommonsAttributionLicense,
whichpermitsunrestricteduse,distribution,and Introduction
reproductioninanymedium,providedtheoriginal
Forecastingsportseventslikematchesortournamentshasattractedtheinterestofthescien-
authorandsourcearecredited.
tificcommunityforquitealongtime.Sportseventslikesoccermatchestakeplaceregularly
DataAvailabilityStatement:Alldatausedwithin
andgeneratehugepublicattention.Moreover,extensivedataareavailableandrelativelyeasy
thisstudyhasbeenobtainedfrompublicly
tointerpret.Duetothesefactors,sports(andespeciallysoccer)turnouttobeaperfectenvi-
availablewebsitesthatarementionedinthe
ronmenttostudytheapplicabilityofexistingforecastingmethodsordevelopnewmethodsto
respectivepartofthestudy.Moreover,afile
containingtheminimaldatatoreplicatethestudy betransferredtootherfieldsofforecasting.
aswellasthemostimportantresultsareincluded Searchingforthemostaccuratesportsforecastingmethodsisbothinterestingfromascien-
assupportinginformation. tificviewandfromaneconomicviewasthehugebettingmarketforsoccer(andothersports)
Funding:Theauthor(s)receivednospecific isprovidingtheopportunitytowinmoneybyforecastingaccurately[1].Besidesproviding
fundingforthiswork. accurateforecaststheforecastingmodelscanalsobevaluableinunderstandingthenatureof
theunderlyingprocesses[2]and,asdemonstratedwithinthisstudy,togainpracticalinsights
Competinginterests:Theauthorshavedeclared
thatnocompetinginterestsexist. toperformanceanalysisinsports.
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 1/18

TheBettingOddsRatingSystem
Threedifferenttaskscontributetothecomplexityofapproachingsportsforecastswiththe
useofmathematicalmodels.First,theunknownqualityofateam(orplayer)needstobeinves-
tigatedutilizingawideandmeaningfuldatasetaswellasawell-fittedmathematicalmodel
[3,4].Second,theforecastitself(i.e.probabilityofacertainmatchortournamentoutcome)
needstobederivedusingappropriatestatisticalmethodssuchasprobabilitymodels[5]or
MonteCarlosimulation[2,6].Finally,theresultsoftheforecastsneedtobetestedagainstreal
datausingappropriatestatisticaltests.Wewillrefertothesethreechallengesasratingprocess,
forecastingprocessandtestingprocessthroughoutthepaper.
Varioussourcesofforecastshavebeeninvestigatedinanattempttounderstandforecasting
processes,developpromisingforecastingmethodsandcomparetheirforecastingabilities.The
sourcescanbebroadlyclassifiedinfourcategories:
1. Humanjudgement,i.e.askingparticipantswithavaryingdegreeofknowledgetoperform
sports-relatedforecastingtasks
2. Rankings,i.e.usingofficialrankingssuchastheFIFAWorldRankinginsoccerortheATP
rankingintennistoderiveforecastsforfuturematchesandtournaments.
3. Mathematicalmodels,i.e.usingexistingordevelopingnovelmathematicalandstatistical
approachestoforecasttheoutcomesofsportsevents.
4. Bettingodds,i.e.usingtheoddsofferedbybookmakersandbettingexchangesasaforecast
oftheunderlyingsportsevent.
Humanjudgement
Numerousworkshaveinvestigatedthepredictivequalityofhumanforecastsinsoccer.Ingen-
eral,so-calledsoccerexpertsarenotabletooutperformlaypeopleonsimplesoccerrelated
forecastingtasks[7].Moreover,mostparticipantswereoutperformedbyforecastsfollowinga
simplerulebasedontheFIFAWorldRankingintheaforementionedstudy.Expertforecasts
fromtipsterspublishedinsportsjournalswereevenshowntobeoutperformedbythenaïve
modelofalwaysselectingthehometeamtowin[8].However,itwasshownthatexpertsout-
performlaypeopleinmorecomplexforecastingtaskssuchasforecastingexactscoresormatch
statistics[9].
Rankings
Thepredictivecharacterofrankingsisquestionableforseveralreasons.Rankingsareusually
designedtorewardforsuccessandnottomakethebestestimateonafutureperformanceofa
teamorplayer.Moreover,sportsrankingsaresimplisticandlackrelevantinformationforthe
purposeofbeingfairandeasytounderstand(cf.[10]).However,rankingsarefoundtobeuse-
fulpredictorsingeneralforsoccer[11],tennis[10]andbasketball[12].Atthesametimeitis
shownthatbettingodds[11]ormathematicalmodels[10]arecapableofoutperformingthese
rankingsinpredictivetasks.
Mathematicalmodels
Afrequentlyinvestigatedandwidelyacceptedmathematicalapproachinsportsforecastingis
theELOratingsystem,whichisawell-knownmethodforrankingandratingsportsteamsor
players.Itwasoriginallyinventedforandusedinchess,butthroughoutthetimeithasbeen
successfullyappliedtoavarietyofothersportsincludingsoccer(see[13,3]),tennis[14]or
Australianrulesfootball[15].
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 2/18

TheBettingOddsRatingSystem
HvattumandArntzen[16]extendedthewell-knownELOratingsystemusinglogitregres-
sionmodelstocalculateprobabilitiesforthethreematchoutcomes(Home/Draw/Away)from
theELOratings.ItwasshownthatthisELOapproachwassuperiortomodelsbasedonan
orderedprobitregressionapproachintroducedbyGoddard[17]butinferiortobettingodds.
Bettingodds
Bettingoddscanbeseenasanaggregatedexpertopinionreflectingboththejudgementof
bookmakersandthebettingbehaviorofbettors.However,itisacompletelydifferentformof
expertopinioncomparedtostudieswhereexpertsareaskedtoperformforecastingtasksinan
experimentalenvironment.Whereasthoseexpertsusuallydonothavetofearnegativeconse-
quencesfrominaccurateforecasts,offeringinaccurateoddswillhaveseriousfinancialconse-
quencesforbookmakers.Thiscouldbeareasonwhybettingoddswereshowntobeclearly
outperformingsoccertipsterspublishingtheirforecastsinsportsjournals[8].
HvattumandArntzen[16]showthatingeneralbettingoddspossessanexcellentpredictive
qualityandperformbetterinforecastingsoccerresultsthanvariousquantitativemodels.A
consensusmodelbasedonbettingoddsofvariousbookmakerswasshowntoprovidemore
accurateforecastsontheEuropeanchampionship2008insoccerthanmethodsusingtheELO
ratingandtheFIFAWorldRanking[11].Kovalchik[14]eveninvestigateselevenforecasting
modelsintennisandfindsthatnoneofitisabletooutperformbettingoddsinforecastingsin-
glesmatches.
Withoutdenyingthegeneralpredictivepowerofbettingodds,itisworthnotingthatthere
areempiricalindicationsontheimperfectnessofbettingoddsasshownin[18]orintheexten-
sivelydocumentedfavorite-longshotbias(see[19]foranoverview).Moreover,itisworthnot-
ingthatvariousmodelbasedapproacheswereyieldingpositivebettingreturnswhendeducing
bettingstrategiesfromtheforecasts([20–22]amongothers).
Amajorpartoftheaforementionedstudiesfocusesoncomparingthefourdifferentsources
offorecastsordifferentapproachesforthesamesourceofforecast.Asawideconsensusexists
thatbettingoddshaveproventobeapowerfulinstrumentinforecasting[23],bettingoddsare
routinelyusedasaqualitybenchmarkfortestingthepredictivequalityofmathematical
approaches[14].Bydoingthis,bettingoddsandmathematicalmodelsareoutlinedascontrary
approachesforthesameforecastingtask,insteadofmixingthepowerofbothapproachesto
createnewforecastingpossibilities.
Sofar,hardlyanystudyhastriedtoreverttheforecastingprocessusingexistingforecasts
(frombettingodds)todrawconclusionsaboutthequalitiesoftheteams,obtainteamratings
andthuscontributetotheperformanceanalysisofteams.Leitneretal.[11]pursuethisstrat-
egybyusingan“inverse”simulationoftheEuropeanChampionshipin2008toobtainteam
ratingsfromthebettingoddsforthetournament.Thisapproachespeciallyshedslightonthe
differencesbetweenateam’squalityanditsprobabilityofwinningatournament(theeffectsof
tournamentdraws).However,nobettingoddsfromsinglematchesareconsideredforestab-
lishingteamratings.Althoughthepredictivequalityofbettingoddsisfrequentlystatedand
theextensiveinformationreflectedintheoddscanundisputedlybeseenasanimportant
advantageofbettingodds,thequestionofhowvaluablebettingoddsofpriormatchesarefor
forecastingfuturematcheshasnotbeentackledsofar.
Thisstudyextendspriorresearchinvariousaspects.Wepresentanovelmodelthatisable
tocombinetheadvantagesofmathematicalapproacheswiththeinformationadvantageofbet-
tingodds.Bydesign,themodelisnotexpectedtoimproveforecastsfrombettingodds,butit
aimsatdevelopingaframeworkthatenablesustoinvestigatethetransferabilityofpriorfore-
caststofutureforecasts,constructaratingthatimprovesclassicalratingmethodsandthususe
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 3/18

TheBettingOddsRatingSystem
forecastingmethodstogainimprovedpracticalinsightsintoperformanceanalysis.Indetail,
weexaminethequestionwhetherbettingoddsknownpriortoamatchareofhighervaluefor
forecastingpurposesthantheresultknownafterthematch.Theratingusedasanintermediate
stepoftheforecastingmodelcanbeinterpretedasareversaloftheforecastingprocessasthe
qualityofasoccerteamisdeducedfrompriorforecasts.Weusethisratingtodemonstrate
improvementstotraditionalratingmethodsandhowtheinformationincludedinbetting
oddscaneffectivelybeextractedtobeusedinpracticalanalysis,e.g.onthequalitydevelop-
mentofsoccerteams.Moreover,wedemonstratehowtheELO-Oddsmodelcanbeusedfor
analyzingthequalitydevelopmentofindividualteamsovertimeortheexplanatorypowerof
leaguetables.Finally,wedemonstratealackoftheoreticalfoundationsconcerningratingmod-
elsthattakeadvantagefromthenetworkstructureofmatchesbyapplyingmatchresultstothe
ratingsofuninvolvedteams.
Method
Data
Weobtainedmatchdatafor10seasonsinfourofthemostimportantEuropeansoccerleagues
(namelytheEnglishPremierLeague,theGermanBundesliga,theSpanishPrimeraDivision
andtheItalianSerieA)fromhttp://www.football-data.co.uk.Foreachleagueallseasonsfrom
2007/2008until2016/2017wereconsideredaddingupinatotaldatasetofnearly14,500
domesticsoccermatches.Moreover,weobtaineddatafor10seasonsinthemostimportant
internationalclubcompetitions(UEFAChampionsLeagueandUEFAEuropeLeague)from
http://www.oddsportal.com.Forallseasonsfrom2007/2008until2016/2017thosematches
playedbetweenparticipantsfromthefouraforementionedsoccerleagueswereconsidered.
Overall,morethan450internationalmatcheswereconsideredaddingupinatotaldatabaseof
nearly15,000matches.
Themodelsexaminedthroughoutthispaperarebasedonthefollowingdataforeach
match:matchdate,hometeam,awayteam,homegoals(fulltime),awaygoals(fulltime)as
wellasbettingoddsforhomewin,drawandawaywin.Toavoidbookmaker-specificityand
obtainabestpossiblereflectionofthebettingmarket,allbettingoddsusedintheanalysisare
averagedbasedonavailablebettingoddsofvariousdifferentbookmakers.Exceptforisolated
cases,theaveragebettingoddsarebasedonfiveormorebookmakersininternationalmatches
and20ormorebookmakersindomesticmatches.Thedifferencebetweeninternationaland
domesticmatchesisduetotheextentofinformationandlevelofdetailavailableattherespec-
tivedatasource.ThematchesCagliarivs.Roma(23.09.12)andSassuolovs.Pescara(28.08.16)
werecompletelydiscardedfromthedatasetasbothweredecidedbyfederationdecision.The
finalmatchesfromChampionsLeagueandEuropeLeaguewerecompletelyexcludedfromthe
datasetastheseareplayedataneutrallocation.SeeTable1fordetailedinformationonthe
numberofmatchesforeachseasonandcompetition.
Transferringbettingoddstoprobabilities
Bettingoddsarewidelyusedtoderiveforecastsastheyaresimplytransferrabletoprobabilities
andhaveproventheirqualityinalargenumberofdifferentstudies.Ifnobookmakermargin
wascontainedinthebettingodds,theinversebettingoddsforanypossibleoutcomeofa
matchcouldbeinterpretedasitsprobabilityofoccurring.Toeliminatethebookmakermargin
fromtheodds,i.e.ensurethatthederivedprobabilitiessumupto100%,weappliedthemost
widelyusedapproachofbasicnormalization(see[11,24]foramoredetailedexplanationand
S1Filefordetailsonthecalculation).Thisapproacheliminatestheoverallbookmakermargin,
howeveritcanbecriticizedassimplifying,asitimplicitlyassumesthatbookmakermarginis
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 4/18

TheBettingOddsRatingSystem
Table1. Informationonthedatasetusedwithinthisstudy.
Competition Seasons Numberofmatches Averageoverround Averagetheoreticalbookmakerpayout
EnglishPremierLeague 07/08–16/17 3,800 1.065 0.939
GermanBundesliga 07/08–16/17 3,060 1.060 0.944
SpanishPrimeraDivision 07/08–16/17 3,800 1.065 0.939
ItalianSerieA 07/08–16/17 3,798 1.067 0.937
UEFAChampionsLeague 07/08–16/17 316 1.047 0.956
UEFAEuropeLeague 07/08–16/17 157 1.054 0.949
Total 07/08–16/17 14,931 1.064 0.940
https://doi.org/10.1371/journal.pone.0198668.t001
distributedproportionatelyacrossallpossibleoutcomesofamatch(e.g.home,winanddraw).
Foramoredetaileddiscussiononthisissue,possibleconsequencesandalternativeapproaches
see[25,24].Duetothereasonablysmallmarginsinourdataset(averagebookmakerover-
roundof1.064correspondingtoatheoreticalpayoutof94.0%)weconsidertheapproachof
basicnormalizationanacceptablesimplification.SeeTable1andS1Fileformoredetailson
themargins.
Ratingsystems
TheELOratingsystemisawell-knownandwidelyusedratingsystemthatwasoriginally
inventedtobeusedinchess,buthassuccessfullybeentransferredtoratesoccerteams(cf.[3]).
Themodelisbasedontheideaofcalculatinganexpectedresultforeachmatchfromthecur-
rentratingoftheparticipatingteams.Afterthematchtheactualresultisknownandtherat-
ingsofbothparticipantsareadjustedaccordingly.Ahigherdifferencebetweenactualresult
andexpectedresultevokesahigheradjustmentmadetotheratings(andviceversa).Asa
result,foreachteamadynamicratingisobtainedandisadjustedovertimebyeverynew
matchresultthatbecomesobservable.
ELO-Result
LetH andA betheELO-ratingsforthehomeandtheawayteampriortoamatch.Thenthe
i i
expectedresultforthematchis
1
eH ¼
1þcðAi(cid:0) Hi(cid:0) oÞ=d
eA ¼1(cid:0) eH
whereωisameasureforthehomeadvantage(inELO-points)whilecanddarefreelyselect-
ableparametersthatinfluencethescaleoftherating.Withinthisstudy,weapplytheusual
choiceofc=10andd=400.
AfterthematchtheactualresultaHforthehometeamcanbeobserved.ItissetasaH=1if
thehometeamwins,aH=0.5incaseofadrawandaH=0ifthehometeamloses.Theactual
resultfortheawayteamconsequentlyisaA=1−aHandtheratingsforbothteamsareadjusted
asfollows:
H ¼H þkðaH(cid:0) eHÞ
iþ1 i
A ¼A þkðaA(cid:0) eAÞ
iþ1 i
wherekisanadjustmentfactorthatwewillchoosebycalibrating.WerefertothisclassicELO
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 5/18

TheBettingOddsRatingSystem
modelasELO-Result.See[26]and[13,3]formoreinformationonthecalculationofaclassic
ELOratinginchessandsoccer.
ELO-Goals
ThismodificationoftheELOmodeladditionallytakesthegoalsscoredbyeachteaminto
account.Letδbetheabsolutegoaldifferenceforamatch.Thentheparameterkismodifiedto
be
k¼k ð1þdÞl
0
Therefore,themodelisabletousemoreinformationthanthepureresultofamatch.The
calculationhasbeenadoptedfrom[16]andthemodelisreferredtoasELO-Goals.Notethat
thewell-knownWorldFootballEloRatingspublishedonline[13,3]isalsobasedonacalcula-
tionincludingthegoals,howeverusingaslightlydifferentcalculationmethod.
ELO-Odds
Althoughbettingoddshaveproventopossessexcellentpredictivequalities,theyhavenotbeen
usedasabasistocreaterankingsandratings.Surprisinglyithasnotbeenevaluatedyet,how
valuablebettingoddsfrompreviousmatchesareforforecastingfuturesoccermatches.The
followingmodelisreferredtoasELO-OddsandcombinesthemethodsofELO-ratingwith
theinformationobtainedfrombettingodds.
ThecalculationworkssimilarasshownforELO-Result,i.e.theexpectedresultforeach
matchiscalculatedfromthecurrentratingofitsparticipants.Theactualresult,however,is
replacedbytheexpectedresultintermsofbettingodds.Letp ,p andp betheprobabilities
H D A
forhomewin,drawandawaywinobtainedfromthebettingodds.Thentheactualresultas
usedinELO-Resultisreplacedby:
aH ¼p þ0:5p
H D
aA ¼p þ0:5p ¼1(cid:0) aH
A D
Themodelaimsataccessingmoreinformationthanresultsorgoalsbyindirectlyderiving
itfromthebettingodds.Atthesametime,itisadrasticrestrictionasthroughoutthecalcula-
tionoftheELO-Oddsratingsnomatchresultiseverdirectlyused.Moreover,themodeluses
thebettingoddspriortothematchasameasurefortheactualresult,thusonlyusinginforma-
tionthatwasknownpriortothestartofthematchandfullyignoringtheresultthatisobserv-
ableafterthematch.
Statisticalframework
Tomakesurethisstudyisbasedonasolidframework,wemakeuseofpreviousresearchand
provenstatisticalmethods,thatarelargelyadoptedfromHvattumandArntzen[16].Foreach
oftheELOmodelstheapproachisasfollows:Forthefulltimeperiodofdata(10seasons,07/
08–16/17)theELOratingofeachteamiscalculatedandadjustedaftereachmatch.Ahome
advantageofω=80isusedasfoundintheaforementionedpaper.Asastartvalueeachteamis
givenaratingof1,000pointspriortothefirstmatchofthefirstseason.Tohaveausefulstart
valueforpromotedteamsinlaterseasons,theseteamscarryontheratingsoftherelegated
teams.Thisprocedurehastwopositiveeffects:First,itcanbeassumedthatpromotedteams
areingeneralweakerthantheaverageteamintheleague.Thustheratingsoftherelegated
teamsareamorepromisingestimatorofteamqualitythanusinganaveragestartvalueforthe
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 6/18

TheBettingOddsRatingSystem
Fig1.Theforecastingmethodsandstatisticalframeworkasusedwithinthisstudyandlargelyobtainedfrom
HvattumandArntzen.
https://doi.org/10.1371/journal.pone.0198668.g001
promotedteams.Second,ithastheniceside-effectthatthesumofratingsstaysthesameover
thefullperiodoftime,calculatedoverallteamsthatarecurrentlyparticipatinginoneofthe
fourleagues.
Thefirsttwoseasons(07/08&08/09)solelyserveasatimeperiodtoderiveausefulinitial
ratingforeachteam.Foreachmatchofthefollowingthreeseasons(09/10–11/12)thediffer-
encebetweenthehometeam’sratingandtheawayteam’sratingisobtained.Theseratingdif-
ferencesthenaretakenasthesinglecovariateofanorderedlogitregressionmodel.Asaresult
fromtheregressionmodel,logisticfunctionsareobtainedthattransferaratingdifferenceinto
probabilitiesforhomewin,drawandawaywin.Foreachmatchofthelastfiveseasons(12/13–
16/17)theseprobabilitiesarecalculatedandformtheforecastsofthematches.Finally,the
forecastsareanalyzedusingtheinformationallossL (see[27]foradefinition)asameasureof
i
predictivequality.Pleasenotethatminimizingtheinformationallossisequivalenttomaximiz-
ingthelikelihoodfunction.Toverifywhetherdifferencesregardingthelossfunctionsoftwo
modelsaresignificant,pairedt-testsareused.SeeFig1foragraphicalrepresentationofrating
process,forecastingprocessandtestingprocess.
Results
Parametercalibration
ThethreemodelsELO-Result,ELO-GoalsandELO-Oddsrequirecalibrationofparameters.
WhereasELO-ResultandELO-Oddsrequireonesingleparameterk,ELO-Goalsrequirestwo
parametersk andλ.Table2showstheinformationallosswhenchoosingdifferentparameters
0
forELO-Result,ELO-GoalsandELO-Odds.Theinformationallossforallthreemodelsand
differentparametersismoreoverillustratedinFig2,Fig3andFig4.Fromtheresultswecan
chooseusefulparametersforthemodels(namelyk=14forELO-Result;k =4,λ=1.6for
0
ELO-Goalsandk=175forELO-Odds).
Atfirstglance,itissurprisingthattheadjustmentfactorkismorethantentimeshigherfor
ELO-OddsthanforELO-Result,butthisresultcanbeexplainedasfollows:First,theactual
results(aH,aA)inELO-Resultbeingeither0,0.5or1naturallydeviatemorefromtheexpected
resultthaninELO-Odds,consequentlyrequiringasmalleradjustmentfactor.Second,the
actualresultsinELO-Resultaresubjecttostronginfluenceofrandomness.Ahigheradjust-
mentfactordoesthereforeevokeatoostrongadaptionofthelatestresults.
Ingeneral,usingtheresultstochoosetheparameters(i.e.selectingthoseparametersyield-
ingthebestresults)evokesadangerofoverfittingthedata.However,wecanseethatthe
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 7/18

TheBettingOddsRatingSystem
Table2. Comparisonofinformationallossfordifferentmodelsandvariousparameters.
| Forecastingmodel | Parameters | AverageL |
| ---------------- | ---------- | -------- |
i
| BettingOdds | -          | 1.3795 |
| ----------- | ---------- | ------ |
| ELO-Odds    | k=175      | 1.3913 |
| ELO-Odds    | k=200      | 1.3913 |
| ELO-Odds    | k=150      | 1.3914 |
| ELO-Odds    | k=250      | 1.3915 |
| ELO-Odds    | k=100      | 1.3919 |
| ELO-Odds    | k=300      | 1.3920 |
| ELO-Odds    | k=400      | 1.3937 |
| ELO-Odds    | k=50       | 1.3937 |
| ELO-Goals   | k =4,λ=1.6 | 1.4008 |
0
| ELO-Goals | k =4,λ=1.4 | 1.4009 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =6,λ=1.2 | 1.4009 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =6,λ=1.0 | 1.4011 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =2,λ=2.0 | 1.4012 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =6,λ=1.4 | 1.4013 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =8,λ=1.0 | 1.4013 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =8,λ=0.8 | 1.4013 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =4,λ=1.8 | 1.4014 |
| --------- | ---------- | ------ |
0
| ELO-Goals | k =4,λ=1.2 | 1.4016 |
| --------- | ---------- | ------ |
0
| ELO-Result | k=14 | 1.4032 |
| ---------- | ---- | ------ |
| ELO-Result | k=12 | 1.4033 |
| ELO-Result | k=16 | 1.4034 |
| ELO-Result | k=18 | 1.4038 |
| ELO-Result | k=10 | 1.4038 |
| ELO-Result | k=20 | 1.4043 |
| ELO-Result | k=25 | 1.4060 |
| ELO-Result | k=5  | 1.4105 |
https://doi.org/10.1371/journal.pone.0198668.t002
resultsarenothighlysensitivetothechoiceoftheparameter(s),comparedtothesensitivityof
theresultstothechoiceofthemodel(seenextsection).
Predictivequality
Table3showsthemajorresultsofanalyzingthepredictivequalityofthedifferentforecasting
methods.Bettingoddsareshowntohavethehighestpredictivequality,outperforming
ELO-Oddsonahighlysignificantlevel.ELO-OddsinturnisoutperformingELO-Goalsona
highlysignificantlevelwhileELO-GoalsisoutperformingELO-Resultsignificantly.Therefore,
theresultsofHvattumandArntzen[16]couldbereproducedwithrespecttobettingodds,
ELO-ResultandELO-Goals,althoughusingadifferentsetofdataincludingfourEuropean
leaguesandtwointernationalcompetitions.
ELO-GoalsbeingsuperiortoELO-Resultconfirmsthatthegoaldifferenceofamatchcon-
tainsmorerelevantinformationthanitsresult(win,draw,lose).Thisisinlinewithsimilar
resultsfrom[28]whoshowedthattheaveragegoaldifferenceisabettermeasureforateam’s
qualitythantheaveragepoints(bothcalculatedoveranumberofmatches).
ThestrikingandnovelresultisthesuperiorityofELO-OddstoELO-Goalswhichconfirms
thatforecastsfrompreviousmatchesareindeedusefulinratingteamsandavaluablesourceof
informationforforecastingfuturematches.Pleasenotethatthisresultisnotnotably
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 8/18

TheBettingOddsRatingSystem
Fig2.AverageinformationallossforvariouschoicesoftheparameterkinmodelELO-Result.
https://doi.org/10.1371/journal.pone.0198668.g002
dependingonthechoiceoftheparameterkasELO-OddsisstilloutperformingELO-Goalson
ahighlysignificantlevel(p<0.01)ifchoosingextremeparameterslikek=30ork=400.Even
forparameterslikek=20ork=500ELO-OddsisstillsuperiortoELO-Goals,butthediffer-
enceisnotsignificantanymore(seeTable4).
Infact,thisshowsthatfromapredictiveperspectivethebettingoddsknownpriortoasoc-
cermatchpossessmoreinformationthantheresultknownafterthematch.Toputitsimple,
lookingatthebettingoddspriortoamatchgivesyoumorerelevantinformationonteam
qualityandmorevaluableinsightstoperformanceanalysisthanstudyingtheresultsafter-
wards.Thisresultmightpartlybedrivenbythefactthattheresultofamatchisarealizationof
theunderlyingprobabilitydistribution,whilethebettingoddsrepresentthisprobability
Fig3.AverageinformationallossforvariouschoicesoftheparameterskandlambdainmodelELO-Goals.
https://doi.org/10.1371/journal.pone.0198668.g003
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 9/18

TheBettingOddsRatingSystem
Fig4.AverageinformationallossforvariouschoicesoftheparameterkinmodelELO-Odds.
https://doi.org/10.1371/journal.pone.0198668.g004
distribution.Includingothermatch-relatedqualitymeasures(besidesresultsandgoals)such
asexpectedgoalscalculatedfrommatchstatisticsafteramatchcouldserveasbasisforauseful
additionalELOrating.Unfortunately,thiswouldeitherrequireapubliclyavailablesourceof
expectedgoalscoveringthewholedatabaseoradatabaseincludingcomprehensivematchsta-
tisticsinordertocalculateownmeasuresofexpectedgoals.
Bydesign,wecannotexpecttheELO-Oddsmodeltoprovidebetterforecaststhanthebet-
tingoddsitself,asthesearetheonlysourceofinformationforthemodel.Nevertheless,itis
worthevaluatingwhythereissuchacleargapinpredictivequalities.Notethat,althoughusing
bettingoddsasasourceofinformation,theELO-Oddsmodelbyfarisexploitinglessinforma-
tionthanthebettingodds.Itcanonlyextractteamspecificinformationfromthebettingodds
andaggregatethemintheratings.Motivationalaspectsofasinglematchoranyrelevantinfor-
mation(likeinjuriesorline-ups)thathasbecomeavailableinbetweentwomatcheswillnotbe
reflectedinELO-Odds.Moreover,theactualresultoftheprecedingmatchisnotreflectedin
ELO-Odds,whileitissurelyinfluencingthebettingodds.Finally,theorderedlogitregression
modelusingtheELOdifferenceassinglecovariatemightbealimitingfactor,thusevenan
accurateratingdoesnotnecessarilyleadtoanaccurateforecast.
Analyzingindividualteamratings
Oneimportantaspectofthisstudyistoshedlightonaccurate(predictive)teamratingsthat
areusuallyusedasanintermediateresultofforecastingmodels.Bettingoddsforamatchcan
Table3. Statisticaltestscomparingthepredictivequalitiesofdifferentforecastingmethods. Thep-valuecom-
pareseachmodeltothemodelinthenextrow.
ForecastingModel AverageL StandarddeviationL p-value(pairedt-test)
i i
BettingOdds 1.380 0.674 <0.0001
ELO-Odds(k=175) 1.391 0.706 <0.0001
ELO-Goals(k =4,λ=1.6) 1.401 0.714 0.0202
0
ELO-Result(k=14) 1.403 0.715 -
https://doi.org/10.1371/journal.pone.0198668.t003
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 10/18

TheBettingOddsRatingSystem
Table4. StatisticaltestscomparingthepredictivequalitiesofELO-Odds(variousextremeparameters)toELO-Goals. Thep-valuecompareseachmodelto
ELO-Goals.
ForecastingModel AverageL StandarddeviationL p-value(pairedt-test)
i i
ELO-Odds(k=175) 1.391 0.706 <0.0001
ELO-Odds(k=400) 1.394 0.709 0.0044
ELO-Odds(k=30) 1.396 0.707 0.0026
ELO-Odds(k=500) 1.397 0.707 0.2118
ELO-Odds(k=20) 1.398 0.714 0.0857
ELO-Goals(k =4,λ=1.6) 1.401 0.714 -
0
https://doi.org/10.1371/journal.pone.0198668.t004
beseenasthemarketjudgementforthequalityofbothteamsparticipating.However,itisnot
straightforwardtoobtainaquantitativeratingforeachteamfromthebettingoddsofvarious
matches.ByusingthebettingoddsasaninputfortheELOcalculationinELO-Odds,wemade
theinformationincludedinthebettingoddsvisibleintermsofateamrating.Theresultsof
theprevioussectionhavealreadyshownthatELO-Oddsingeneralprovidesasuperiorestima-
tionofteamquality.Wewouldliketoillustratethiswithreferencetotworemarkableexam-
ples.CertainlytheseexamplescannotbeseenasaproofforthesuperiorityofELO-Odds,but
theycanbeusefultoillustratedifferencesinqualityestimationandhowthesecanbeusedto
understandthequalitydevelopmentofteams.
BeforecomparingELO-Oddstoratingsbasedonresultsorgoals,weneedtoverifythatthe
differentELOmeasuresarecomparableatall.Pleasenotethatduetotheconstructionofthe
ELOcalculation,pointsgainedbyoneteamareequallylostbyanotherteam.Thereforethe
sumofpointsforallteamsinourdatabasestaysconstantoverthewholeperiodofinvestiga-
tion.Asaresult,theratingsarecomparableintermsofsizeanditispossibletocomparethe
qualityestimationofteams(inELOpoints)betweendifferentmodels.Inparticularitbecomes
possibletoanalyzedifferencesbetweenELO-OddsandELO-Resultonateamlevelandconse-
quentlytogainmoredetailedinsightsonthequalityandperformancedevelopmentofeach
soccerteam.
Fig5showstheratingsfortheGermanteamBorussiaDortmundwithintheseasons2013/
2014and2014/2015(periodfromAugust2013–May2015).BothELO-Results(k=14)and
ELO-Odds(k=175)arepresented.Havingbeenoneofthebestteamsinthepreviousseasons,
Dortmundalsofinishedsuccessfullyas2ndintheseason2013/2014.Despitesmalldeviations
(especiallyatthebeginningoftheseason),theratingsforELO-ResultandELO-Oddsare
mainlyinlineandvirtuallynodifferenceinratingsexistsattheendoftheseason.InFebruary
2015–afterhavingmassivelyunsuccessfulresultsforhalfayear–Dortmundwasinlastposi-
tionoftheleaguetable.ConsequentlyELO-Resultshowsadrasticdecreaseofalmost100rat-
ingpoints.SurprisinglyELO-Oddsforalongtimehardlyshowsanyreactiontothe
unsuccessfulperiod,provingthatthemarketjudgementoftheteamqualitywasonlyweakly
modified.Thesubsequentdevelopmentmightbeinterpretedasaconfirmationofthisjudge-
mentasDortmundwasplayingasuccessfulrestoftheseasonandfinished2ndand3rdinthe
twofollowingseasons.
Fig6showstheratingsfortheEnglishteamLeicesterCitywithintheseasons2014/2015
and2015/2016(periodfromAugust2014–May2016).Asapromotedteam,Leicesterfinished
14thinthe2014/2015season.ThroughoutthecompleteseasonELO-Oddsisnoticeablyhigher
thanELO-Results.Attheendoftheseason2014/2015thereisagapofroughly50points
betweenthetworatings,indicatingthatthemarketclearlyratedtheteamhigherthanthe
actualresultsrevealed.Duringtheseason2015/2016LeicesterwonthePremierLeaguebeing
oneofthemostexceptionalsuccessstoriesinrecentyear’sassociationsoccer.Duringthat
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 11/18

TheBettingOddsRatingSystem
Fig5.ELO-OddsandELO-ResultofBorussiaDortmundwithintheseasons2013/14and2014/15.
https://doi.org/10.1371/journal.pone.0198668.g005
timeELO-Resultincreasesdramatically,addingroughly130pointstoLeicester’srating,
whereastheincreaseinELO-Oddsisnoticeablyweaker(roughly60points).Similarlytothe
precedingexample(yetintheoppositedirection)thesuccessfulresultswereonlymildly
reflectedinthemarketjudgementontheteam’squality.Leicesterfinished12thinthefollowing
season,whichagainfitsclosertothecautiousmarketjudgementthantotheratingbasedon
results.
Inlightoftheresultsofthisstudy,theseexamplesshowtheeffectiveuseofabettingodds
basedratinginordertogainpracticalinsightsintothequalityofsoccerteams.Moreover,they
areimpressivelyshowingthatsoccerresultsseemtobeaveryone-dimensionalandthusan
insufficientreflectionofteamquality.ThisresultisinlinewithHeueretal.[29]whodescribe
“scoringgoals”asa“highlyrandomprocess”.Thisisthemajorreasonforusinghardlydefin-
able,butvaluablecriterialikechancesforgoalstoestimateteamquality[30].Moreover,it
Fig6.ELO-OddsandELO-ResultofLeicesterCitywithintheseasons2014/15and2015/16.
https://doi.org/10.1371/journal.pone.0198668.g006
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 12/18

TheBettingOddsRatingSystem
Table5. ComparisonbetweenleaguetableandaverageELO-Oddsrating(PrimeraDivision2013/14).
| Pos. | Team              | GoalDiff. | Points | Pos. | Team              | ELO-Odds |         |
| ---- | ----------------- | --------- | ------ | ---- | ----------------- | -------- | ------- |
| 1.   | Atle´ticoMadrid   | 51        | 90     | 1.   | FCBarcelona       |          | 1294.59 |
| 2.   | FCBarcelona       | 67        | 87     | 2.   | RealMadrid        |          | 1229.22 |
| 3.   | RealMadrid        | 66        | 87     | 3.   | Atle´ticoMadrid   |          | 1174.11 |
| 4.   | AthleticBilbao    | 27        | 70     | 4.   | FCValencia        |          | 1057.04 |
| 5.   | FCSevilla         | 17        | 63     | 5.   | AthleticBilbao    |          | 1045.58 |
| 6.   | FCVillarreal      | 16        | 59     | 6.   | RealSociedad      |          | 1033.51 |
| 7.   | RealSociedad      | 7         | 59     | 7.   | FCVillareal       |          | 1022.52 |
| 8.   | FCValencia        | −2        | 49     | 8.   | FCSevilla         |          | 989.47  |
| 9.   | CeltaVigo         | −5        | 49     | 9.   | EspanyolBarcelona |          | 983.53  |
| 10.  | LevanteUD         | −8        | 48     | 10.  | FCMa´laga         |          | 973.85  |
| 11.  | FCMa´laga         | −7        | 45     | 11.  | BetisSevilla      |          | 968.70  |
| 12.  | RayoVallecano     | −34       | 43     | 12.  | CeltaVigo         |          | 962.58  |
| 13.  | FCGetafe          | −19       | 42     | 13.  | FCGetafe          |          | 946.62  |
| 14.  | EspanyolBarcelona | −10       | 42     | 14.  | FCGranada         |          | 941.67  |
| 15.  | FCGranada         | −24       | 41     | 15.  | FCElche           |          | 941.33  |
| 16.  | FCElche           | −20       | 40     | 16.  | RayoVallecano     |          | 940.17  |
| 17.  | UDAlmer´ıa        | −28       | 40     | 17.  | CAOsasuna         |          | 938.78  |
| 18.  | CAOsasuna         | −30       | 39     | 18.  | RealValladolid    |          | 933.25  |
| 19.  | RealValladolid    | −22       | 36     | 19.  | UDAlmer´ıa        |          | 928.16  |
| 20.  | BetisSevilla      | −42       | 25     | 20.  | LevanteUD         |          | 915.48  |
https://doi.org/10.1371/journal.pone.0198668.t005
givesrisetotheideaofcalculatingadvancedkeyperformanceindicatorsusingpositiondata
fromsoccermatches[31,32].
Admittedly,thetwoexamplesrefertoveryspecialsituationsandwereexplicitlychosenin
ordertoillustratedifferencesinratings.Moreover,bothsituationswereonlydiscussedvery
brieflynotconsideringeventslikethecoachofDortmundannouncingtoleavetheclubduring
theseasonorpossiblepsychologicalandmotivationaleffectshamperingtheperformanceof
Leicesterafterthesurprisingchampionship.
Analyzingleaguetables
Table5showsthefinalleaguetablefromthe2013/2014seasoninSpanishPrimeraDivision
(leftside).Theusualperceptionwouldbethatafter38matchestheteamsarefairlywell
orderedrelatedtotheirunderlyingqualitythroughoutthewholeseason.Asacomparisonthe
teamswereorderedfollowingtheaverageELO-Oddsratingduringtheseasonandpresented
attherightsideofthetable.Thereisastrongsimilaritybetweenbothrankings,butlikewise
thereareafewnotablediscrepancies.AtleticoMadridwonthetitlealthoughclearlybeing
rankedinthirdpositionbythebettingmarketbehindFCBarcelonaandRealMadrid.Given
theoutstandingroleofFCBarcelonaandRealMadrid,thisresultmightnotbesurprisingand
willbeinlinewiththeperceptionofmanysoccerexperts,coachesandofficialsatthattime.
Differencesconcerninglesssuccessfulteamsaremoreinteresting.Accordingtothemarket
valuationLevanteUDwastheworstteamintheleagueduringthisseasonalthoughfinishing
10thintheleaguetable.Incontrasttothat,BetisSevillawasranked11thbythemarket,butin
factwasrelegatedattheendoftheseason.
Thiscomparisongivesvaluableinsightstothedifferencebetweenresultsandmarketvalua-
tionofteams.Certainly,wedonothavefullknowledgeabouttheexactmechanismsofperfor-
manceanalysisinprofessionalsoccerclubs.Fromanoutsidepositionandfollowingthe
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 13/18

TheBettingOddsRatingSystem
detailedmediacoverage,however,itseemsthatresultsarebyfarthemostimportantbasisof
decision-making.Underthebackgroundofthisstudy,clubofficialsshouldpaymoreattention
tocarefulperformanceanalysisbyassessingvarioussourcesofinformationthansolelylooking
attheresultswhenevaluatingtheworkofplayersandcoaches.
Bettingreturns
Wheninvestigatingaquantitativemodelforforecastingsoccermatches,acommonapproach
istoexaminethefinancialbenefitofthemodelbyback-testingvariousbettingstrategiesand
calculatingthebettingreturns.Forreasonsofcompletenessandcomparabilitytootherstudies,
bettingreturnsfordifferentELOmodelswerecalculatedandcanbefoundinS1File.How-
ever,wewouldliketopointoutthatgainingpositivebettingreturnscannotbeequatedwitha
superiorpredictivequalityoftheunderlyingmodelasmeasuredbystatisticalmeasures.The
naïvemodelofassigning100%winningprobabilitytoeachawayteamwouldyieldpositive
bettingreturnsiftheprobabilityofawaywinswasgenerallyunderestimatedinthebetting
odds.However,itwouldcertainlynotbejudgedasavaluableprobabilisticforecastingmodel.
Thisexampleillustratesthatfindingprofitablebettingstrategiesandfindingaccurateforecast-
ingmodelsareslightlydifferenttasks.
Inaddition,ELO-Oddsisintendedtoconnecttheadvantagesofbettingoddsandmathe-
maticalmodelsbyextractinginformationfrombettingoddsandusingtheminmathematical
models.Consequentlyitwould–bydesign–beunreasonabletoexpectsystematicallypositive
bettingreturnsfromsuchamodel.Basedonthesereasons,thefocusofthisstudyisonevaluat-
ingthepredictivequalityofaforecastingmodelintermsofstatisticalmeasuresanditsbenefit
inenablinginsightstoperformanceanalysis.
Discussion
Althoughthepredictivepowerofbettingoddsiswidelyaccepted[23,11],bettingoddshave
notbeenusedasabasistocreaterankingsandratings.Lotsofefforthasbeenmadeindevelop-
ingmathematicalmodelsinordertofindprofitablebettingstrategiesandthusbeatthebetting
market[1,20,16].Incontrast,wepursuethestrategyofusingbettingoddsasasourceofinfor-
mationinsteadoftryingtooutperformthem.Astheresultsshow,thisisapromisingapproach
inanattempttoextractrelevantinformationthatwouldbehardlyexploitableotherwisein
mathematicalmodels.
WecouldsuccessfullytransferpriorresultsconcerningELO-ratingsinassociationsoccer
[16]toadifferentsetofdataincludingbothdomesticandinternationalmatches.Thistransfer-
abilityofresultsshouldnotbetakenforgrantedasthestructureofthedataheavilydependson
thechoiceofteamsandcompetitions.Thedatasetusedhereischaracterizedbyfullsetsof
matcheswithintheleaguesand–inrelationtothis–onlyafewcross-references(i.e.interna-
tionalmatches)betweentheleagues.SeeFig7forasimplifiedillustrationofthedatabaseasa
networkofteams(nodes)andmatches(edges).Pleasenotethatforpurposesofthepresenta-
tionanexplainingexampleisdemonstrated,insteadofthefulldatabase.Theaforementioned
studywasmissinginternationalmatchesanddifferentcountries,butincludinglowerleagues.
Yetanothersituationappliesfornationalteamswhoareplayingrelativelyrarely.Tournaments
astheWorldCuptakeplaceonlyeveryfouryearsandareplayedinagroupstageandknock-
outmatches.Furthermatchesincontinentalchampionshipsorqualificationsarelacking
matcheswithopponentsfromdifferentcontinents.Inothersportsorcomparablecontexts
(suchassocialnetworks)thestructureagainmightbecompletelydifferent.
Fordatasetsliketheoneusedwithinthisstudy,theELOratingsystemmightnotbethe
optimalapproachasitisnotdesignedforindirectcomparison.Eachmatchdirectlyinfluences
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 14/18

TheBettingOddsRatingSystem
Fig7.Simplifiedillustrationofthedatabaseasanetworkofteams(nodes)andmatches(edges).
https://doi.org/10.1371/journal.pone.0198668.g007
theratingofbothcompetitorsandthuscanindirectlyinfluencethefutureratingofother
teams.However,amatchisneverdirectlyinfluencingtheratingofanon-involvedteam.We
wouldexpectanotablebenefitintreatingteamsandmatchesasanetworkandtakingadvan-
tageofthisstructureforfutureratingapproaches.Itcanbesupposedthatthiswillleadtoa
shortenedtimeperiodtoderiveusefulinitialratingsandmoreaccuratequalityestimations,
especiallyforteamsnotbeingpartofcross-references(i.e.competinginaninternationalcom-
petition)atall.
Sofar,onlyfewattemptstomakeuseofthenetworkstructure[33]orexplicitlyincluding
indirectcomparison[34]havebeenmadeinUSCollegeFootball.OthermethodsliketheMas-
seyrating(see[35]foranintroduction)canbearguedtoimplicitlytakeadvantageofthenet-
workstructure.However,thereisalackofgeneraltheoryandatheoreticalframeworkthat
investigatesthebestratingmethodsfordifferenttypesofnetworkstructures.
Anotheraspectcontributestothecomplexityofevaluatingratingandforecastingmethods.
ThequalityofaratingandforecastingmodelsuchasELO-Oddsdependsbothonitsabilityin
estimatingteamratingsanditsabilitytoforecasttheoutcomes,givenaccurateratings.As
matchresultsareaffectedbyrandomfactors,thetruequalityofateamisneverknownor
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 15/18

TheBettingOddsRatingSystem
directlyobservableandthusthequalityoftheratingcanonlybetestedindirectly.Moreover,it
canbeassumedthatthetruequalityofateamwillbesubjecttochangesovertime.Inviewof
this,itisdifficulttoprovewhichaspectofthemodelcarriesresponsibilityforachievingornot
achievingacertainpredictivequality.
Togainbetterinsightsintothequalityofratingmodels,itwillbeusefultoconductfurther
studiesusingamoretheoreticalframework.Thiscouldbeachievedbyconstructingtheoretical
datasetsincludingknownteamqualities(trueratings)andsimulateddatafortheobservable
results,applyingtheratingmodelstothisdatasetandthencomparingthecalculatedratings
withthetrueratings.
ELO-Oddsprovidesclearevidencefortheusefulnessofincorporatingexpertjudgementinto
quantitativesportsforecastingmodelsinordertoprofitfromcrowdwisdom.Furtherevidence
forthepowerofexpertjudgementcanbefoundinPeeters[20]wherecollectivejudgementson
themarketvalueofsoccerplayersfromawebsitearesuccessfullyusedinforecastingtasks.
Moreover,researchersrecentlyhavestartedattemptstoextractcrowdwisdomfromsocial
mediadata.AnexampleaimingatsoccerforecastingcanbefoundinBrownetal.[36]where
TwitterdataareusedtodetectmispricinginlivebettingoddsofthebetexchangeBetfair.
Conclusion
Withinthisstudywemadeuseofbettingoddsasahighlyvaluabletoolinprocessingavailable
informationandforecastingsportsevents.Thebettingoddsthemselvesareameasureforthe
expectedsuccessinthefollowingmatch.Usingourapproach,wecandirectlymaptheseexpecta-
tionsofthemarkettoaquantitativeratingofeachteam,i.e.ameasureofteamquality.Thismea-
sureprovestobesuperiortoresultsorgoalswhenusedwithinaframeworkofanELOforecasting
model.WedidnotevaluatethedifferencesbetweenELO-Oddsandthebettingoddsthemselvesin
detail.Futurestudiesinvestigatingmatchrelatedaspects(suchasmotivationalaspects,line-up,
etc.)mighthelptofindandgaininsightsintofactorsthatinfluencethebettingoddsofamatch,
butarenotrelatedtothegeneralteamquality.Incontrasttopriorresearch,weemphasizedthat
ratingmethodsandforecastingmodelscanhelptogaininsightstotheunderlyingprocessesin
sportsandthatthereisastronglinkbetweenforecastsandperformanceanalysis.
Thepresentstudyisfurtherevidencethatresultsandgoalsarenotasufficientinformation
basisforratingsoccerteamsandforecastingtheoutcomesofsoccermatches.Expertopinion
canpossesshighlyvaluableinformationinforecasting,futureratingandforecastingmodels
shouldbecomemoreopentoincludesourcesofcrowdwisdomintomathematicalapproaches.
Intimesofsocialnetworksandonlinecommunicationnewpossibilitieshaveemergedand
willkeepemerging.Hugedatasetsfromsocialmedia(e.g.Twitterdata)orsearchengines(e.g.
Googlesearchqueries)havejustbeenstartedtobeexploredinthescientificcommunityand
areachallenging,buthighlypromisingapproachtobeusedinratingandforecasting.Dueto
thelackofanalternative,sport-scientificstudiesregularlyusewins/losses,thenumberofgoals
orleaguetablepositionsasameasuretodifferentiatebetweenstrongerandweakersoccer
teams.Withrespecttothemethodsandresultsshownwithinthisstudy,ameasurebasedon
bettingoddswouldbemoresuitablethantheaforementionedmeasuresbasedonresults,goals
orleaguetables.Thiscouldbeadaptedinfutureresearchbytakingadvantageofthe
ELO-Oddsratingasanimprovedmethodtoassessteamqualities.
Supportinginformation
S1File.Appendix.Appendixincludingdetailsoncalculatingprobabilitiesfrombettingodds
(AppendixA)andtheinvestigationofbettingstrategies(AppendixB).
(DOCX)
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 16/18

TheBettingOddsRatingSystem
S2File.MinimalDataSample.Datasetincludingtheminimaldataneededtoreplicatethe
studyaswellasmainresults(ratings)intendedtobeusablebyotherresearchersinfuture
research.
(XLSX)
AuthorContributions
Conceptualization:FabianWunderlich.
Datacuration:FabianWunderlich.
Investigation:DanielMemmert.
Methodology:FabianWunderlich.
Projectadministration:DanielMemmert.
Resources:DanielMemmert.
Supervision:DanielMemmert.
Validation:DanielMemmert.
Visualization:FabianWunderlich.
Writing–originaldraft:FabianWunderlich.
Writing–review&editing:DanielMemmert.
References
1. DixonMJ,ColesSG"(1997)Modellingassociationfootballscoresandinefficienciesinthefootballbet-
tingmarket.JournaloftheRoyalStatisticalSociety:SeriesC(AppliedStatistics)(46.2):265–280.
2. SˇtrumbeljE,VračarP(2012)SimulatingabasketballmatchwithahomogeneousMarkovmodeland
forecastingtheoutcome.InternationalJournalofForecasting 28(2):532–542.
3. LasekJ,Szla´vikZ,BhulaiS(2013)Thepredictivepowerofrankingsystemsinassociationfootball.
IJAPR 1(1):27.
4. BarrowD,DrayerI,ElliottP,GautG,OstingB(2013)Rankingrankings.Anempiricalcomparisonofthe
predictivepowerofsportsrankingmethods.JournalofQuantitativeAnalysisinSports 9(2).
5. KarlisD,NtzoufrasI(2003)AnalysisofsportsdatabyusingbivariatePoissonmodels.JRoyalStatisti-
calSocD 52(3):381–393.
6. NewtonPK,AslamK(2009)MonteCarloTennis.AStochasticMarkovChainModel.JournalofQuanti-
tativeAnalysisinSports 5(3).
7. AnderssonP,EdmanJ,EkmanM(2005)PredictingtheWorldCup2002insoccer.Performanceand
confidenceofexpertsandnon-experts.InternationalJournalofForecasting 21(3):565–576.
8. SpannM,SkieraB(2009)Sportsforecasting.Acomparisonoftheforecastaccuracyofpredictionmar-
kets,bettingoddsandtipsters.JournalofForecasting 28(1):55–72.
9. AnderssonP,MemmertD,PopowiczE(2009)ForecastingoutcomesoftheWorldCup2006infootball.
Performanceandconfidenceofbettorsandlaypeople.PsychologyofSportandExercise 10(1):116–
123.
10. McHaleI,MortonA(2011)ABradley-Terrytypemodelforforecastingtennismatchresults.Interna-
tionalJournalofForecasting 27(2):619–630.
11. LeitnerC,ZeileisA,HornikK(2010)Forecastingsportstournamentsbyratingsof(prob)abilities.A
comparisonfortheEURO2008.InternationalJournalofForecasting 26(3):471–481.
12. BoulierBL,SteklerHO(1999)Aresportsseedingsgoodpredictors.Anevaluation.InternationalJournal
ofForecasting 15(1):83–91.
13. WorldFootballEloRatings.Availablefrom:http://www.eloratings.net/.Accessed10November2017.
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 17/18

TheBettingOddsRatingSystem
14. KovalchikSA(2016)SearchingfortheGOAToftenniswinprediction.JournalofQuantitativeAnalysis
inSports 12(3):311.
15. RyallR,BedfordA(2010)Anoptimizedratings-basedmodelforforecastingAustralianRulesfootball.
InternationalJournalofForecasting 26(3):511–517.
16. HvattumLM,ArntzenH(2010)UsingELOratingsformatchresultpredictioninassociationfootball.
InternationalJournalofForecasting 26(3):460–470.
17. GoddardJ(2005)Regressionmodelsforforecastinggoalsandmatchresultsinassociationfootball.
InternationalJournalofForecasting 21(2):331–340.
18. WunderlichF,MemmertD(2016)AnalysisofthepredictivequalitiesofbettingoddsandFIFAWorld
Ranking.Evidencefromthe2006,2010and2014FootballWorldCups.Journalofsportssciences 34
(24):2176–2184.https://doi.org/10.1080/02640414.2016.1218040PMID:27686243
19. OttavianiS(2008)Thefavorite-longshotbias:AnOverviewoftheMainExplanations.Handbookof
SportsandLotterymarkets,83–101.
20. PeetersT(2018)TestingtheWisdomofCrowdsinthefield.Transfermarktvaluationsandinternational
soccerresults.InternationalJournalofForecasting 34(1):17–29.
21. KoopmanSJ,LitR(2015)AdynamicbivariatePoissonmodelforanalysingandforecastingmatch
resultsintheEnglishPremierLeague.JournaloftheRoyalStatisticalSociety:SeriesA(Statisticsin
Society), 178(1):167–186.
22. ConstantinouAC,FentonNE,NeilM(2012)pi-football.ABayesiannetworkmodelforforecastingAsso-
ciationFootballmatchoutcomes.Knowledge-BasedSystems 36:322–339.
23. ForrestD,GoddardJ,SimmonsR(2005)Odds-settersasforecasters.ThecaseofEnglishfootball.
InternationalJournalofForecasting 21(3):551–564.
24. SˇtrumbeljE(2014)ACommentontheBiasofProbabilitiesDerivedFromBettingOddsandTheirUse
inMeasuringOutcomeUncertainty.JournalofSportsEconomics 17(1):12–26.
25. SˇtrumbeljE(2014)Ondeterminingprobabilityforecastsfrombettingodds.InternationalJournalof
Forecasting 30(4):934–943.
26. GlickmanME,JonesAC(1999)Ratingthechessratingsystem.Chance 12(2):21–28.
27. WittenIH,PalCJ,FrankE,HallMA(2017)Datamining.Practicalmachinelearningtoolsandtech-
niques. Cambridge,MA: MorganKaufmann.
28. HeuerA,RubnerO(2009)Fitness,chance,andmyths.Anobjectiveviewonsoccerresults.Eur.Phys.
J.B 67(3):445–458.
29. HeuerA,Mu¨llerC,RubnerO(2010)Soccer.IsscoringgoalsapredictablePoissonianprocess.Euro-
phys.Lett. 89(3):38007.
30. HeuerA,RubnerO(2012)Towardstheperfectpredictionofsoccermatches.7p.
31. ReinR,RaabeD,MemmertD(2017)"Whichpassisbetter?"Novelapproachestoassesspassing
effectivenessinelitesoccer.Humanmovementscience 55:172–181.https://doi.org/10.1016/j.humov.
2017.07.010PMID:28837900
32. PerlJ,MemmertD(2017)APilotStudyonOffensiveSuccessinSoccerBasedonSpaceandBallCon-
trol–KeyPerformanceIndicatorsandKeytoUnderstandGameDynamics.InternationalJournalof
ComputerScienceinSport 16(1):12.
33. ParkJ,NewmanMEJ(2005)Anetwork-basedrankingsystemforUScollegefootball.JournalofStatis-
ticalMechanics:TheoryandExperiment, 2005(10),P10014
34. WignessMB,WilliamsCC,RowellMJ(2010)ANewIterativeMethodforRankingCollegeFootball
Teams.JournalofQuantitativeAnalysisinSports 6(2).
35. GlickmanM,SternH(2017)EstimatingteamstrengthintheNFL.HandbookofStatisticalMethodsand
AnalysesinSports.
36. BrownA,RambaccussingD,ReadeJJ,RossiG(2017)Forecastingwithsocialmedia:evidencefrom
tweetsonsoccermatches.EconomicInquiry 20(3):1363.
PLOSONE|https://doi.org/10.1371/journal.pone.0198668 June5,2018 18/18