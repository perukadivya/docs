Data Engineering Docs
=====================

Welcome to the Data Engineering team documentation.

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🚀 Data Pipelines
      :link: pipelines/etl-pipeline
      :link-type: doc

      Complete documentation for all project pipelines.

   .. grid-item-card:: 📝 SQL Reference
      :link: sql/common-queries
      :link-type: doc

      Common SQL queries and optimization tips.

   .. grid-item-card:: 🐍 Python Code
      :link: python/data-processing
      :link-type: doc

      Reusable Python functions and utilities.

   .. grid-item-card:: 📋 Guidelines
      :link: guidelines/coding-standards
      :link-type: doc

      Team coding standards and deployment guides.


Architecture Overview
---------------------

.. mermaid::

   flowchart LR
       A[Source Systems] --> B[Ingestion Layer]
       B --> C[Data Lake]
       C --> D[Transformation]
       D --> E[Data Warehouse]
       E --> F[BI Tools]
       
       style A fill:#e1f5fe
       style E fill:#c8e6c9
       style F fill:#fff3e0


Quick Start
-----------

.. code-block:: bash

   # Clone and setup
   git clone https://github.com/your-org/data-engineering-docs.git
   cd data-engineering-docs
   pip install -r requirements.txt
   
   # Build docs
   make html


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting-started/overview
   getting-started/setup

.. toctree::
   :maxdepth: 2
   :caption: Data Pipelines
   :hidden:

   pipelines/etl-pipeline
   pipelines/data-ingestion

.. toctree::
   :maxdepth: 2
   :caption: SQL Reference
   :hidden:

   sql/common-queries
   sql/optimization-tips

.. toctree::
   :maxdepth: 2
   :caption: Python Reference
   :hidden:

   python/data-processing
   python/api-reference

.. toctree::
   :maxdepth: 2
   :caption: Guidelines
   :hidden:

   guidelines/coding-standards
   guidelines/deployment
