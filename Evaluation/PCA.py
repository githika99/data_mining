import pandas as pd
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

def run_pca_and_save_with_scree(df_encoded, save_dir="data_mining/Evaluation/plots/"):
    # Standardize data
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_encoded)

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
    scree_path = os.path.join(save_dir, "scree_plot.png")
    plt.savefig(scree_path)
    plt.close()
    print(f"Scree plot saved to {scree_path}")

    #Print components
    components = pca.components_
    print(components) 
    return pca 
    # Also print cumulative variance for reference
    #cum_var = evr.cumsum()
    #for i, (var, cum) in enumerate(zip(evr, cum_var), 1):
        #print(f"PC{i}: {var:.4f} variance, Cumulative: {cum:.4f}")

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
    

if __name__ == "__main__":
    # Assuming df and value_to_int are loaded & processed as before
    df_encoded = pd.read_csv("data_mining/data/Processed_Data/study1_2_encoded.csv")  # or use df_encoded directly if already in memory

    pca = run_pca_and_save_with_scree(df_encoded) 

    print_top_features_per_component(pca, df_encoded.columns) 

