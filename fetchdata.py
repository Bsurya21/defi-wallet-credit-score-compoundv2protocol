import requests
import json
import time
import pandas as pd

import os
print("📁 Current working directory:", os.getcwd())


API_KEY = ""  # Replace with your real key
CHAIN_ID = 137  # Polygon

# Load wallet addresses from Excel
df = pd.read_excel("data/wallet_id.csv.xlsx")  # Make sure the file is in the same folder
wallet_addresses = df["wallet_id"].dropna().unique().tolist()

all_wallet_data = {}

for wallet in wallet_addresses:
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet}/transactions_v2/?key={API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_wallet_data[wallet] = data.get("data", {}).get("items", [])
            print(f"✅ Data fetched for wallet: {wallet}")
        else:
            print(f"❌ Error fetching data for {wallet} - {response.status_code}")
            all_wallet_data[wallet] = []
    except Exception as e:
        print(f"⚠️ Exception for {wallet}: {e}")
        all_wallet_data[wallet] = []

    time.sleep(1)  # Avoid rate limits

# Save result
with open("data/compound_wallet_data.json", "w") as f:
    json.dump(all_wallet_data, f, indent=2)

print("\n✅ All wallet data saved to 'compound_wallet_data.json'")
