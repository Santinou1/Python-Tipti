import pandas as pd
import os
from src.utils.decorators import timeit, logit

@timeit
@logit
def load_data(data_path):
    """Load data from a CSV file."""
    df = pd.read_csv(data_path)
    print("Data loaded successfully")
    return df

@timeit
@logit
def clean_data(df):
    """Clean the data."""
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    print("Data cleaned successfully")
    return df

@timeit
@logit
def analyze_data(df):
    """Perform some basic data analysis."""
    print("Basic Data Analysis:")
    print(df.describe())
    print("\nProducts with highest prices:")
    print(df.nlargest(5, 'price'))

@timeit
@logit
def save_clean_data(df, output_path):
    """Save the cleaned data to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Clean data saved to {output_path}")

if __name__ == "__main__":
    data_path = "../../data/raw/products.csv"
    output_path = "../../data/processed/cleaned_products.csv"
    
    df = load_data(data_path)
    df = clean_data(df)
    analyze_data(df)
    os.makedirs("../../data/processed", exist_ok=True)
    save_clean_data(df, output_path)

