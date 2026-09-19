# Trading Pipeline Architecture

This pipeline follows a Lakehouse architecture inspired by enterprise Data Mesh implementations.

## Pipeline Flow

Raw CSV

↓

Bronze

↓

Silver

↓

Gold

## Bronze

Purpose:

- Preserve raw records
- Add audit timestamps

## Silver

Purpose:

- Validate schema
- Remove duplicates
- Apply business rules
- Standardize data

## Gold

Purpose:

- Business-ready reporting
- Daily analytics
- Executive dashboards
