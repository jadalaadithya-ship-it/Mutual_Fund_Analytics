import pandas as pd
from sqlalchemy import create_engine

# Create SQLite Database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Save into SQLite tables
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("SQLite database created successfully")