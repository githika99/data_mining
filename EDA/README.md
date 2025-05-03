This will contain a summary of EDA with distribution plots of every feature we are interested in.

The Data Dictionary is a csv file that specifies, for each feature, the domain and encoding for every value in the domain. 

We plotted distributions of the following features of the data:

SWAN 1:
Mom:
    MOMALIV2 - Is your biological mother (the one who gave birth to you) still living? - PIE CHART
        No - 1
        Yes - 2
        Don't Know - -8
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    MOMDIED2 - How old was your mother when she died? - Histogram
        Years
        Don't Know - -8
        Still Alive - -1
        Note: We ignored Don't Know and Still Alive values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    MOMCOD2 - What was the cause of death? - Histogram or - PIE CHART
        Text
        Still Alive - Blank
        Note: We ignored Still Alive values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    MOMAGE2 - How old is your mother now? - Histogram
        Years
        Don't Know - -8
        Not Alive - -1
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    AGESTOP2 - Age your mother stopped menstrating - Histogram
        <30 - 1 
        30-34 - 2 
        35-39 - 3 
        40-44 - 4 
        45-49 - 5 
        50-54 - 6
        55+ - 7 
        STILL MENSTRUATING WHEN SHE DIED - 8 (C4) 
        UNCERTAIN IF STILL MENSTRUATING WHEN SHE DIED - 9 (C4) 
        STILL MENSTRUATING DUE TO TAKING HORMONES - 10 (C4) 
        DON’T KNOW - -8
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    STOPMEN2 - Did she stop menstruating naturally or did she stop due to surgery, medication or radiation treatments? - PIE CHART
        Natural - 1
        Surgery - 2
        Medical/Radiation - 3
        Don't Know - -8
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 
    SYMPTOM2 - Did your biological mother have any symptoms such as hot flashes, irregular or heavy periods, sleep problems or mood changes or problems associated with stopping her menstruation? - PIE CHART
        No - 1
        Yes - 2
        Don't Know - -8
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 

    Following are symptoms: (Domain is same as for SYMPTOM2) - PIE CHART
        HOTFLA2
        HEVYPER2	
        SLEEPRO2	
        PSYPROB2	
        OTHRPRO2	
        OTHRPRS2
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 

    
    HERMENO2 - How much did the woman who raised you discuss her menopause with you?  - PIE CHART
        Not at all - 1
        In some detail - 2
        In great detail - 3
        NOT APPLICABLE - -1 (D1)
        Note: We ignored Not Applicable values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 

    GENMENO2 - How often did she discuss menopause in general with you? - PIE CHART
        Never - 1 
        Occasionally or rarely - 2 
        Sometimes -  3 
        Often - 4

    ATTIMEN2 - Which of the following best describes her overall attitudes or perceptions about menopause? - PIE CHART
        Neutral - 1 
        Positive - 2 
        Negative - 3 
        DON’T KNOW - -8
        
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 


    Following are Health Conditions. Participants are asked if their mother has ever been diagnosed with condition: (Domain is same as for SYMPTOM2) - PIE CHART
        ARTHRMO2 - Arthiritis
        HIBPMOM2 - High blood pressure
        DIABMOM2 - Diabetes
        STRKMOM2 - Stroke
        HEARTMO2 - Heart Attack
        OHDMOM2 - Other Heart Disease
        HIPMOM2 - Hip Fracture
        OSTEOMO2 - Osteoporosis
        SPINEMO2 - Spine Fracture
        HUMPMOM2 - Dawger's (spine) hump
        COLONMO2 - Colon cancer
        DEPRMOM2 - Depression lasting longer than 4 weeks

        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 



