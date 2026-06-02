import pandas as pd
from pathlib import Path

# Raw data folder path
DATA_PATH = Path("../data/raw")

# List all CSV files
csv_files = list(DATA_PATH.glob("*.csv"))

print("=" * 60)
print("BLUESTOCK MF CAPSTONE - DATA INGESTION")
print("=" * 60)

# Dictionary to store DataFrames
datasets = {}

for file in csv_files:
    try:
        # Read CSV
        df = pd.read_csv(file)

        # Store dataframe
        datasets[file.stem] = df

        print(f"\nDataset: {file.name}")
        print("-" * 40)

        # Shape
        print(f"Shape: {df.shape}")

        # Data types
        print("\nData Types:")
        print(df.dtypes)

        # Missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # First 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error loading {file.name}: {e}")

print("\n")
print("=" * 60)
print("ALL DATASETS LOADED SUCCESSFULLY")
print("=" * 60)