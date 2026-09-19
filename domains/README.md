# Business Domains

Data Mesh organizes data ownership around business capabilities rather than a centralized data warehouse.

In this reference implementation, each business domain owns its own data products, quality rules, metadata, and publishing responsibilities.

## Available Domains

| Domain | Primary Responsibility |
|---------|------------------------|
| Trading | Trade execution and market data |
| Supply Chain | Inventory and logistics |
| Finance | Revenue and P&L reporting |
| Risk | Risk calculations and exposure |

Each domain will later publish its own Bronze, Silver, and Gold data products.

<img width="614" height="386" alt="Screenshot 2026-09-19 at 1 36 41 PM" src="https://github.com/user-attachments/assets/10a8c547-8ba0-4415-b4df-3952ba0b1826" />

## Domain Ownership Model

Instead of sending all data to one centralized engineering team, each business domain owns:

- its own pipelines,
- its own data quality,
- its own documentation,
- and its own published data products.

The platform team provides reusable capabilities such as governance, infrastructure, and security.
