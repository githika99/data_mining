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

What is being excluded: 
Vitamins: 
B22 - Since your last study visit, have you taken any vitamins or minerals fairly regularly, at least once a week?
B23. IF YES: Since your last study visit, what vitamins and minerals have you taken fairly regularly, at least once per week?
B23.l IF MULTIPLE VITAMIN USE REPORTED, Do you usually take multiple vitamins that:
B24. We’ve just talked about your prescription medications, over-the-counter medications, vitamins, and minerals you have taken since your last study visit. What did you take in the last 24 hours?
B25. Have you had any alcohol in the last 24 hours?

General Health: (1 - No, 2 - Yes, -8 Dont Know)

B29. Since your last study visit, how many times did you break or fracture a bone?
B30. Since your last study visit, have you consulted a doctor, nurse practitioner, chiropractor, or other health care provider for back pain?


C7. QLTYLIF2 - Quality of Life: Thinking about your quality of life at the present time, I’d like you to give it a rating where 0 represents the worst possible quality for you and 10 represents the best possible quality for you.
C8. CLOSE2 - About how many close friends and close relatives do you have, that is, people you feel at ease with and can talk to about what is on your mind? 

C9. People sometimes look to others for companionship, assistance, or other types of support. How often is each of the following kinds of support available to you if you need it?
LISTEN2 - Someone you can count on to listen to you when you need to talk? 
TAKETOM2 - Someone to take you to the doctor if you needed it?
CONFIDE2 - Someone to confide in or talk to about yourself or your problems?
HELPSIC2 - Someone to help with daily chores if you were sick?

I would now like to ask you about your feelings over the past two weeks. Tell me how often you have felt or thought this way.
CONTROL2 - Felt unable to control important things in your life?
ABILITY2 - Felt confident about your ability to handle your personal problems? 
YOURWAY2 - Felt that things were going your way?
PILING2 - Felt difficulties were piling so high that you could not overcome them?

During the past week:
BOTHER2 - I was bothered by things that usually don’t bother me
APPETIT2 - I did not feel like eating; my appetite was poor
BLUES2 - I felt that I could not shake off the blues even with help from my friends
GOOD2 - I felt that I was just as good as other people
KEEPMIN2 - I had trouble keeping my mind on what I was doing
DEPRESS2 - I felt depressed 
EFFORT2 - I felt that everything I did was an effort
HOPEFUL2 - I felt hopeful about the future
FAILURE2 - I thought my life had been a failure
FEARFUL2 -  I felt fearful
RESTLES2 - My sleep was restless
HAPPY2 - I was happy
TALKLES2 - I talked less than usual
LONELY2 -  I felt lonely
UNFRNDL2 - People were unfriendly
ENJOY2 - I enjoyed life
CRYING2 - I had crying spells 
SAD2 - I felt sad
DISLIKE2 - I felt that people disliked me
GETGOIN2 - I could not get going

Employment/Volunteer:
CHNGJOB2 - Since your last study visit, has there been a change in any of your jobs, that is where you work, the usual hours you worked, or your usual job tasks?
JOB2 - During the past 2 weeks, did you work at any time at a job or business, including work for pay performed at home? Include unpaid work in the family farm or business. If you were on vacation, or scheduled leave or sick leave, please answer as though you were at your usual job.
JOBTIT12 JOBTIT22 JOBTIT32 - For each paid job you have had in the last two weeks, what was your job title?
JOBACT12 JOBACT22 JOBACT32 - Briefly, what are your usual job activities?
STRTIM12 to ROTAT32 - What are your usual hours of work each day for each job? 
VOLUNTE2 - Do you do volunteer work?
TYPVOL12 to VLNTHR32 - What type of volunteer work? How many hours a week do you spend doing it?
PARTNJO2 - What is/ was your partner or spouse’s job title for their primary, usual job or occupation?
PRTNRMA2 - What does the company or part of the company, that your spouse or partner works for, do or make?

SMOKERE2 - Since your last study visit, have you smoked cigarettes regularly (at least one cigarette a day)?
AVCIGDA2 - IF YES: How many cigarettes, on average, do you smoke per day now?
LASTSMO2 - IF NONE, (You stopped smoking), What was the last month you smoked?

