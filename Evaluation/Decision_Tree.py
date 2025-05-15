import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load your encoded dataframe
    df = pd.read_csv("/Users/githika/GitHub/data_mining/Evaluation/study2_encoded.csv")  # or use df_encoded directly if already in memory

    # Specify your response variable (change this to your actual column name)
    target_column = "HLTHSER2"

    # Split into features (X) and target (y)
    X = df.drop(columns=["HLTHSER2", "HLTHSV12", 'HLTHSV22', 'HLTHSV32', 'PRIMREA2', 'REASSPE2'])
    y = df[target_column]

    # Split into train/test (optional, but good practice)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a decision tree classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Get feature importances
    importances = pd.Series(clf.feature_importances_, index=X.columns)
    importances = importances.sort_values(ascending=False)

    # Print top features
    print("Top features by importance:")
    print(importances.head(10))

    # Plot feature importances
    plt.figure(figsize=(10, 6))
    importances.head(10).plot(kind='barh', color='skyblue')
    plt.gca().invert_yaxis()
    plt.title("Top 10 Important Features (Decision Tree)")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()

