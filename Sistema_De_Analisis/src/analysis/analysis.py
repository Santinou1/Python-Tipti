import pandas as pd
import os

def load_data(data_path):
    """Load data from a CSV or Excel file."""
    if data_path.endswith('.csv'):
        df = pd.read_csv(data_path)
    elif data_path.endswith('.xlsx'):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported file format")
    print("Data loaded successfully")
    return df

def clean_data(df):
    """Clean the data."""
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    print("Data cleaned successfully")
    return df

def analyze_data(df):
    """Perform some basic data analysis."""
    print("Basic Data Analysis:")
    print(df.describe())
    print("\nProducts with highest prices:")
    print(df.nlargest(5, 'price'))

def save_clean_data(df, output_path):
    """Save the cleaned data to a CSV or Excel file."""
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False)
    elif output_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported file format")
    print(f"Clean data saved to {output_path}")

if __name__ == "__main__":
    data_path = "../../data/raw/products.csv"
    output_path = "../../data/processed/cleaned_products.csv"
    
    df = load_data(data_path)
    df = clean_data(df)
    analyze_data(df)
    os.makedirs("../../data/processed", exist_ok=True)
    save_clean_data(df, output_path)
