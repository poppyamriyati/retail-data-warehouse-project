-- Dimension Customer
CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(10),
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

-- Dimension Product
CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(10),
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(12,2)
);

-- Dimension Date
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    month INT,
    quarter INT,
    year INT
);

-- Fact Sales
CREATE TABLE fact_sales (
    sale_key SERIAL PRIMARY KEY,
    date_key INT,
    customer_key INT,
    product_key INT,
    qty INT,
    sales_amount NUMERIC(12,2),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key),

    FOREIGN KEY (customer_key)
        REFERENCES dim_customer(customer_key),

    FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key)
);
