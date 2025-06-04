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
    df = pd.read_csv("/Users/githika/GitHub/data_mining/Evaluation/study1_2_encoded.csv")  # or use df_encoded directly if already in memory

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

    # dic = {"EMOACCO2":"Accomplished less past month due to emotional problem",
    #        "PAPSMEA2":"Pap smear since last visit",
    #        "MONEYPR2":"Money problems upsetting since last visit",
    #        "ACHES2":"Back aches/pains past 2 weeks",
    #        "SHBG2": "Sex hormone-binding globulin (nM)",
    #        "MARITAL2":"Marital status",
    #        "SABDAY2":"Self-administered-Part B Day",
    #        "SWANID": "Respondent ID",
    #        "E2AVE2":"Estradiol",
    #        "PHYSPLE2":"Relationship with Partner is Physically Pleasurable"}
    
    # Plot feature importances
    plt.figure(figsize=(max(10, len(important_features) * 0.4), 6))
    important_features.plot(kind='bar', color='skyblue')

    plt.xticks(rotation=45, ha='right')
    plt.title("Features with Importance > 0.01")
    plt.ylabel("Importance Score")
    plt.tight_layout()
    plt.show()

    print(important_features)

    # Map feature codes to descriptive questions
    # top_features = importances.head(10)
    # mapped_labels = top_features.index.to_series().map(dic).fillna(pd.Series(top_features.index, index=top_features.index))

    # # Plot with descriptive labels
    # plt.figure(figsize=(10, 6))
    # plt.barh(mapped_labels, top_features.values, color='skyblue')
    # plt.gca().invert_yaxis()
    # plt.title("Top 10 Important Features (Decision Tree)")
    # plt.xlabel("Importance Score")
    # plt.tight_layout()
    
    scree_path = "/Users/githika/GitHub/data_mining/Evaluation/Decision_Tree_Results_4.png"
    plt.savefig(scree_path)
    plt.close()



"""
* sex hormone-binding has many different responses 
* SWANID has many different responses. that could be why a correlation was found
* SABDAY2 is not relevant. 
* Estradiol is not relevant. 
"""