Dad: 
    DADALIV2 - Is your biological father still living? - PIE CHART
        No - 1
        Yes - 2
        Don't Know - -8
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 


    DADDIED2 - How old was your father when he died? - Histogram
        Years
        Don't Know - -8
        Still Alive - -1
        Note: We ignored Don't Know  and Still Alive values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 


    DADCOD2 - What was the cause of death? - Histogram or - PIE CHART
        Text
        Still Alive - Blank
        Note: We ignored Still Alive values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 


    DADAGE2 - How old is your father now? - Histogram
        Years
        Don't Know - -8
        Not Alive - -1
        Note: We ignored Don't Know and Not Alive values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 

    
    Following are Health Conditions. Participants are asked if their father has ever been diagnosed with condition: (Domain is same as for DADALIV2) - PIE CHART
        ARTHRDA2 - Arthiritis
        HIBPDAD2 - High blood pressure
        DIABDAD2 - Diabetes
        STRKDAD2 - Stroke
        HEARTDA2 - Heart Attack
        OHDDAD2 - Other Heart Disease
        HIPDAD2 - Hip Fracture
        OSTEODA2 - Osteoporosis
        SPINEDA2 - Spine Fracture
        HUMPDAD2 - Dawger's (spine) hump
        COLONDA2 - Colon cancer
        DEPRDAD2 - Depression lasting longer than 4 weeks
        
        Note: We ignored Don't Know values because they were so frequent that when plotted, the distribution of the other variables could not be easily seen. 


Brother:
    NUMBROS2  - PIE CHART

Sister:
    NUMSIS2  - PIE CHART

Data we're creating:
    BRECANUM - number of woman related to participant (mother, sister(s) - half or full, aunt, grandmother) who were diagnosed with breast cancer. 
        Count of 2 values in these columns: BCMOM2, BCMGR2, BCPGR2, BCOTH2
        Plus
        Sum of values in these columns: BCNUMSI2, BCNUMMA2, BCNUMPA2, 
    
    SISMENO - age at which sister(s) stopped having periods 
        Distribution of non -8 values in these columns: AGETO12, AGETO22, AGETO32, AGETO42, AGETO52, AGETO62, AGETO72, AGETO82, AGETO92, AGET102, AGET112, AGET122, AGET132, AGET142, AGET152, AGET162



Which attributes in SWAN2 focus on women's health.
What are some possible ideas of what we can predict? 
SWAN2:
    SWAN1 len 2829
    SWAN2 len 2748
    common 2729


Check Day that they did each to see which was completed first. 
PREGNAN2 - are you pregnant

Since your last visit have you ...
FERTIL12 FERTIL22 - Fertility medications to help you get pregnant (Pergonal, Clomid)?
BCP12 BCP22 - Birth Control Pills
ESTROG12 ESTROG22 - Estrogen pills
ESTRDA12 ESTRDA22 - Estrogen pill daily?
ESTRNJ12 ESTRNJ22 - Estrogen by injection or patch
COMBIN12 COMBIN22 - combination estrogen/progestin 
PROGES12 PROGES22 - progestin pill
PROGDA12 PROGDA22 - progestin pill daily?

Reason for taking hormones, including birth control pills. (1 - No, 2 - Yes)

REDUHAR2 - To reduce the risk of heart disease
OSTEOPO2 - To reduce the risk of osteoporosis
MENOSYM2 - To relieve menopausal symptoms
YOUNGLK2 - To stay young-looking
HCPADVI2 - A health care provider advised me to take them
FRNADVI2 - A friend or relative advised me to take them
IMPRMEM2 - To improve my memory
REGPERI2 - To regulate periods
HORMOTH2 - Other
    - specified in HORMSPE2
DONTKNO2 - Don't Know

For those that since thier last study visit, they started taking some hormones and then stopped. What were their reasons for stopping? (1 - No, 2 - Yes)

PRBBLEE2 - PROBLEMS WITH BLEEDING
HAVEPER2 - DIDN’T LIKE HAVING PERIODS
LIKEFEL2 - DIDN’T LIKE HOW I FELT ON THEM
SIDEEFF2 - WORRIED ABOUT POSSIBLE SIDE EFFECTS
CANCER2 - WORRIED ABOUT CANCER
ADVISTO2 - MY HEALTH CARE PROVIDER ADVISED ME TO STOP (FOR MEDICAL REASONS)
EXPENSI2 - TOO EXPENSIVE
NOLIKE2 - DON’T LIKE TO TAKE ANY MEDICATIONS
NOREMEB2 - COULDN’T REMEMBER TO TAKE THEM
DNTKNOW2 - DON’T KNOW
STOPOTH2 - Other
    - specified in STOPSPE2
No reason given - NOREASO2

