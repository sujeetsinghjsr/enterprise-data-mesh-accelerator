<img width="879" height="576" alt="Screenshot 2026-09-19 at 2 04 58 PM" src="https://github.com/user-attachments/assets/aaaf234d-af5e-461e-b9a4-00813fe6e4b3" />

## Pipeline Architecture

Raw trade events enter the Bronze layer before being standardized in Silver and published as governed business-ready datasets in Gold.

This mirrors enterprise Lakehouse implementation patterns used by modern Data Engineering teams.

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
