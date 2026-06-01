import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:poppy123@localhost:5432/retail_dw"
)

sales = pd.read_csv("data/clean_sales.csv")

sales["order_date"] = pd.to_datetime(
    sales["order_date"]
)

dim_date = pd.DataFrame()

dim_date["full_date"] = (
    sales["order_date"]
    .drop_duplicates()
)

dim_date["date_key"] = (
    dim_date["full_date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dim_date["month"] = (
    dim_date["full_date"]
    .dt.month
)

dim_date["quarter"] = (
    dim_date["full_date"]
    .dt.quarter
)

dim_date["year"] = (
    dim_date["full_date"]
    .dt.year
)

dim_date = dim_date[
    [
        "date_key",
        "full_date",
        "month",
        "quarter",
        "year"
    ]
]

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

print("dim_date loaded successfully.")