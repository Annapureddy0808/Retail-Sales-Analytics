import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# -----------------------------
# MySQL Connection
# -----------------------------
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Annapureddy@123",   # Your MySQL password
    host="localhost",
    port=3307,
    database="retail_sales"
)

engine = create_engine(connection_url)

# -----------------------------
# Read Data
# -----------------------------
print("Reading data from MySQL...")

df = pd.read_sql("SELECT * FROM sales", engine)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nTotal Sales:", df["sales"].sum())
print("Total Profit:", df["profit"].sum())

# -----------------------------
# Chart 1: Top 10 Products
# -----------------------------
print("Creating Top Products Chart...")

top_products = (
    df.groupby("product")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# -----------------------------
# Chart 2: Monthly Sales Trend
# -----------------------------
print("Creating Monthly Sales Trend...")

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,6))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# -----------------------------
# Chart 3: Region-wise Sales
# -----------------------------
print("Creating Region-wise Sales Chart...")

region_sales = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.close()

# -----------------------------
# Chart 4: Category-wise Sales
# -----------------------------
print("Creating Category-wise Sales Chart...")

category_sales = (
    df.groupby("category")["sales"]
    .sum()
)

plt.figure(figsize=(7,7))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# -----------------------------
# Chart 5: Profit by Category
# -----------------------------
print("Creating Profit by Category Chart...")

profit_category = (
    df.groupby("category")["profit"]
    .sum()
)

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_category.png")
plt.close()

# -----------------------------
# Chart 6: Top 10 Customers
# -----------------------------
print("Creating Top Customers Chart...")

top_customers = (
    df.groupby("customer_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
top_customers.plot(kind="bar")
plt.title("Top 10 Customers")
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_customers.png")
plt.close()

# -----------------------------
# Chart 7: Sales vs Profit
# -----------------------------
print("Creating Sales vs Profit Chart...")

plt.figure(figsize=(8,6))
plt.scatter(df["sales"], df["profit"], alpha=0.5)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.close()

# -----------------------------
# Finished
# -----------------------------
print("\n===================================")
print(" All charts generated successfully!")
print("===================================")

print("\nGenerated files:")
print("1. top_products.png")
print("2. monthly_sales_trend.png")
print("3. region_sales.png")
print("4. category_sales.png")
print("5. profit_category.png")
print("6. top_customers.png")
print("7. sales_vs_profit.png")