# Architecture Decisions

## ADR-001

### Decision

Use Bronze, Silver, and Gold architecture.

### Reason

Separate raw ingestion from business-ready analytics.

---

## ADR-002

### Decision

Use Delta Lake.

### Reason

- ACID transactions
- Schema evolution
- Reliable updates

---

## ADR-003

### Decision

Partition by trade_date.

### Reason

Improve query performance.

---

## ADR-004

### Decision

Use Unity Catalog.

### Reason

Centralize governance while preserving domain ownership.
