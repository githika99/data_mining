import pandas as pd
import os
import json
import matplotlib.pyplot as plt

def plot_and_save_all_distributions(df_encoded, value_to_int, save_dir="data_mining/EDA/Study2/", max_unique=50):
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


def process_data(df1, df2, name):
    # Step 1: Extract headers and data separately for both
    header1 = df1.iloc[0]
    data1 = df1.iloc[1:].copy()
    data1.columns = header1
    data1.reset_index(drop=True, inplace=True)

    header2 = df2.iloc[0]
    data2 = df2.iloc[1:].copy()
    data2.columns = header2
    data2.reset_index(drop=True, inplace=True)

    # Step 2: Perform SQL-style inner join on 'SWANID'
    merged_df = pd.merge(data1, data2, on='SWANID', how='inner')

    merged_df.to_csv('data_mining/data/Processed_Data/SWAN1_2.tsv', sep='\t', index=False)
    # Step 3: Get all unique values in the merged data
    all_unique_values = pd.unique(merged_df.values.ravel())

    # Step 4: Create global mapping
    value_to_int = {val: idx for idx, val in enumerate(all_unique_values)}

    # Step 5: Encode merged data
    df_encoded = merged_df.applymap(lambda x: value_to_int[x])

    # Save mapping to JSON
    with open("value_to_int.json", "w") as f:
        json.dump(value_to_int, f, indent=2)

    # Save encoded DataFrame
    df_encoded.to_csv('data_mining/data/Processed_Data/' + name, index=False)

    return df_encoded, value_to_int




if __name__ == "__main__":
    # Load TSV file (including header as first row)
    df1 = pd.read_csv('data_mining//data/Raw_Data/SWAN1.tsv', sep='\t', dtype=str, header=None, on_bad_lines='skip')
    df2 = pd.read_csv('data_mining/data/Raw_Data/SWAN2.tsv', sep='\t', dtype=str, header=None)

    df1, value_to_int1 = process_data(df1, df2, 'study1_2_encoded.csv') 

    """
    df = pd.read_csv('data_mining/data/Raw_Data/SWAN2.tsv', sep='\t', dtype=str, header=None)
    df, value_to_int = process_data(df, 'study2_encoded.csv') 
    plot_and_save_all_distributions(df, value_to_int)
    """


