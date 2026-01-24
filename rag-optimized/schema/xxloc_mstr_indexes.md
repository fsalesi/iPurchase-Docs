# xxloc_mstr - Location Master Table - Indexes

Database indexes for the xxloc_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxloc_mstr?
- How do I query xxloc_mstr efficiently?
- What is the primary key of xxloc_mstr?

## Indexes

| Index | Type | Fields |
|-------|------|--------|
| `bydomain` | - | `xxloc_domain` |
| `oid` | Unique | `oid_xxloc_mstr` |
| `pri` | Primary + Unique | `xxloc_domain`, `xxloc_supplier`, `xxloc_site` |