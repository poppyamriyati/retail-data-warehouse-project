# Data Quality Report

## Overview

This report evaluates data quality issues found in the retail datasets.

---

## Customer Dataset

### Issues Identified

| Issue | Description |
|---------|---------|
| Missing Customer Name | Customer C008 has missing customer_name |
| Missing Email | Customer C009 has missing email |
| Duplicate Customer | C006 and C007 appear to represent the same customer |
| Invalid Date | C010 has invalid join_date (2024-13-01) |

---

## Product Dataset

### Issues Identified

| Issue | Description |
|---------|---------|
| Missing Product Name | Product P010 has missing product_name |

---

## Sales Dataset

### Issues Identified

| Issue | Description |
|---------|---------|
| Invalid Date | Order O011 contains invalid date (2025-02-30) |
| Missing Date | Order O014 has missing order_date |
| Invalid Product Reference | Product P999 does not exist in product master |
| Invalid Customer Reference | Customer C999 does not exist in customer master |
| Negative Quantity | Order O015 contains negative quantity |

---

## Data Quality Rules

| Rule | Status |
|---------|---------|
| customer_name cannot be null | Failed |
| email cannot be null | Failed |
| order_date must be valid | Failed |
| qty must be greater than zero | Failed |
| customer_id must exist in customer master | Failed |
| product_id must exist in product master | Failed |

---

## Data Cleansing Actions

| Issue                             | Action Taken                                                      |
| --------------------------------- | ----------------------------------------------------------------- |
| Duplicate Customer (C006, C007)   | Duplicate record removed based on email address                   |
| Invalid Customer Join Date (C010) | Customer record excluded from customer dimension during cleansing |
| Invalid Order Date (O011)         | Transaction removed from clean sales dataset                      |
| Missing Order Date (O014)         | Transaction removed from clean sales dataset                      |
| Invalid Product Reference (P999)  | Transaction excluded from clean sales dataset                     |
| Invalid Customer Reference (C999) | Transaction excluded from clean sales dataset                     |
| Negative Quantity (O015)          | Transaction excluded from clean sales dataset                     |

### Referential Integrity Handling

The customer master record C010 contained an invalid join_date value (2024-13-01) and could not be loaded into the customer dimension.

To preserve transactional history and revenue accuracy, an Unknown Customer record (customer_key = -1) was implemented in the customer dimension.

Transactions referencing unavailable customer master data are mapped to the Unknown Customer surrogate key during the fact table loading process.

This approach maintains referential integrity while preventing loss of valid sales transactions.


---

## Recommendations

1. Remove duplicate customer records.
2. Validate dates before loading data.
3. Implement referential integrity checks.
4. Apply mandatory field validation.
5. Reject transactions with negative quantity values.
