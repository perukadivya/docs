# ETL Pipeline - Sales Data

## Overview

This pipeline extracts sales data from source systems, transforms it, and loads into the data warehouse.

:::{admonition} Pipeline Status
:class: note

**Schedule**: Daily at 2:00 AM UTC  
**Owner**: Data Engineering Team  
**SLA**: 4 hours
:::

## Architecture

```{mermaid}
flowchart TD
    subgraph Sources
        A[PostgreSQL] 
        B[REST API]
        C[S3 Files]
    end
    
    subgraph Processing
        D[Apache Airflow]
        E[Spark Jobs]
    end
    
    subgraph Storage
        F[Data Lake]
        G[Snowflake DW]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> G
    
    style D fill:#ffecb3
    style G fill:#c8e6c9
```

## Configuration

```python
# pipeline_config.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PipelineConfig:
    """Configuration for the Sales ETL Pipeline."""
    
    source_database: str = "postgres://sales_db"
    target_schema: str = "warehouse.sales"
    batch_size: int = 10000
    retry_attempts: int = 3
    
    def get_partition_date(self) -> str:
        """Get the partition date for the current run."""
        return datetime.now().strftime("%Y-%m-%d")
```

## Key SQL Transformations

### Sales Aggregation

```sql
-- Aggregate daily sales by region
WITH daily_sales AS (
    SELECT 
        DATE_TRUNC('day', order_date) AS sale_date,
        region_id,
        SUM(amount) AS total_sales,
        COUNT(DISTINCT customer_id) AS unique_customers
    FROM raw.orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY 1, 2
)
SELECT 
    sale_date,
    r.region_name,
    total_sales,
    unique_customers,
    total_sales / NULLIF(unique_customers, 0) AS avg_order_value
FROM daily_sales ds
JOIN dim.regions r ON ds.region_id = r.region_id
ORDER BY sale_date DESC, total_sales DESC;
```

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Runtime | > 4 hours | PagerDuty |
| Row Count | < 1000 | Slack |
| Error Rate | > 1% | Email |

:::{warning}
If the pipeline fails, check the Airflow logs first before escalating.
:::
