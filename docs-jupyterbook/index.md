# Data Engineering Documentation

Welcome to the Data Engineering team documentation. This site contains all pipeline documentation, SQL references, Python code examples, and team guidelines.

```{admonition} Quick Links
:class: tip

- 📊 [Data Pipelines](pipelines/etl-pipeline.md) - All ETL and data pipeline documentation
- 🔍 [SQL Reference](sql/common-queries.md) - Common SQL queries and patterns
- 🐍 [Python Reference](python/data-processing.md) - Python code examples
- 📋 [Guidelines](guidelines/coding-standards.md) - Team coding standards
```

## What's Inside

::::{grid} 2
:gutter: 3

:::{grid-item-card} 🚀 Data Pipelines
:link: pipelines/etl-pipeline
:link-type: doc

Complete documentation for all 7 project pipelines including architecture diagrams and code examples.
:::

:::{grid-item-card} 📝 SQL Reference
:link: sql/common-queries
:link-type: doc

Common SQL queries, optimization tips, and best practices for our data warehouse.
:::

:::{grid-item-card} 🐍 Python Code
:link: python/data-processing
:link-type: doc

Reusable Python functions, API references, and data processing utilities.
:::

:::{grid-item-card} 📋 Guidelines
:link: guidelines/coding-standards
:link-type: doc

10+ guidelines for setup, coding standards, and deployment procedures.
:::

::::

## Architecture Overview

```{mermaid}
flowchart LR
    A[Source Systems] --> B[Ingestion Layer]
    B --> C[Data Lake]
    C --> D[Transformation]
    D --> E[Data Warehouse]
    E --> F[BI Tools]
    
    style A fill:#e1f5fe
    style E fill:#c8e6c9
    style F fill:#fff3e0
```

## Getting Help

💬 **Have feedback?** Use the annotation tool on the right side of the page to highlight text and leave comments.

📧 **Questions?** Contact the Data Engineering team.
