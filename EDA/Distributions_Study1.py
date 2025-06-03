import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

def encoding(codebook):
    feature_code_mappings = {}
    feature_domains = {}

    for col in codebook:
        if 'Features-that-use' in col:
            feature_group = col.split('-')[3]

            # Get the relevant columns as lists (drop NaNs)
            lst = codebook[col].dropna().tolist()
            domain_col = codebook[f'{feature_group}-domain'].dropna().tolist()
            code_col = codebook[f'{feature_group}-code'].dropna().tolist()
            for i in lst:
                feature_code_mappings[i] = dict(zip(domain_col, code_col))
                feature_domains[i] = domain_col
    
    return [feature_code_mappings, feature_domains]

# for features that we want to count, not find distribution of 
def pie_chart(df, codebook):
    l = encoding(codebook)
    feature_code_mappings = l[0]
    feature_domains = l[1]
    print(feature_code_mappings, "/n/n")
    features_to_be_plotted = ['MOMALIV2', 'STOPMEN2', 'SYMPTOM2', 'HOTFLA2', 'HEVYPER2', 'SLEEPRO2', 'PSYPROB2', 'OTHRPRO2', 'OTHRPRS2', 'HERMENO2', 'GENMENO2', 'ATTIMEN2',
                              'ARTHRMO2', 'HIBPMOM2', 'DIABMOM2', 'STRKMOM2', 'HEARTMO2', 'OHDMOM2', 'HIPMOM2', 'OSTEOMO2', 'SPINEMO2', 'HUMPMOM2', 'COLONMO2', 'DEPRMOM2', 'DADALIV2' , 
                              'ARTHRDA2', 'HIBPDAD2', 'DIABDAD2', 'STRKDAD2', 'HEARTDA2', 'OHDDAD2', 'HIPDAD2', 'OSTEODA2', 'SPINEDA2', 'HUMPDAD2', 'COLONDA2', 'DEPRDAD2']


    colors = ['#ec4899', '#fbcfe8', '#d1d5db', '#6b7280', '#000000']
    for i in features_to_be_plotted:    
        if i not in feature_code_mappings:
            continue
        label_map = feature_code_mappings[i]

        # Count the occurrences of each value (Only count positive values because negative values include Not applicable and I don't know)
        counts = pd.to_numeric(df[i], errors='coerce')[lambda x: x >= 0].value_counts().reindex(feature_domains[i], fill_value=0)

        counts_for_pie = counts[counts.index > 0]
        
        values_for_pie = counts_for_pie.values 

        labels = [f"{label_map[val]} ({counts[val]})" for val in counts_for_pie.index]


        # Plot
        plt.pie(values_for_pie, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title(f'{i} Chart')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        legend_labels = [f"{label_map[val]}: {counts[val]}" for val in counts.index]
        patches = [mpatches.Patch(color=colors[j], label=legend_labels[j]) for j in range(len(legend_labels))]
        plt.legend(handles=patches, loc='lower left')
        plt.savefig(f'./pie_charts/{i}_distribution.png')
        plt.clf()  # Clear figure for next plot

# for features we want to find a distribution of 
# ex. contains 'years' as a measurement
# only feature that we need to look at codebook for is AGESTOP2
# the rest of the features are text or years
def histogram(df, codebook):
    #l = encoding(codebook)
    #feature_code_mappings = l[0]
    #feature_domains = l[1]
    # features_to_be_plotted = ['MOMDIED2', 'MOMCOD2', 'MOMAGE2', 'AGESTOP2', 'DADDIED2', 'DADCOD2', 'DADAGE2']
    features_to_be_plotted = ['MOMDIED2', 'MOMCOD2', 'MOMAGE2', 'DADDIED2', 'DADCOD2', 'DADAGE2']

    # MOMCOD2 and DADCOD2 are text
    # everything else is years

    for i in features_to_be_plotted:   
        if i == "MOMCOD2" or i == "DADCOD2": # textual data
            counts = df[i].dropna()
            counts = counts.str.strip().str.lower()
            counts = counts[(counts != "") & (counts != "-8")]
            counts = counts.value_counts()
            counts = counts[counts > 3]

            print(counts)
            # Get codes and labels
            codes = counts.index.tolist()
            values = counts.values

            # Plot histogram (as a bar plot)
            plt.figure(figsize=(12, 6))
            plt.bar(codes, values, color='#ec4899')
            plt.title(f'{i} Distribution\nOnly causes of death with more than 3 counts are plotted.')
            plt.ylabel('Count')
            plt.xlabel('Cause of Death') 
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'./bar_charts/{i}_distribution.png')
            plt.clf()  # Clear figure for next plot
        
        else: 
            counts = pd.to_numeric(df[i], errors='coerce')
            counts = counts[counts >= 0].value_counts().sort_index()

            # Get codes and labels
            codes = counts.index.tolist()
            values = counts.values

            # Plot histogram (as a bar plot)
            plt.bar(codes, values, color='#ec4899')
            plt.title(f'{i} Distribution')
            plt.ylabel('Count')
            plt.xlabel('Years')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'./bar_charts/{i}_distribution.png')
            plt.clf()  # Clear figure for next plot

if __name__ == "__main__":
    # --- Load your main dataset and codebook ---
    df = pd.read_csv('../data/Raw_Data/SWAN1.tsv', sep='\t', quoting=3, engine='python')
    df2 = pd.read_csv('../data/Raw_Data/SWAN2.tsv', sep='\t', quoting=3, engine='python')
    codebook = pd.read_csv('../data/data_dictionary.csv')

    results = []
    # print data dictionary for df2
    for col in df.columns:
        results.append((col, " "))
    
    sr = pd.DataFrame(results, columns=['Feature', 'Meaning'])
    sr.to_csv("/Users/githika/GitHub/data_mining/data/SWAN_1_Names.csv", sep='\t', index=False)

    results = []
    # print data dictionary for df2
    for col in df2.columns:
        results.append((col, " "))
    
    sr = pd.DataFrame(results, columns=['Feature', 'Meaning'])
    sr.to_csv("/Users/githika/GitHub/data_mining/data/SWAN_2_Names.csv", sep='\t', index=False)

    #pie_chart(df, codebook)
    #histogram(df, codebook)

    # count how many overlapping datapoints there are for SWAN1 and SWAN2
    count1 = df["SWANID"]
    count2 = df2["SWANID"]

    # count number of times a value in count1 matches a value in count2
    print("SWAN1 len", len(count1))
    print("SWAN2 len", len(count2))

    common = set(count1) & set(count2)
    print("common", len(common))




