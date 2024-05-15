import pandas as pd
from datetime import datetime

#  Convert a column in DataFrame to datetime format, coercing errors

def process_dates(df, date_column):
    df[date_column] = pd.to_datetime(df[date_column], errors = 'coerce')
    return df 

# Calculate the age in years from a datetime column to the current year

def calculate_age(df, date_column):
    current_year = datetime.now().year 
    df["age"] = current_year - df[date_column].dt.year
    return df 

# Filter a DataFrame based on a query string

def filter_and_select(df, condition, columns):
    filtered_df = df.query(condition)
    return filtered_df[columns]