For non-smokers:
HHMEMSM2 - Since your last study visit, how many other members of your household have smoked tobacco, inside the house (at least 1 cigarette, cigar or pipe bowl per day)?
HOMEXPD2 - During the past 7 days, how many days were you exposed to tobacco smoke in your home?
HOMEXPH2 - Over the past 7 days, when you were exposed to tobacco smoke in your home, how many hours were you exposed during a typical day?
Since your last study visit, did you drink any beer, wine, liquor, or mixed drinks? DRNKBEE2
GLASBEE2 - How many glasses of beer (a medium glass or serving of beer is twelve ounces) did you drink on average per day, week or month? (PLEASE CIRCLE ONLY ONE RESPONSE.) 
GLASWIN2 - How many glasses of wine or wine coolers, (a medium glass or serving of wine is 4 to 6 ounces), did you drink on average per day, week or month? (CIRCLE ONE NUMBER)
GLASLIQ2 - How many glasses of liquor or mixed drinks, (a medium serving is one shot), did you drink on average, per day, week or month? (CIRCLE ONE NUMBER)

Physical or Emotional Pain Results:
During the past 4 weeks, have you had any of the following problems with your work or other regular daily activities as a result of your physical health?
PHYCTDW2 -  Cut down the amount of time you spent on work or other activities?
PHYACCO2 - Accomplished less than you would like?
PHYLIMI2 - Were limited in the kind of work or other activities?
PHYDFCL2 -  Had difficulty performing the work or other activities (for example, it took extra effort)?

During the past 4 weeks, have you had any of the following problems with your work or other regular daily activities as a result of any emotional problems (such as feeling depressed or anxious)?
EMOCTDW2 - Cut down the amount of time you spent on work or other activities?
EMOACCO2 - Accomplished less than you would like?
EMOCARE2 - Didn't do work or other activities as carefully as usual?
INTERFR2 - During the past 4 weeks, to what extent has your physical health or emotional problems interfered with your normal social activities with family, friends, neighbors, or groups?
BODYPAI2 - How much bodily pain have you had during the past 4 weeks?
PAINTRF2 - During the past 4 weeks, how much did pain interfere with your normal work (including both work outside the home and housework)?

During the past 4 weeks, how much time...
PEP2 0 Did you feel "full of pep"? 
ENERGY2 - Did you have a lot of energy?
WORNOUT2 - Did you feel worn out?
TIRED2 - Did you feel tired?

SOCIAL2 - During the past 4 weeks, how much of the time has your physical health or emotional problems interfered with your social activities (like visiting with friends, relatives, etc.)?

PHYSACT2 - In comparison with other women your age, is your usual level of physical activity.

WATCHTV2 - Since your last study visit, did you watch television?

WALKBIK2 - Did you walk or bike to and from work, school or errands?

SWEATPA2 - Did you sweat from exertion?

SPORTS2 - Since your last study visit, did you play sports or exercise?

CHORES2 - Since your last study visit, is your current level of physical activity doing chores around your home?

WORKPHY2 - Since your last study visit, is your current level of physical activity at work performed for pay.

PLANSPO2 - Since your last study visit, is your current level of physical activity in planned sports (such as volleyball, softball or tennis) and exercise (such as aerobics or jogging).

ROUTINE2 - Since your last study visit, is your current level of other routine physical activity (such as walking, gardening, climbing stairs, etc.)

Thinking back over the past two weeks, please circle the number corresponding to how often you experienced any of the following.
STIFF2 - Stiffness or soreness in joints, neck or shoulder?
ACHES2 - Back aches or pains?
COLDSWE2 - Cold sweats?
NITESWE2 - Night sweats? 
VAGINDR2 - Vaginal dryness?
FEELBLU2 - Feeling blue or depressed?
DIZZY2 - Dizzy spells?
IRRITAB2 -  Irritability or grouchiness?
NRVOUS2 - Feeling tense or nervous? 
FORGET2 - Forgetfulness?
MOODCHG2 - Frequent mood changes?
HARTRAC2 - Heart pounding or racing?
FEARFULA2 - Feeling fearful for no reason? 
HDACHE2 - Headaches?
HOTFLAS2 - Hot flashes or flushes?

