import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

# ===================================
# 1. CLEAN NAV HISTORY
# ===================================

nav = pd.read_csv(f"{raw_path}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{processed_path}/02_nav_history_cleaned.csv",
    index=False
)

print("NAV History cleaned successfully")

# ===================================
# 2. CLEAN INVESTOR TRANSACTIONS
# ===================================

tx = pd.read_csv(f"{raw_path}/08_investor_transactions.csv")

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.upper()
)

tx = tx[tx["amount_inr"] > 0]

tx = tx.drop_duplicates()

tx.to_csv(
    f"{processed_path}/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions cleaned successfully")

# ===================================
# 3. CLEAN SCHEME PERFORMANCE
# ===================================

perf = pd.read_csv(f"{raw_path}/07_scheme_performance.csv")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# Expense ratio validation (0.1% to 2.5%)
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

perf = perf.drop_duplicates()

perf.to_csv(
    f"{processed_path}/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance cleaned successfully")