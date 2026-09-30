# API Guide

## Health
`GET /health`

## Explain code
`POST /api/v1/explain`

Request:
```json
{"language":"python","code":"def add(a,b): return a+b"}
```

## Generate SQL
`POST /api/v1/sql`

Request:
```json
{"request":"show the latest orders","schema_context":"orders(id,created_at,total)"}
```

## Generate documentation
`POST /api/v1/document`

All endpoints return a `result` and the active execution `mode`.
