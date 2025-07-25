import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")



# Load CSVs
scores_df = pd.read_csv("outputs/wallet_credit_scores.csv")
features_df = pd.read_csv("data/wallet_features.csv")

# Merge for joint analysis
merged_df = pd.merge(features_df, scores_df, on="wallet_address")

# 1. Credit Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(scores_df["credit_score"], bins=20, kde=True, color='royalblue')
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("outputs/credit_score_distribution.png")
plt.close()

# 2. Credit Score vs Total Value Transacted
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=merged_df,
    x="total_value_quote",
    y="credit_score",
    hue="transaction_count",
    size="transaction_count",
    palette="coolwarm",
    legend=False
)
plt.title("Credit Score vs Total Value Transacted")
plt.xlabel("Total Value Transacted (USD)")
plt.ylabel("Credit Score")
plt.tight_layout()
plt.savefig("outputs/score_vs_total_value.png")
plt.close()

# 3. Credit Score vs Transaction Count
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=merged_df,
    x="transaction_count",
    y="credit_score",
    color="teal"
)
plt.title("Credit Score vs Transaction Count")
plt.xlabel("Transaction Count")
plt.ylabel("Credit Score")
plt.tight_layout()
plt.savefig("outputs/score_vs_txn_count.png")
plt.close()

print("✅ Plots saved in the 'outputs/' folder.")
