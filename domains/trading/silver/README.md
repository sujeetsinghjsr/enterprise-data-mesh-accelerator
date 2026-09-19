# Silver Layer

The Silver layer transforms raw trade events into trusted engineering datasets.

## Responsibilities

- Schema validation
- Duplicate removal
- Business rule filtering
- Standardized values
- Derived metrics

## Current Business Rules

| Rule | Reason |
|------|---------|
| Remove duplicate trades | Data consistency |
| Ignore cancelled trades | Business reporting |
| Convert commodity names to uppercase | Standardization |
| Calculate Trade Value | Analytics |

## Output

The Silver layer produces standardized Delta tables that are ready for downstream business consumption.
