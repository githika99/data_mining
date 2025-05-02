This will contain a summary of EDA with distribution plots of every feature we are interested in.

The Data Dictionary is a csv file that specifies, for each feature, the domain and encoding for every value in the domain. 

We plotted distributions of the following features of the data:

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
        