Page 18 -- general health conditions
Page 20 -- OB GYN specific medical treatments
Page 21 -- about period

HOURSPA2 - how many hours do you work a week for pay
    ≤ 10 ........................................................................................................................ 1 11-19 ...................................................................................................................... 2 20-34 ...................................................................................................................... 3 35-40 ...................................................................................................................... 4 41-60 ...................................................................................................................... 5 >60 ......................................................................................................................... 6
MARITAL2 - Marital Status
    Single/never married.............................................................................................. 1 Currently married or living as married .................................................................. 2 Separated ............................................................................................................... 3 Widowed................................................................................................................ 4 Divorced ................................................................................................................ 5 DON’T KNOW .................................................................................................... -8 REFUSED ........................................................................................................... -7


Page 32 - about hospital visits, for OB GYN stuff

HLTHSER2 - Since your last study visit, are there any health services that you needed but did not receive? No 1 Yes 2

HLTHSV12, HLTHSV22, HLTHSV32 - What kind of health services?

PRIMREA2 What is the primary reason for not receiving these health services? - Insurance or health plan does not cover................................................................. 1 Cannot afford......................................................................................................... 2 Travel distance / lack of transportation................................................................. 3 No health care provider ......................................................................................... 4 Too busy/ didn’t have the time .............................................................................. 5 Other ...................................................................................................................... 6

UTI2 - have you had any urinary tract infections? (No -1 Yes - 2)

INCOME2 - total family income
LESS THAN $19,999............................................................................................ 1 $20,000 TO $49,999 .............................................................................................. 2 $50,000 TO $99,999 .............................................................................................. 3 $100,000 OR MORE ............................................................................................. 4 REFUSED ........................................................................................................... -7 DON’T KNOW ................................................................................................... -8

PROVIDE2 - Do you have a health care provider from whom you primarily get your care for women's health conditions? (1 - No, 2- Yes)

TYPEPRA2 - What type of practice is this?
Hospital ............................................................................................................... 1 Office................................................................................................................... 2 Clinic ................................................................................................................... 3 Other ................................................................................................................... 4
Specify:____________________________________ #SPECIF12


SPECIAL2 - Which of the following best describes this provider’s specialty.
A family practitioner ............................................................................................. 1 An internist .......................................................................................................... 2 A gynecologist ..................................................................................................... 3 A nurse practitioner or physician assistant........................................................... 4 A naturopath (one who uses natural (non-medicinal) therapy)............................. 5 Other ................................................................................................................... 6
Specify:____________________________________ SPECIFY2
No specialty ............................................................................................... 7 Don’t know ................................................................................................ -8

VISIPRO2 - Since your last study visit, about how many times did you see or talk to this health care provider regarding your own health? (count)

ROLE2 - Please indicate what role you prefer that this health care provider take in deciding about your health
(scale 1 to 7)
My provider’s role is to provide information and let me make my own decision
1234567
My provider’s role is toevaluate my situation and make the best decision for me

Following are 1 - almost never, 2 - seldom, 3 - neutral, 4 - often, 5 - almost always

ENCOURA2 - My heath care provider encourages me to make my own decisions regardingtreatment plans.

DISCUSS2 - When my health care provider recommends treatment plans he/she also discusses alternatives.

REFUSAL2 - If I refuse treatment, my health care provider respects my decision.

PARTICI2 - My health care provider encourages me to participate in decisions about my health care.

ALTERNA2 - My health care provider seriously considers any alternative treatments that I suggest.

CHANGES2 - If I tell my health care provider my treatment plan is too difficult or too much trouble, he/she changes it.

JUDGEMN2 - My health care provider encourages me to trust my own judgment about my health care.

Page 59 - checking if you've had serious OB GYN related health probelms

STATUS2 - menopausal status 1 = Post by BSO (Bilateral Salpingo Oophorectomy)
2 = Natural Post
3 = Late Peri
4 = Early Peri
5 = Pre
6 = Pregnant/breastfeeding
7 = Unknown due to HT use
8 = Unknown due to hysterectomy

RACE - 1: Black/African American
2: Chinese/Chinese American
3: Japanese/Japanese American 4: Caucasian/ White Non-Hispanic 5: Hispanic

AGE2 - Age
