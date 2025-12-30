# Data Ingestion Pipeline

## Overview

Generic data ingestion framework for loading data from various sources into the data lake.

## Supported Sources

| Source Type | Connector | Status |
|-------------|-----------|--------|
| PostgreSQL | `psycopg2` | ✅ Active |
| MySQL | `mysql-connector` | ✅ Active |
| REST API | `requests` | ✅ Active |
| S3 | `boto3` | ✅ Active |
| SFTP | `paramiko` | 🔄 Beta |

## Usage Example

```python
from ingestion import DataIngester

# Initialize the ingester
ingester = DataIngester(
    source_type="postgresql",
    connection_string="postgresql://user:pass@host:5432/db"
)

# Define extraction query
query = """
    SELECT * 
    FROM customers 
    WHERE updated_at > %(last_run)s
"""

# Run incremental ingestion
result = ingester.extract(
    query=query,
    params={"last_run": "2024-01-01"},
    target_path="s3://data-lake/raw/customers/"
)

print(f"Ingested {result.row_count} rows")
```

## Data Flow

```{mermaid}
sequenceDiagram
    participant S as Source
    participant I as Ingester
    participant L as Data Lake
    participant C as Catalog
    
    I->>S: Connect & Extract
    S-->>I: Return Data
    I->>I: Validate Schema
    I->>L: Write Parquet
    I->>C: Update Metadata
    C-->>I: Confirm
```
