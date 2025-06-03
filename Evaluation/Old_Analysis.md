This file will contain a summary of the evaluation metrics of various models. There will be justification for picking the best model.<br>

## PCA Results: <br>
![PCA Results](/Users/githika/GitHub/data_mining/Evaluation/scree_plot.png)
Principal Component 1:<br>
  PRIMARY2: 0.1661 - Do you have a Primary Care Provider (Yes/No)<br>
  PRIMAR12: 0.1661 - If yes, how many times have you seen or talked to this kind of provider or professional in the past year? <br>
  OTHER_S2: 0.1661 - Have you seen a different type of doctor (not Primary care provider, OB/GYN, Nurse Practitioner, Psychiatrist, Psychologist)? <br>
  OTHER12: 0.1661 - If yes, how many times have you seen or talked to this kind of provider or professional in the past year?<br>
  OTHER2: 0.1661 - Have you seen a different type of doctor (not Primary care provider, OB/GYN, Nurse Practitioner, Psychiatrist, Psychologist)?<br><br>

Principal Component 2:<br>
  IMPRMEM2: 0.1943 - I take hormones, including birth control pills, to improve memory.<br>
  MENOSYM2: 0.1938 - I take hormones, including birth control pills, to resolve menopause symptoms. <br>
  FRNADVI2: 0.1930 - I take hormones, including birth control pills, becasue a friend or relative advised me to take them. <br>
  DONTKNO2: 0.1926 - I take hormones, including birth control pills, for a reason I don't know or remember. <br>
  REDUHAR2: 0.1924 - I take hormones, including birth control pills, to reduce the risk of heart disease. <br><br>

Principal Component 3:<br>
  THYRREM2: 0.2017 - Since your last study visit, I have my thyroid gland removed<br>
  OSTEPR12: 0.2009 - OSTEPR11 Do you take medications to prevent or treat osteoporosis (brittle or thinning bones such as Fosamax, Didronel, Evista, Miacalcin, Rocaltrol)?<br>
  FERTIL12: 0.2009 - Since your last study visit have you taken any fertility medications to help you get pregnant (Pergonal, Clomid)? <br>
  HEARTAT2: 0.1913 - Since your last study visit, has a doctor, nurse practitioner or other health care provider told you that you had a heart attack or treated you for it? <br>
  PRGNANT2: 0.1913 - Since your last study visit, have you been pregnant? Please include live births, stillbirths, abortions, miscarriages, tubal or ectopic pregnancies.<br><br>

Principal Component 4: <br>
  OTCTW82: 0.1440 - Have you been taking other over the counter (OTC) medication number 8 at least two times per week for the last month? <br>
  OTC102: 0.1428 - Have you taken any other over-the-counter pills or other medications (including liquids or ointments) that I haven't asked you about?<br>
  OTCTW72: 0.1336 - Have you been taking other over the counter (OTC) medication number 7 at least two times per week for the last month?<br>
  OTCTW112: 0.1291 - Have you been taking other over the counter (OTC) medication number 11 at least two times per week for the last month?<br>
  OTCTW92: 0.1274 - Have you been taking other over the counter (OTC) medication number 9 at least two times per week for the last month?<br><br>

Principal Component 5:<br>
  OTC102: 0.2032 - Have you been taking other over the counter (OTC) medication number 10 at least two times per week for the last month?<br>
  OTCTW82: 0.1944 - Have you been taking other over the counter (OTC) medication number 8 at least two times per week for the last month?<br>
  OTCTW112: 0.1871 - Have you been taking other over the counter (OTC) medication number 11 at least two times per week for the last month?<br>
  OTCTW152: 0.1845 - Have you been taking other over the counter (OTC) medication number 15 at least two times per week for the last month?<br>
  OTCTW142: 0.1845 - Have you been taking other over the counter (OTC) medication number 14 at least two times per week for the last month?<br><br><br>

## Decision Tree Results
![Decision Tree Results](/Users/githika/GitHub/data_mining/Evaluation/Decision_Tree_Results.png)

EMOACCO2 - During the past 4 weeks, have you had any of the following problems with your work or other regular daily activities as a result of any emotional problems (such as feeling depressed or anxious)? Accomplished less than you would like?<br>

PAPSMEA2 - Since your last study visit, have you had: a Pap Smear?<br>

MONEYPR2 - ince your last study visit, have you experienced any of the following: Major money problems?<br>

ACHES2 - The following questions are about specific health problems you may have had over the past two weeks. Back aches or pains?<br>

SHBG2 - The following measures that were collected at Visit 02 have been included in the codebook: SERUM HORMONE MEASURES Sex hormone-binding globulin measured in nM <br>

MARITAL2 - What is your current marital status? <br>

SABDAY2 - Date Form Completed<br>

SWANID - Study Assigned ID<br>

E2AVE2 - The following measures that were collected at Visit 02 have been included in the codebook: SERUM HORMONE MEASURES Estradiol (see important note below) * IMPORTANT NOTE: There were originally two estradiol result variables because estradiol was run in duplicate. E2AVE2 is the within-person arithmetic average of the two estradiol variables.<br>

PHYSPLE2 - B4. In the past 6 months, how physically pleasurable was your relationship with your partner<br>

Questions:<br>
Why was SWANID included? 

