import pandas as pd

# Load data from a CSV file into a DataFrame

def load_data(file_path):
    return pd.read_csv(file_path)
    
# Rename columns of a DataFrame based on a dictionary mapping
   
def rename_columns(df, rename_dict):
    df.rename(columns=rename_dict, inplace = True)
    return df