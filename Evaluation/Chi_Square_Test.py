import pandas as pd
from scipy.stats import chi2_contingency

def chi_square_feature_importance(df, target_col = "HLTHSER2"):
    results = []

    print("entered function")
    # Split into features (X) and target (y)
    df = df.drop(columns=["HLTHSV12", 'HLTHSV22', 'HLTHSV32', 'PRIMREA2']) #, 'REASSPE2'
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.precision', 20)
    print("made df")
    for col in df.columns:
        if col == target_col:
            continue
        contingency_table = pd.crosstab(df[col], df[target_col])
        if contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
            continue  # skip degenerate cases
        chi2, p, dof, ex = chi2_contingency(contingency_table)
        if p < 1e-15:
            print(f"Effectively zero p-value: {p:.2e}")
        results.append((col, chi2, p))

    print("sorting")
    results.sort(key=lambda x: x[1], reverse=True)  # sort by chi2 score
    # Filter for p-value < 0.05
    significant_results = [r for r in results if r[2] < 0.01]

    sr = pd.DataFrame(significant_results, columns=['Feature', 'Chi2 Score', 'p-value'])
    
    sr.to_csv('output.txt', sep='\t', index=False)

    print("returning")
    return sr

if __name__ == "__main__":
    df = pd.read_csv("/Users/githika/GitHub/data_mining/Evaluation/study2_encoded.csv")  # or use df_encoded directly if already in memory
    print("calling function")
    chi2_df = chi_square_feature_importance(df, target_col="HLTHSER2")
    print(chi2_df)

