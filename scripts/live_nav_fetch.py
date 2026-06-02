import requests
import pandas as pd
from pathlib import Path

# Scheme codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Output folder
output_folder = Path("../data/raw")

for scheme_name, scheme_code in schemes.items():

    print(f"\nFetching {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        data = response.json()

        df = pd.DataFrame(data['data'])

        file_path = output_folder / f"{scheme_name}.csv"

        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    except Exception as e:
        print(f"Error fetching {scheme_name}: {e}")

print("\nAll NAV files fetched successfully.")