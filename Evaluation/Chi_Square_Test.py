import pandas as pd
from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

def print_top_features_per_component(pca, feature_names, top_n=5):
    components = pca.components_
    count = 0
    for i, comp in enumerate(components):
        count += 1
        if count == 6:
            break
        top_indices = np.argsort(np.abs(comp))[-top_n:][::-1]
        top_features = [(feature_names[idx], comp[idx]) for idx in top_indices]
        print(f"\nPrincipal Component {i+1}:")
        for name, val in top_features:
            print(f"  {name}: {val:.4f}") 

def chi_square_feature_importance(df, target_col = "HLTHSER2", save_dir = "data_mining/Evaluation/plots/"):
    results = []
    relevant_features = []

    print("entered function")
    # Split into features (X) and target (y)
    df = df.drop(columns=["HLTHSV12", 'HLTHSV22', 'HLTHSV32', 'PRIMREA2']) #, 'REASSPE2'
    print(f"Total columns including target: {df.shape[1]}")
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
        #if p < 1e-15:
        #    print(f"Effectively zero p-value: {p:.2e}")
        if p < 0.1:  # Filter for p-value < 0.05
            results.append((col, chi2, p))
            relevant_features.append(col)

    print("sorting")
    results.sort(key=lambda x: x[1], reverse=True)  # sort by chi2 score

    sr = pd.DataFrame(results, columns=['Feature', 'Chi2 Score', 'p-value'])
    
    sr.to_csv('output.txt', sep='\t', index=False)

    # Running PCA on relevant features
    scaler = StandardScaler()
    df_only_some_features = df[relevant_features]
    df_scaled = scaler.fit_transform(df_only_some_features)

    # Fit PCA with all components
    pca = PCA(n_components=min(df_scaled.shape[0], df_scaled.shape[1]))
    pca.fit(df_scaled)

    # Explained variance ratio
    evr = pca.explained_variance_ratio_

    # Limit to first 10 components
    max_components_to_plot = min(10, len(evr))
    evr_subset = evr[:max_components_to_plot]

    # Scree plot
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_components_to_plot + 1), evr_subset, 'o-', color='teal')
    plt.title('Scree Plot (First 10 Principal Components)')
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.xticks(range(1, max_components_to_plot + 1))
    plt.grid(True)

    # Save scree plot
    os.makedirs(save_dir, exist_ok=True)
    scree_path = os.path.join(save_dir, "scree_plot_chi_test.png")
    plt.savefig(scree_path)
    plt.close()
    print(f"Scree plot saved to {scree_path}")

    #Print components
    components = pca.components_
    print(components) 
    print_top_features_per_component(pca, df_only_some_features.columns)
    
    return sr

if __name__ == "__main__":
    df = pd.read_csv("data_mining/data/Processed_Data/study1_2_encoded.csv")  # or use df_encoded directly if already in memory
    print("calling function")
    chi2_df = chi_square_feature_importance(df, target_col="HLTHSER2")
    print(chi2_df)

