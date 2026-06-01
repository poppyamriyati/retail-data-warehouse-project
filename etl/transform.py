import pandas as pd

# Load data
customer = pd.read_csv("data/customer.csv")
product = pd.read_csv("data/product.csv")
sales = pd.read_csv("data/sales.csv")

print("=== DATA QUALITY CHECK ===")

# ====================================
# Missing Values
# ====================================

print("\nMissing Values:")

print("\nCustomer:")
print(customer.isnull().sum())

print("\nProduct:")
print(product.isnull().sum())

print("\nSales:")
print(sales.isnull().sum())

# ====================================
# Duplicate Customers
# ====================================

print("\nDuplicate Customers:")

duplicates = customer[
    customer.duplicated(
        subset=["email"],
        keep=False
    )
]

print(duplicates)

# ====================================
# Referential Integrity Check
# ====================================

print("\nInvalid Product References:")

invalid_product = sales[
    ~sales["product_id"].isin(
        product["product_id"]
    )
]

print(invalid_product)

print("\nInvalid Customer References:")

invalid_customer = sales[
    ~sales["customer_id"].isin(
        customer["customer_id"]
    )
]

print(invalid_customer)

# ====================================
# Invalid Dates
# ====================================

print("\nInvalid Order Dates:")

sales["order_date"] = pd.to_datetime(
    sales["order_date"],
    errors="coerce"
)

invalid_dates = sales[
    sales["order_date"].isna()
]

print(invalid_dates)

# ====================================
# Negative Quantity
# ====================================

print("\nNegative Quantity:")

negative_qty = sales[
    sales["qty"] < 0
]

print(negative_qty)

# ====================================
# DATA CLEANING
# ====================================

# Remove duplicate customers
customer = customer.drop_duplicates(
    subset=["email"]
)

# Remove invalid product references
sales = sales[
    sales["product_id"].isin(
        product["product_id"]
    )
]

# Remove invalid customer references
sales = sales[
    sales["customer_id"].isin(
        customer["customer_id"]
    )
]

# Remove negative quantity
sales = sales[
    sales["qty"] > 0
]

# Remove invalid dates
sales = sales.dropna(
    subset=["order_date"]
)

# Validate customer join_date

customer["join_date"] = pd.to_datetime(
    customer["join_date"],
    errors="coerce"
)

# Remove invalid join_date

customer = customer.dropna(
    subset=["join_date"]
)

# ====================================
# SAVE CLEAN DATASETS
# ====================================

customer.to_csv(
    "data/clean_customer.csv",
    index=False
)

product.to_csv(
    "data/clean_product.csv",
    index=False
)

sales.to_csv(
    "data/clean_sales.csv",
    index=False
)

print("\nClean datasets created successfully.")

print("\n=== CLEAN DATA SUMMARY ===")
print(f"Customer rows: {len(customer)}")
print(f"Product rows: {len(product)}")
print(f"Sales rows: {len(sales)}")
