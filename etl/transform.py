import pandas as pd

# Load data
customer = pd.read_csv("../data/customer.csv")
product = pd.read_csv("../data/product.csv")
sales = pd.read_csv("../data/sales.csv")

print("=== DATA QUALITY CHECK ===")

# Missing values
print("\nMissing Values:")
print(customer.isnull().sum())
print(product.isnull().sum())
print(sales.isnull().sum())

# Duplicate customers
print("\nDuplicate Customers:")
duplicates = customer[
    customer.duplicated(
        subset=["email"],
        keep=False
    )
]
print(duplicates)

# Invalid dates
print("\nInvalid Order Dates:")

sales["order_date"] = pd.to_datetime(
    sales["order_date"],
    errors="coerce"
)

invalid_dates = sales[
    sales["order_date"].isna()
]

print(invalid_dates)

# Negative quantity
print("\nNegative Quantity:")

negative_qty = sales[
    sales["qty"] < 0
]

print(negative_qty)

# Remove duplicate customers
customer = customer.drop_duplicates(
    subset=["email"]
)

# Remove invalid quantity
sales = sales[
    sales["qty"] > 0
]

# Remove invalid dates
sales = sales.dropna(
    subset=["order_date"]
)
