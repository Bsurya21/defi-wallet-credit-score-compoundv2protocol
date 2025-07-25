
# 🪙 DeFi Wallet Credit Scoring – Zeru Finance Internship

This project builds a **credit scoring model (0–1000)** for DeFi wallets based on transaction data from the [GoldRush platform](https://goldrush.dev/platform/). The pipeline extracts, processes, analyzes, and visualizes on-chain behavior to assess creditworthiness in decentralized finance (DeFi).

---

## 📁 Project Structure

```
.
├── extract_and_save.py          # Flattens the raw JSON data into CSV
├── wallet_features.py          # Generates wallet-level transaction features
├── assign_credit_score.py      # Assigns credit scores based on features
├── plot_credit_analysis.py     # Visualizes credit score distribution and patterns
├── run.py                      # Runs all scripts in order
├── data/
│   ├── raw_data.json           # Raw compound V2 data (fetched externally)
│   ├── wallet_data.csv         # Flattened transaction data
│   └── wallet_features.csv     # Processed wallet-level features
├── outputs/
│   ├── wallet_credit_scores.csv  # Final output with credit scores
│   └── plots/                    # Generated visual charts
└── requirements.txt            # Required Python packages
```

---

## 🚀 How It Works

### 🔗 Data Source

Data is fetched from [GoldRush DeFi Data Platform](https://goldrush.dev/platform/) using **compound V2 protocol transaction APIs**.

### ⚙️ Pipeline Overview

1. **`extract_and_save.py`**  
   Parses the raw JSON compound v2 data and saves a flattened CSV.

2. **`wallet_features.py`**  
   Groups data by wallet address and generates:
   - Total transactions
   - Total/average value
   - Min/max value
   - First & last transaction timestamps

3. **`assign_credit_score.py`**  
   A basic rule-based scoring model assigns credit scores out of 1000 based on:
   - Transaction activity
   - Consistency
   - Value of operations

4. **`plot_credit_analysis.py`**  
   Generates visual plots:
   - Score distribution
   - Wallet behavioral types (borrow only, repay only, etc.)
   - Inactive vs partially active wallets
5. **`fetchdata.py`**
   - it is used to fetch the data and create the json file
     used in the further process.you should click the goldrush link and
     provide the key 
---

## 🧪 Running the Project

### 1. ✅ Setup Environment

```bash
python -m venv new-env
new-env\Scripts\activate   # On Windows
pip install -r requirements.txt
```

### 2. 🚀 Run the Full Pipeline

```bash
python run.py
```

This will:
- Extract and save flattened data
- Generate wallet features
- Assign credit scores
- Create output charts in `outputs/plots/`

---

## 📊 Sample Output

- ✅ 71 wallets processed
- ✅ Credit scores generated in `outputs/wallet_credit_scores.csv`
- ✅ Charts saved in `outputs/plots/`

---

## 📦 Requirements

Install required libraries with:

```bash
pip install -r requirements.txt
```

Example minimal content:

```txt
pandas
numpy
matplotlib
```

---

## 🧠 Notes

- **Inactive Wallets:** Wallets with no activity were excluded from scoring and visualized separately.
- **Partially Active Wallets:** Wallets with incomplete behavior (e.g., only borrowing or only repaying) were still scored with adjustments.
- **Scoring Approach:** Heuristic (rule-based); future versions can explore ML-based or credit-risk optimization models.

---

## 📮 Credits

This project is part of the **Zeru Finance Internship Challenge** submitted by **Surya Thirumal Reddy**  
GitHub: [Bsurya21](https://github.com/Bsurya21)  

---
