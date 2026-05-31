import pandas as pd

customer = pd.read_csv("../data/clean_customer.csv")
product = pd.read_csv("../data/clean_product.csv")
sales = pd.read_csv("../data/clean_sales.csv")

print("Loading clean datasets...")

print(f"Customer rows: {len(customer)}")
print(f"Product rows: {len(product)}")
print(f"Sales rows: {len(sales)}")

print("Load completed.")
