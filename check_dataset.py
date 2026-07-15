import pandas as pd

# Replace with your file name
df = pd.read_csv("superstore.csv", encoding="latin1")

print("Shape:", df.shape)
print()

print("Columns:")
print(df.columns)
print()

print("Missing Values:")
print(df.isnull().sum())
print()

print("Duplicate Rows:", df.duplicated().sum())
print()

print("Data Types:")
print(df.dtypes)
# 1. Shape
print("\n===== SHAPE =====")
print(df.shape)

# 2. Information
print("\n===== INFO =====")
df.info()

# 3. Missing Values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 4. Duplicate Rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# 5. First 5 Rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())