# Data Processing Utilities

Reusable Python functions for data processing tasks.

## DataFrame Operations

### Load and Clean Data

```python
import pandas as pd
from typing import List, Optional

def load_and_clean(
    filepath: str,
    date_columns: Optional[List[str]] = None,
    drop_duplicates: bool = True
) -> pd.DataFrame:
    """
    Load CSV and perform standard cleaning operations.
    
    Args:
        filepath: Path to the CSV file
        date_columns: Columns to parse as dates
        drop_duplicates: Whether to remove duplicate rows
        
    Returns:
        Cleaned DataFrame
    """
    df = pd.read_csv(
        filepath,
        parse_dates=date_columns or []
    )
    
    # Strip whitespace from string columns
    str_columns = df.select_dtypes(include=['object']).columns
    df[str_columns] = df[str_columns].apply(lambda x: x.str.strip())
    
    if drop_duplicates:
        df = df.drop_duplicates()
    
    return df
```

### Validate Schema

```python
def validate_schema(
    df: pd.DataFrame,
    expected_columns: List[str],
    raise_on_error: bool = True
) -> bool:
    """
    Validate that DataFrame has expected columns.
    
    Args:
        df: DataFrame to validate
        expected_columns: List of required column names
        raise_on_error: Raise exception if validation fails
        
    Returns:
        True if valid, False otherwise
    """
    missing = set(expected_columns) - set(df.columns)
    
    if missing:
        if raise_on_error:
            raise ValueError(f"Missing columns: {missing}")
        return False
    
    return True
```

## Database Utilities

### Connection Manager

```python
from contextlib import contextmanager
import sqlalchemy as sa

@contextmanager
def get_connection(connection_string: str):
    """
    Context manager for database connections.
    
    Usage:
        with get_connection("postgresql://...") as conn:
            df = pd.read_sql(query, conn)
    """
    engine = sa.create_engine(connection_string)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()
        engine.dispose()
```

```{note}
Always use context managers for database connections to ensure proper cleanup.
```
