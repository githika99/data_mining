import pandas as pd
import matplotlib.pyplot as plt
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
    #features_to_be_plotted = ['MOMALIV2', 'MOMCOD2', 'STOPMEN2', 'SYMPTOM2', 'HOTFLA2', 'HEVYPER2', 'SLEEPRO2', 'PSYPROB2', 'OTHRPRO2', 'OTHRPRS2', 'HERMENO2', 'GENMENO2', 'ATTIMEN2',
    #                          'ARTHRMO2', 'HIBPMOM2', 'DIABMOM2', 'STRKMOM2', 'HEARTMO2', 'OHDMOM2', 'HIPMOM2', 'OSTEOMO2', 'SPINEMO2', 'HUMPMOM2', 'COLONMO2', 'DEPRMOM2', 'DADALIV2' , 
    #                          'ARTHRDA2', 'HIBPDAD2', 'DIABDAD2', 'STRKDAD2', 'HEARTDA2', 'OHDDAD2', 'HIPDAD2', 'OSTEODA2', 'SPINEDA2', 'HUMPDAD2', 'COLONDA2', 'DEPRDAD2']

    features_to_be_plotted = ['MOMALIV2', 'STOPMEN2', 'SYMPTOM2', 'HOTFLA2', 'HEVYPER2', 'SLEEPRO2', 'PSYPROB2', 'OTHRPRO2', 'OTHRPRS2', 'HERMENO2', 'GENMENO2', 'ATTIMEN2',
                              'ARTHRMO2', 'HIBPMOM2', 'DIABMOM2', 'STRKMOM2', 'HEARTMO2', 'OHDMOM2', 'HIPMOM2', 'OSTEOMO2', 'SPINEMO2', 'HUMPMOM2', 'COLONMO2', 'DEPRMOM2', 'DADALIV2' , 
                              'ARTHRDA2', 'HIBPDAD2', 'DIABDAD2', 'STRKDAD2', 'HEARTDA2', 'OHDDAD2', 'HIPDAD2', 'OSTEODA2', 'SPINEDA2', 'HUMPDAD2', 'COLONDA2', 'DEPRDAD2']

    for i in features_to_be_plotted:    
        if i not in feature_code_mappings:
            continue
        label_map = feature_code_mappings[i]

        # Count the occurrences of each value (Only count positive values because negative values include Not applicable and I don't know)
        counts = df[i][df[i] >= 0].value_counts().reindex(feature_domains[i], fill_value=0)

        # Extract counts and matching labels
        values = counts.values
        labels = [label_map[val] for val in counts.index]

        # Plot
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f'{i} Chart')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend(loc="lower left")
        plt.savefig(f'./{i}_distribution.png')

# for features we want to find a distribution of 
# ex. contains 'years' as a measurement
def histogram(df, codebook):
    l = encoding(codebook)
    feature_code_mappings = l[0]
    feature_domains = l[1]
    features_to_be_plotted = ['MOMDIED2', 'MOMCOD2', 'MOMAGE2', 'AGESTOP2', 'DADDIED2', 'DADCOD2', 'DADAGE2']

    for i in features_to_be_plotted:    
        label_map = feature_code_mappings[i]

        # Count the occurrences of each value (ignore -8 if desired)
        counts = df[i].value_counts().reindex(feature_domains[i], fill_value=0)

        # Get codes and labels
        codes = counts.index.tolist()
        values = counts.values
        labels = [label_map[code] for code in codes]

        # Plot histogram (as a bar plot)
        plt.bar(codes, values, tick_label=labels)
        plt.title(f'{i} Distribution')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'./{i}_distribution.png')
        plt.clf()  # Clear figure for next plot

if __name__ == "__main__":
    # --- Load your main dataset and codebook ---
    df = pd.read_csv('../data/Raw_Data/30181-0001-Data.tsv', sep='\t', quoting=3, engine='python')
    codebook = pd.read_csv('../data/data_dictionary.csv')

    pie_chart(df, codebook)
    #histogram(df, codebook)
    




