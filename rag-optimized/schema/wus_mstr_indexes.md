# wus_mstr - User Master Table - Indexes

Database indexes for the wus_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on wus_mstr?
- How do I query wus_mstr efficiently?
- What is the primary key of wus_mstr?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_erp_initials` | - | `wus_erp_initials` |
| `by_wus_company` | - | `wus_company` |
| `by_wus_id` | Primary + Unique | `wus_id` |
| `by_wus_name` | - | `wus_name` |
| `by_wus_type` | - | `wus_type` |
| `wus_delegate` | - | `wus_delegate` |
| `wus_disable` | - | `wus_disable` |
| `wus_groups` | Word | `wus_groups` |
| `wus_name_word` | Word | `wus_name` |
| `wus_supervisor` | - | `wus_supervisor` |