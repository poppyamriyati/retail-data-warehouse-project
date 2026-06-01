import pandas as pd
from sqlalchemy import create_engine

# Read clean datasets
customer = pd.read_csv("data/clean_customer.csv")
product = pd.read_csv("data/clean_product.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:poppy123@localhost:5432/retail_dw"
)

print("Loading dim_customer...")

customer.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

print("Loading dim_product...")

product.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

print("Load completed successfully.")