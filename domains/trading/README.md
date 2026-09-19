# Trading Domain

The Trading domain owns datasets related to trade execution.

This domain is intentionally modeled after enterprise-scale trading organizations where domain teams own their own data products.

## Business Responsibilities

- Trade execution
- Instrument reference
- Trade lifecycle
- Execution timestamps
- Pricing

## Trading Data Product

This repository now implements a complete Lakehouse pattern.

### Bronze

- Raw trade ingestion

### Silver

- Duplicate removal
- Lifecycle filtering
- Standardized commodity names
- Trade value calculation

### Gold

- Commodity-level aggregated analytics
- Business-ready reporting

## Future Pipeline

Bronze → Silver → Gold

This domain will later demonstrate Delta Lake transformations using PySpark.
