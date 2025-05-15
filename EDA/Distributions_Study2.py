import pandas as pd
import os
import json
import matplotlib.pyplot as plt

def plot_and_save_all_distributions(df_encoded, value_to_int, save_dir="/Users/githika/GitHub/data_mining/EDA/Study2/", max_unique=50):
    colors = ['#ec4899', '#fbcfe8', '#d1d5db', '#6b7280', '#000000']
    int_to_value = {v: k for k, v in value_to_int.items()}
    os.makedirs(save_dir, exist_ok=True)

    for col_name in df_encoded.columns:
        counts = df_encoded[col_name].value_counts(normalize=True).sort_index()
        
        if len(counts) > max_unique:
            print(f"Skipping '{col_name}' (too many unique values: {len(counts)})")
            continue

        labels = [str(int_to_value.get(val, val)) for val in counts.index]
        plt.figure(figsize=(10, 5) if len(counts) >= 6 else (6, 6))

        # Choose a repeating color cycle
        chosen_colors = colors[:len(counts)] if len(counts) <= len(colors) else [colors[i % len(colors)] for i in range(len(counts))]

        if len(counts) >= 6:
            plt.bar(range(len(counts)), counts.values, color=chosen_colors)
            plt.xticks(ticks=range(len(counts)), labels=labels, rotation=45, ha='right')
            plt.ylabel("Proportion")
            plt.title(f"Distribution of values in column {col_name}")
            plt.tight_layout()
        else:
            plt.pie(counts.values, labels=labels, colors=chosen_colors, autopct='%1.1f%%', startangle=90)
            plt.title(f"Distribution of values in column {col_name}")
            plt.axis('equal')

        filename = f"{col_name}.png".replace("/", "_")
        plt.savefig(os.path.join(save_dir, filename))
        plt.close('all')





def process_data(df):
    # Step 1: Keep header and data separate
    header = df.iloc[0]       # first row is header
    data = df.iloc[1:].copy() # everything else is data
    data.reset_index(drop=True, inplace=True)

    # Step 2: Get all unique values in the data
    all_unique_values = pd.unique(data.values.ravel())

    # Step 3: Create a consistent global mapping
    value_to_int = {val: idx for idx, val in enumerate(all_unique_values)}

    # Step 4: Encode the data
    df_encoded = data.applymap(lambda x: value_to_int[x])

    # (Optional) restore header column names (will be integers otherwise)
    df_encoded.columns = header

    # Save mapping to a JSON file
    with open("value_to_int.json", "w") as f:
        json.dump(value_to_int, f, indent=2)

    df_encoded.to_csv('/Users/githika/GitHub/data_mining/Evaluation/study2_encoded.csv', index=False)

    return df_encoded, value_to_int





if __name__ == "__main__":
    # Load TSV file (including header as first row)
    df = pd.read_csv('../data/Raw_Data/SWAN2.tsv', sep='\t', dtype=str, header=None)
    df, value_to_int = process_data(df) 
    plot_and_save_all_distributions(df, value_to_int)




# FIX THIS 
