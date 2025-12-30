# Coding Standards

Team coding standards for data engineering projects.

## Python Standards

### Style Guide

We follow [PEP 8](https://pep8.org/) with these additions:

- **Line length**: 88 characters (Black default)
- **Imports**: Use `isort` with Black compatibility
- **Type hints**: Required for all public functions

### Tools

```bash
# Install development tools
pip install black isort mypy ruff

# Format code
black src/
isort src/

# Type check
mypy src/

# Lint
ruff check src/
```

### Function Documentation

Use Google-style docstrings:

```python
def process_data(
    input_path: str,
    output_path: str,
    batch_size: int = 1000
) -> int:
    """
    Process data from input to output path.
    
    Args:
        input_path: Source data path
        output_path: Destination path
        batch_size: Number of rows per batch
        
    Returns:
        Number of rows processed
        
    Raises:
        FileNotFoundError: If input path doesn't exist
    """
    pass
```

## SQL Standards

### Naming Conventions

| Object | Convention | Example |
|--------|------------|---------|
| Tables | `snake_case` | `customer_orders` |
| Columns | `snake_case` | `order_date` |
| Primary Keys | `id` or `{table}_id` | `customer_id` |
| Foreign Keys | `{referenced_table}_id` | `customer_id` |

### Formatting

```sql
-- Use uppercase for keywords
-- Align clauses for readability
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
WHERE c.status = 'active'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 0
ORDER BY order_count DESC;
```

:::{tip}
Use [SQLFluff](https://sqlfluff.com/) for automated SQL linting.
:::
