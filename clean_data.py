"""
Cleans the raw Superstore CSV (sourced from a public GitHub mirror of the
classic 'Sample Superstore' dataset). The raw file has two extra tables
(a Person->Region lookup and a Returns list) accidentally appended below
the real order data -- this script strips those out and produces a clean file.
"""
import pandas as pd

RAW_PATH = "real_superstore.csv"
CLEAN_PATH = "superstore_clean.csv"

df = pd.read_csv(RAW_PATH, encoding="latin1")

# Row ID should always be a clean integer for real order rows.
# Junk appended tables break this (non-numeric or NaN), so this filters them out.
df = df[pd.to_numeric(df["Row ID"], errors="coerce").notnull()].copy()
df["Row ID"] = df["Row ID"].astype(int)

# Drop rows still missing core fields after the junk removal
df = df.dropna(subset=["Order Date", "Sales", "Profit"])

# Parse dates properly
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# Type cleanup
df["Quantity"] = df["Quantity"].astype(int)
df["Postal Code"] = df["Postal Code"].fillna(0).astype(int)

df = df.sort_values("Order Date").reset_index(drop=True)

df.to_csv(CLEAN_PATH, index=False)

print(f"Raw rows: {sum(1 for _ in open(RAW_PATH)) - 1}")
print(f"Clean rows: {len(df)}")
print(f"Date range: {df['Order Date'].min().date()} to {df['Order Date'].max().date()}")
print(f"Total sales: ${df['Sales'].sum():,.0f}")
print(f"Total profit: ${df['Profit'].sum():,.0f}")
print(f"Columns: {list(df.columns)}")
