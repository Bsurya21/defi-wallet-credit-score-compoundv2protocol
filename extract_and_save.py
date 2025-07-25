import json
import pandas as pd

# Step 1: Load the JSON file
with open("data/compound_wallet_data.json", "r") as f:
    raw_data = json.load(f)

# Step 2: Extract all transaction records into a flat list
flattened_data = []

for wallet, tx_list in raw_data.items():
    for tx in tx_list:
        record = {
            "wallet_address": wallet,
            "block_signed_at": tx.get("block_signed_at"),
            "tx_hash": tx.get("tx_hash"),
            "from_address": tx.get("from_address"),
            "to_address": tx.get("to_address"),
            "value_quote": tx.get("value_quote"),
            "pretty_value_quote": tx.get("pretty_value_quote")
        }
        flattened_data.append(record)

# Step 3: Convert to DataFrame
df = pd.DataFrame(flattened_data)

# Step 4: Save to CSV
df.to_csv("data/flattened_transactions.csv", index=False)

print(f"✅ Saved {len(df)} transactions to 'flattened_transactions.csv'")
