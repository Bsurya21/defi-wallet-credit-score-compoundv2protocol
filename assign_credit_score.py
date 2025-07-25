import pandas as pd
from datetime import datetime

# Load features
df = pd.read_csv("data/wallet_features.csv")

# Calculate account age in days
df['first_transaction'] = pd.to_datetime(df['first_transaction'])
df['last_transaction'] = pd.to_datetime(df['last_transaction'])
df['account_age_days'] = (df['last_transaction'] - df['first_transaction']).dt.days + 1

# Calculate value consistency
df['value_consistency'] = df['max_value_quote'] - df['min_value_quote']

# Normalize each feature to 0–1 scale using Min-Max
def normalize(series):
    return (series - series.min()) / (series.max() - series.min() + 1e-9)

df['score_txn_count'] = normalize(df['transaction_count']) * 300
df['score_total_value'] = normalize(df['total_value_quote']) * 300
df['score_age'] = normalize(df['account_age_days']) * 200
df['score_avg_value'] = normalize(df['average_value_quote']) * 100
df['score_consistency'] = (1 - normalize(df['value_consistency'])) * 100  # lower diff → better

# Final score: sum of weighted components
df['credit_score'] = df[
    ['score_txn_count', 'score_total_value', 'score_age', 'score_avg_value', 'score_consistency']
].sum(axis=1).round(2)

# Round and clean
df['credit_score'] = df['credit_score'].clip(0, 1000)

# Save to CSV
df[['wallet_address', 'credit_score']].to_csv("outputs/wallet_credit_scores.csv", index=False)

print("✅ Credit scores saved to wallet_credit_scores.csv")
print(df[['wallet_address', 'credit_score']].head(10))
