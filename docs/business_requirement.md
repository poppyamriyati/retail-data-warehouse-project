# Business Requirement Document

## Project Overview

A retail company currently stores customer, product, and sales data in separate CSV files. The management team experiences difficulties in generating consistent sales reports and monitoring business performance due to data quality issues and the absence of a centralized data repository.

This project aims to design and implement a simple Data Warehouse solution to improve data quality, data integration, and reporting capabilities.

---

## Business Problem

The current reporting process faces several challenges:

* Customer data contains duplicate records.
* Some records have missing values.
* Invalid dates exist in transaction data.
* Product and customer references are not always valid.
* Sales data is stored in separate files and requires manual consolidation.

These issues impact reporting accuracy and decision-making.

---

## Business Objectives

The project aims to:

1. Improve data quality through validation and cleansing
2. Integrate customer, product, and sales data
3. Implement a Star Schema Data Warehouse
4. Build an automated ETL process
5. Support business reporting and analysis
6. Demonstrate Data Engineering best practices

---

## Data Sources

| Source File  | Description            |
| ------------ | ---------------------- |
| customer.csv | Customer master data   |
| product.csv  | Product master data    |
| sales.csv    | Sales transaction data |

---

## Expected Outcomes

The project will deliver:

* Data Quality Assessment Report
* Metadata Catalog
* Data Lineage Documentation
* Star Schema Data Warehouse Design
* ETL Pipeline
* Business Intelligence Dashboard

---

## Stakeholders

| Role          | Responsibility                                         |
| ------------- | ------------------------------------------------------ |
| Sales Manager | Reviews sales performance reports                      |
| Data Analyst  | Performs business analysis and reporting               |
| Data Engineer | Builds and maintains data pipelines and data warehouse |

---

## Success Criteria

The project is considered successful if:

* Duplicate customer records are identified and handled.
* Invalid transactions are detected and removed.
* Data is successfully transformed into a Data Warehouse structure.
* Business users can access sales insights through dashboards.
* Data lineage and metadata documentation are available.
