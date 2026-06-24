# Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|-------------|
| amfi_code | Unique scheme code |
| scheme_name | Mutual fund scheme |
| fund_house | AMC name |
| category | Equity/Debt |
| sub_category | Fund subtype |
| risk_category | Risk grade |

## 02_nav_history.csv

| Column | Description |
|----------|-------------|
| amfi_code | Scheme code |
| date | NAV date |
| nav | Net Asset Value |

## 07_scheme_performance.csv

| Column | Description |
|----------|-------------|
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| alpha | Alpha |
| beta | Beta |
| sharpe_ratio | Sharpe ratio |
| expense_ratio_pct | Expense ratio |

## 08_investor_transactions.csv

| Column | Description |
|----------|-------------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| amount_inr | Investment amount |
| transaction_type | SIP/Lumpsum/Redemption |
| state | Investor state |
| kyc_status | KYC verification status |