In the past two weeks...
TRBLSLE2 - Did you have trouble falling asleep?
WAKEUP2 - Did you wake up several times a night?
WAKEARL2 -  Did you wake up earlier than you had planned to, and were unable to fall asleep again?
TYPNIGH2 - Overall, was your typical night's sleep during the past 2 weeks

Urination: 
GETUPUR2 - How often do you usually get up from bed at night to urinate?
INVOLEA2 - Since your last study visit, have you ever leaked, even a very small amount, of urine involuntarily?
DAYSLEA2 - In the last month, about how many days have you lost any urine, even a small amount, beyond your control?

Under what circumstances does it occur?
COUGHIN2 - Coughing
LAUGHIN2 - Laughing
SNEEZIN2 - Sneezing
JOGGING2 - Jogging
PICKUP2 - Picking up an object from the floor
URGEVOI2 - When you have an urge to void and can’t get to a toilet fast enough.
OTHRLEA2 - Other OTHRLEA2
AMTLEAK2 - How much urine do you lose when you leak?
LEAKBOT2 - On a scale from 0 to 10, where 0 = Not at all bothered and 10 = Extremely bothered, how much does the leakage of urine bother you?

Medicine: 
NUTRIRE2 - Special diets or nutritional remedies, such as macrobiotic or vegetarian diets, or vitamin supplements or therapy?
HERBREM2 - Herbs or herbal remedies, such as homeopathy or Chinese herbs or teas?
PSYCMET2 - Psychological methods, such as meditation, mental imagery, or relaxation techniques?
PHYSMET2 - Physical methods, such as massage, acupressure, acupuncture, or chiropractic therapy?
FOLKMED2 - Folk medicine or traditional Chinese medicine?
OTHRTHE2 - Any others?

Life Events:
Since your last study visit, have you experienced any of the following:
STARTNE2 - Started school, a training program, or new job?
WORKTRB2 - Had trouble with a boss or conditions at work
got worse?
QUITJOB2 - Quit, fired or laid off from a job?
WORKLOA2 - Took on a greatly increased work load at job?
PRTUNEM2 - Husband/partner became unemployed?
MONEYPR2 - Major money problems? 
WORSREL2 - Relations with husband/partner changed for the worse but without separation or divorce?
RELATEN2 - Were separated or divorced or a long-term relationship ended?
SERIPRO2 - Had a serious problem with child or family member (other than husband/partner) or with a close friend?
CHILDMO2 - A child moved out of the house or left the area?
RESPCAR2 - Took on responsibility for the care of another child, grandchild, parent, other family member or friend? 
LEGALPR2 - Family member had legal problems or a problem with police?



Household: 
HOUSEHL2 - Other than yourself, is there anyone else living in your household? 
RELAT12 to AGE122 - Please tell me their relationship to you, their gender, and their age.


Group Features I Will find the correlation of with my target/outcome:
Medication: B1 - B9, B19-B21, OSTEPR11 (page 29) (1 - No, 2 - Yes). Sum up the Yesses

Individual Features Im interested in:

Check Day that they did each to see which was completed first. 
PREGNAN2 - are you pregnant (1 - No, 2 - Yes, -8 Dont Know)

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

B26. Since your last study visit, has a doctor, nurse practitioner or other health care provider told you that you had any of the following conditions or treated you for them?
ANEMIA2 - Anemia
DIABETE2 - Diabetes
HIGHBP2 - High blood pressure or hypertension? 
HBCHOLE2 - High cholesterol? 
MIGRAIN2 - Migraines?
STROKE2 - Stroke?
OSTEOAR2 - Arthritis or osteoarthritis (degenerative joint disease)?
THYROID2 - Overactive or underactive thyroid?
HEARTAT2 - Heart attack?
ANGINA2 - Angina?
OSTEOPR2 - Osteoporosis (brittle or thinning bones)?
FIBROID2 - Fibroids, benign growths of the uterus or womb?
CANCERS2 - Cancer, other than skin cancer? 

SITESPE2 - What is/was the primary site of the cancer? (text)
TAMOXIF2 - IF BREAST CANCER: Have you taken Tamoxifen since your last study visit? (1 - No, 2 - Yes, -8 Dont Know, -1 Not Applicable)
CHEMOTH2 - Since your last study visit, have you received chemotherapy or radiation treatment for this (1 - No, 2 - Yes, -8 Dont Know) 

