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
