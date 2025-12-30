# SQL Optimization Tips

Best practices for writing efficient SQL queries.

## Indexing

:::{tip}
Create indexes on columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses.
:::

### Example: Create Index

```sql
-- Create index on frequently filtered column
CREATE INDEX idx_orders_customer_date 
ON orders (customer_id, order_date DESC);

-- Partial index for active records only
CREATE INDEX idx_active_customers 
ON customers (email) 
WHERE status = 'active';
```

## Query Patterns to Avoid

### ❌ SELECT *

```sql
-- Bad: Fetches all columns
SELECT * FROM large_table;

-- Good: Select only needed columns
SELECT id, name, email FROM large_table;
```

### ❌ Functions on Indexed Columns

```sql
-- Bad: Can't use index
SELECT * FROM orders 
WHERE YEAR(order_date) = 2024;

-- Good: Index-friendly
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';
```

## EXPLAIN ANALYZE

Always analyze query performance:

```sql
EXPLAIN ANALYZE
SELECT c.name, SUM(o.amount)
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.order_date > '2024-01-01'
GROUP BY c.name;
```

:::{warning}
Run `EXPLAIN ANALYZE` on staging/dev environments first, not production!
:::
