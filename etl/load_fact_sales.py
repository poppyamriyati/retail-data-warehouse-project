import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:poppy123@localhost:5432/retail_dw"
)

# Read sales data
sales = pd.read_csv("data/clean_sales.csv")

# Read dimension tables
dim_customer = pd.read_sql(
    "SELECT customer_key, customer_id FROM dim_customer",
    engine
)

dim_product = pd.read_sql(
    "SELECT product_key, product_id FROM dim_product",
    engine
)

dim_date = pd.read_sql(
    "SELECT date_key, full_date FROM dim_date",
    engine
)

# Convert date format
sales["order_date"] = pd.to_datetime(
    sales["order_date"]
)

dim_date["full_date"] = pd.to_datetime(
    dim_date["full_date"]
)

# Lookup customer_key
sales = sales.merge(
    dim_customer,
    on="customer_id",
    how="left"
)

sales["customer_key"] = (
    sales["customer_key"]
    .fillna(-1)
)

# Lookup product_key
sales = sales.merge(
    dim_product,
    on="product_id",
    how="left"
)

# Lookup date_key
sales = sales.merge(
    dim_date,
    left_on="order_date",
    right_on="full_date",
    how="left"
)

# Build fact table
fact_sales = sales[
    [
        "date_key",
        "customer_key",
        "product_key",
        "qty",
        "sales_amount"
    ]
]

# Load to PostgreSQL
fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False
)

print("fact_sales loaded successfully.")