import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Read CSV
df = pd.read_csv("superstore.csv")

# Select required columns
df = df[
    [
        "Order.ID",
        "Order.Date",
        "Customer.Name",
        "Region",
        "City",
        "Category",
        "Sub.Category",
        "Product.Name",
        "Sales",
        "Quantity",
        "Profit",
        "Discount",
    ]
]

# Rename columns to match MySQL table
df.columns = [
    "order_id",
    "order_date",
    "customer_name",
    "region",
    "city",
    "category",
    "sub_category",
    "product",
    "sales",
    "quantity",
    "profit",
    "discount",
]

# Convert date column
df["order_date"] = pd.to_datetime(df["order_date"])

# MySQL connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Annapureddy@123",   # Replace with your actual password
    host="localhost",
    port=3307,
    database="retail_sales",
)

engine = create_engine(connection_url)

# Import data
df.to_sql(
    "sales",
    con=engine,
    if_exists="append",
    index=False,
)

print("✅ Data imported successfully!")