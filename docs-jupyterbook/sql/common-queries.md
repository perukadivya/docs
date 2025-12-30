# Common SQL Queries

A collection of frequently used SQL queries and patterns.

## Data Quality Checks

### Check for Nulls

```sql
-- Find columns with null values
SELECT 
    'customer_id' AS column_name,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS null_count,
    ROUND(100.0 * SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS null_percentage
FROM customers;
```

### Check for Duplicates

```sql
-- Find duplicate records
SELECT 
    customer_id,
    email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id, email
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

## Window Functions

### Running Total

```sql
-- Calculate running total of sales
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;
```

### Rank Within Groups

```sql
-- Rank products by sales within each category
SELECT 
    category,
    product_name,
    sales,
    RANK() OVER (PARTITION BY category ORDER BY sales DESC) AS rank_in_category
FROM product_sales;
```

## Date Operations

### Generate Date Series

```sql
-- Generate a series of dates (PostgreSQL)
SELECT generate_series(
    '2024-01-01'::date,
    '2024-12-31'::date,
    '1 day'::interval
)::date AS date;
```

```{tip}
Use date series to fill gaps in time-series data for accurate reporting.
```
