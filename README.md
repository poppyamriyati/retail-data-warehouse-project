# Retail Data Warehouse Project
End-to-End Retail Data Warehouse Project developed to demonstrate Data Engineering competencies including Data Quality Management, Data Integration, Data Warehouse Design, ETL Development, and Business Intelligence Reporting.


## Overview
A retail company stores customer, product, and sales data in separate source files. This project demonstrates how raw operational data can be transformed into a centralized Data Warehouse to support analytics and reporting.

The solution includes data quality assessment, data cleansing, dimensional modeling, ETL development, PostgreSQL implementation, and Power BI dashboard visualization.


## Objectives
- Improve data quality through validation and cleansing
- Integrate customer, product, and sales data
- Implement a Star Schema Data Warehouse
- Build an automated ETL process
- Support business reporting and analysis
- Demonstrate Data Engineering best practices


## Technology Stack

### Programming
- Python

### Libraries
- Pandas
- SQLAlchemy
- psycopg2

### Database
- PostgreSQL

### Analytics & Visualization
- Tableau

### Version Control
- GitHub


## Solution Architecture

Raw CSV Files
→ Data Quality Assessment
→ Data Cleansing
→ ETL Pipeline
→ PostgreSQL Data Warehouse
→ Power BI Dashboard

---

## Data Warehouse Design

### Dimension Tables

* dim_customer
* dim_product
* dim_date

### Fact Table

* fact_sales

The Data Warehouse follows a Star Schema design to support analytical reporting and business intelligence use cases.

---

## Data Quality Management

The following data quality checks were implemented:

* Missing Value Detection
* Duplicate Customer Detection
* Invalid Date Validation
* Referential Integrity Validation
* Negative Quantity Validation

### Referential Integrity Handling

An Unknown Customer record (`customer_key = -1`) was implemented to preserve valid sales transactions when customer master data contains quality issues.

This approach prevents revenue loss while maintaining referential integrity within the Data Warehouse.


## Project Structure

data/
docs/
etl/
sql/
dashboard/
screenshots/


## Project Deliverables

### Documentation

- Business Requirement Document
- Architecture Diagram
- Star Schema Design
- Data Lineage Diagram
- Metadata Catalog
- Data Quality Report
- Competency Mapping

### Data Assets

- customer.csv
- product.csv
- sales.csv
- clean_customer.csv
- clean_product.csv
- clean_sales.csv

### Engineering Assets

- PostgreSQL Data Warehouse
- SQL Data Warehouse Design
- ETL Pipeline (Extract, Transform, Load)
- Data Quality Validation Rules

### Analytics Assets

- Tableau Dashboard
- Dashboard Screenshot


## Dashboard Preview

<img width="825" height="723" alt="retail sales dashboard" src="https://github.com/user-attachments/assets/f8835615-4a82-447f-83a9-3aae5d747cbf" />

Key Metrics:
Total Revenue
Total Orders
Total Quantity Sold
Revenue Trend
Top Products
Revenue by Customer

Full dashboard: https://public.tableau.com/app/profile/poppy.amriyati8631/viz/RetailSalesDashboard_17802826532380/Dashboard1?publish=yes


## Project Purpose

This project was developed to demonstrate practical Data Engineering competencies including:

Data Profiling
Data Quality Assessment
Data Cleansing
Metadata Management
Data Integration
Data Warehouse Development
ETL Development
Data Lineage Documentation
Business Intelligence Reporting


## Repository Structure

```text
retail-data-warehouse-project
│
├── data/
│   ├── customer.csv
│   ├── product.csv
│   └── sales.csv
│
├── docs/
│   ├── architecture.png
│   ├── star_schema.png
│   ├── metadata_catalog.xlsx
│   ├── data_quality_report.md
│   └── competency_mapping.md
│
├── sql/
│   └── create_tables.sql
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dashboard/
│
└── README.md
```


## Competencies Demonstrated
- Data Profiling
- Data Quality Assessment
- Data Cleansing
- Metadata Management
- Master Data Management
- Data Integration
- Data Warehouse Development
- ETL Development
- Data Lineage Documentation
- Business Intelligence Reporting


## Author

Poppy Amriyati

This project was developed as part of a Data Engineering portfolio and certification preparation.
