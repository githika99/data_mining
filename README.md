# 🩺 Analyzing Barriers to Women’s Health Care Access  

---

## 📌 Project Objective  
Women not receiving sufficient OB-GYN healthcare may face delays in treatment and increased risk of complications. This project identifies which features in the SWAN dataset correlate with inadequate healthcare access to help institutions better screen and support at-risk individuals.

---

## 📊 Dataset  
**Study: SWAN1** Study of Women's Health Across the Nation (SWAN), 1998-2001: Family Medical History From Visits 02, 03, and 04 (ICPSR 30181)
- This dataset is referred to as SWAN1 throughout the repo.
**Study: SWAN2** Study of Women's Health Across the Nation (SWAN): Visit 02 Dataset, [United States], 1998-2000 (ICPSR 29401)
- This dataset is referred to as SWAN2 throughout the repo.

---

## Repo Organizaiton:
data - folder contains raw and processed data, terms and description of data.
EDA - folder contains distributions of all features. A summary of these findings is provided. 
Evaluation - folder contains evalution (Principle Component Analysis, Decision Trees, Chi-Square Test). A summary with plots of these evaluation metrics is present. 
presentation.pdf - Comprehensive presentation of entire project. In depth analysis of what is covered in this document. 

---

## 🧠 Technical Approach  

The project uses both statistical and machine learning techniques to uncover insights:

### 🧹 Data Preprocessing
- Data cleaning  
- High-cardinality feature removal (threshold: ≥ 50% unique values)  
- One-hot encoding of categorical variables  

### 🔍 Feature Analysis
- **Principal Component Analysis (PCA)**  
- **Decision Tree Classifier**  
- **Chi-Square Statistical Test**  

---

## 🧪 Key Analyses and Results

### 🔹 PCA Results – SWAN2 Only  
- **PC1:** Primary Care & OB-GYN Visit Frequency  
- **PC2:** Hormone Use Reason  
- **PC3:** General Health (e.g., thyroid, heart attack, osteoporosis)  
- **PC4–5:** Over-the-Counter Medication Usage  

### 🔹 PCA Results – SWAN1 + SWAN2 Combined  
- **PC1:** Visit Frequency  
- **PC2:** Hormone Use Reason  
- **PC3–5:** Hormone Use & Sister’s Health History  

### 🌳 Decision Tree Insights  
- Identified features with high correlation to inadequate healthcare  
- Removed high-cardinality features to reduce overfitting  
- **Key Features Detected:**
  - Pap smear since last visit  
  - Marital/relationship status  
  - Emotional or physical health affecting normal activity  

### 🧮 Chi-Square Test Results  
- 405 features statistically significant (p < 0.01)  
- **Top 10 Examples:**
  - Survey completion date  
  - Pap smear since last visit  
  - Mammogram since last visit  
  - Marital/relationship status  
  - Family income  
  - Emotional and physical health impacts on work/activity  
  - Talking to doctors since last visit  

### 🔹 PCA on Significant Chi-Square Features  
- **PC1:** Major health conditions (e.g., heart attack, thyroid issues)  
- **PC2:** Reached out to doctor/professional for Psychological help
- **PC3:** Felt they were discriminated against  
- **PC4:** Felt emotional distress  
- **PC5:** Interview language  

---

## 📈 Visualizations  
- Located in `EDA/` and `Evaluation/` folders  
- Bar plots for PCA and decision tree feature importances  

---

## 🧠 Conclusions  

Certain factors consistently correlate with inadequate OB-GYN healthcare:
- **Pap smear since last visit**
- **Married/Committed relationship**
- **Emotional or physical health issues interfering with daily life**

**Actionable Insight:**  
Healthcare providers can proactively screen for these factors and schedule check-ins for patients meeting multiple risk indicators.

---

## 🔄 Limitations and Future Work

### ⚠ Limitations  
- Dataset may not generalize across broader populations  
- Demographics like race and income were analyzed, but other influential factors may exist  

### 🔬 Future Work  
- Use newer or complementary datasets for broader insights  
- Investigate *why* the identified factors prevent access to care  
- Partner with healthcare institutions to evaluate screening tools based on these findings  

---

## 💡 Value  

This project is a **social science analysis** aimed at improving **health equity**. 
The findings can inform healthcare providers and policymakers to create more inclusive, proactive care models for women.