OBGYN Health: (1 - No, 2 - Yes)
DANDC2 - Since your last study visit, have you had any of the following surgeries or procedures? D and C, a scraping of the uterus for any reason, including abortion?
NUMDAND2 - How many times have you had a D and C? 
HYSTERE2 - B32. Since your last study visit, have you had any of the following surgeries or procedures?Hysterectomy (an operation to remove your uterus or womb)?
OOPHORE2 - B33. Did you have one or both ovaries removed (an oophorectomy)?
Was one ovary removed or were both ovaries removed?
ONEOVAR2 - ONE OVARY REMOVED - 1 BOTH OVARIES REMOVED - 2 DON’T KNOW - -8
UTERPRO2 - B34. Uterine procedures, other than D and C, for example:
cesarean section, IUD insertion, fibroid removal or endometrial biopsy? 
THYRREM2 - Thyroid gland removed?
BLEEDNG2 - Did you have any menstrual bleeding since your last study visit?
BLD3MON2 - Did you have any menstrual bleeding in the last 3 months?

For the next few questions I would like to ask you to think about your periods since your last study visit, during times when you were not using birth control pills or other hormone medications.
C4. Which of the following best describes your menstrual periods since your last study visit? Have they:
DESCPER2 - Become farther apart?  - 1 Become closer together? - 2 Occurred at more variable intervals? - 3 Stayed the same? - 4 Become more regular? - 5 DON’T KNOW - -8 NOT APPLICABLE - -1
MENSFLO2 - Since your last study visit, have you ever had a menstrual flow that lasted more than 10 days? NO - 1 YES - 2 DON’T KNOW - -8 REFUSED - -7 NOT APPLICABLE - -1
PRGNANT2 - Since your last study visit, have you been pregnant? Please include live births, stillbirths, abortions, miscarriages, tubal or ectopic pregnancies. NO - 1 YES - 2 
OUTCOME2 What was the outcome of the pregnancy? Live birth - 1 Still birth - 2 (C7) Miscarriage - 3 (C7) Abortion - 4 (C7) Tubal/ectopic pregnancy - 5 (C7) Still pregnant - 6
BRSTFEE2 - FOR LIVE BIRTHS ONLY: Are you currently breastfeeding? NO - 1 YES - 2 

HOURSPA2 - how many hours do you work a week for pay
    ≤ 10 - 1,  11-19 - 2,  20-34 - 3,  35-40 - 4,  41-60 - 5, >60 - 6
MARITAL2 - Marital Status
    Single/never married - 1, Currently married or living as married - 2, Separated 3,  Widowed 4, Divorced 5, DON’T KNOW -8, REFUSED -7

OVERHLT2 - In general, would you say your health is excellent, very good, good, fair or poor? Excellent 1, Very good 2, Good 3, Fair 4, Poor 5, Don’t know -8

HOSPSTA2 - Since your last study visit, how many different times did you stay in the hospital overnight or longer? (Number)

MDTALK2 - Since your last study visit, about how many times did you see or talk to a doctor, nurse practitioner or other health care provider, regarding your own health?

Since your last study visit, have you had:
PAPSMEA2 - Pap smear
BRSTEXA2 - Breast physical examination
MAMOGRA2 - mammogram

UTI2 - have you had any urinary tract infections? (No -1 Yes - 2)

INCOME2 - total family income
LESS THAN $19,999 1   $20,000 TO $49,999 2    $50,000 TO $99,999 3    $100,000 OR MORE 4    REFUSED  -7      DON’T KNOW -8

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


Target Variables/Outcome: 
HLTHSER2 - Since your last study visit, are there any health services that you needed but did not receive? No 1 Yes 2

HLTHSV12, HLTHSV22, HLTHSV32 - What kind of health services?

PRIMREA2 What is the primary reason for not receiving these health services? - Insurance or health plan does not cover 1, Cannot afford 2, Travel distance / lack of transportation 3, No health care provider 4, Too busy/ didn’t have the time 5, Other 6
REASSPE2 - Other text 
