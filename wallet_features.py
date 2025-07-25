import pandas as pd

# Load the flattened CSV file
df = pd.read_csv("data/flattened_transactions.csv")

# Convert date to datetime format
df['block_signed_at'] = pd.to_datetime(df['block_signed_at'])

# Replace any missing/invalid values with 0
df['value_quote'] = pd.to_numeric(df['value_quote'], errors='coerce').fillna(0)

# Group by wallet and aggregate
wallet_features = df.groupby('wallet_address').agg(
    transaction_count=('tx_hash', 'count'),
    total_value_quote=('value_quote', 'sum'),
    average_value_quote=('value_quote', 'mean'),
    min_value_quote=('value_quote', 'min'),
    max_value_quote=('value_quote', 'max'),
    first_transaction=('block_signed_at', 'min'),
    last_transaction=('block_signed_at', 'max'),
).reset_index()

# Save to CSV
wallet_features.to_csv("data/wallet_features.csv", index=False)

print("✅ wallet_features.csv created successfully with the following columns:")
print(wallet_features.columns.tolist())
print("📊 Total wallets processed:", len(wallet_features))
