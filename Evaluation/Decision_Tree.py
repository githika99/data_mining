import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def remove_high_cardinality_features(df, threshold=0.50):
    """Remove features where the proportion of unique values is too high."""
    high_cardinality_cols = [
        col for col in df.columns
        if df[col].nunique() / len(df) > threshold
    ]
    print(f"Removed high-cardinality columns: {high_cardinality_cols}")
    return df.drop(columns=high_cardinality_cols), high_cardinality_cols


if __name__ == "__main__":
    # Load your encoded dataframe
    df = pd.read_csv("../data/Processed_Data/study1_2_encoded.csv")  # or use df_encoded directly if already in memory

    # Specify your response variable (change this to your actual column name)
    target_column = "HLTHSER2"

    # Remove high-cardinality features before dropping target-related columns
    df_cleaned, dropped_cols = remove_high_cardinality_features(df)

    # Split into features (X) and target (y)
    X = df_cleaned.drop(columns=["HLTHSER2", "HLTHSV12", 'HLTHSV22', 'HLTHSV32', 'PRIMREA2']) #, 'REASSPE2'
    y = df_cleaned[target_column]

    # Split into train/test (optional, but good practice)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a decision tree classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Get feature importances
    importances = pd.Series(clf.feature_importances_, index=X.columns)
    important_features = importances[importances > 0.01].sort_values(ascending=False)

    dic = {"EMOACCO2":"Accomplished less past month due to emotional problem",
           "PAPSMEA2":"Pap smear since last visit",
           "MONEYPR2":"Money problems upsetting since last visit",
           "ACHES2":"Back aches/pains past 2 weeks",
           "SHBG2": "Sex hormone-binding globulin (nM)",
           "MARITAL2":"Marital status",
           "SABDAY2":"Self-administered-Part B Day",
           "SWANID": "Respondent ID",
           "E2AVE2":"Estradiol",
           "PHYSPLE2":"Relationship with Partner is Physically Pleasurable",
            "LMPDAY2": "Last menstrual period day",
            "MI2": "Body mass index",
            "SYSBP12": "Systolic blood pressure (BP)",
            "OTHRPRS2": "Biological Mother menopause symptoms",
            "NOTSMAR2": "People think not as smart as others",
            "BCDIAP12": "Paternal Aunt's age at breast cancer diagnosis",
            "SERIPRO2": "Serious family problem upsetting since last visit",
            "VLNTHR12": "Hours spent Volunteering",
            "TIRED2" : "In the past 4 weeks, how often did you feel tired?",
            "SISAGE12": "Sister 1 Age",
            "HIP2": "Hip Circumference",
            "POORSER2": "Received poorer service than others at restaurants/stores",
            "DIABDAD2": "Dad has diabetes",
            "CONTROL2": "Unable to control important things in your life",
            "PHYACCO2": "Accomplished less due to physical pain",
            "HEIGHT2": "Height",
            "COUGHIN2": "Urinate when coughing",
            "SPEDAY2": "Survey Completion Date",
            "AFRAIDO2": "People act as if they are afraid of you",
            "WATCHTV2": "Since your last visit did you watch TV"
            }
    
    # Plot feature importances
    # top_features = importances.head(5)
    # mapped_labels = top_features.index.map(lambda x: dic.get(x, x))
    # plt.figure(figsize=(max(10, len(important_features) * 0.4), 6))

    # mapped_labels.plot(kind='bar', color='skyblue')

    # plt.xticks(rotation=45, ha='right')
    # plt.title("Features with Importance > 0.01")
    # plt.ylabel("Importance Score")
    # plt.tight_layout()

    # Print to inspect
    print("Top important features:\n", important_features)

    # Select top 10 features
    #top_features = importances.head(5)

    # Convert to string in case feature names are not
    important_features.index = important_features.index.astype(str)

    # Replace codes with descriptive names where available
    mapped_labels = important_features.index.map(lambda x: dic.get(x, x))

    # Plot with descriptive labels
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.barh(mapped_labels, important_features.values, color='skyblue')
    plt.gca().invert_yaxis()
    plt.title("Significant Features (Decision Tree)")
    plt.xlabel("Importance Score")
    plt.tight_layout()

    # Save the plot
    scree_path = "./plots/Decision_Tree_Results_5.png"
    plt.savefig(scree_path)
    plt.close()




"""
* sex hormone-binding has many different responses 
* SWANID has many different responses. that could be why a correlation was found
* SABDAY2 is not relevant. 
* Estradiol is not relevant. 
"""
