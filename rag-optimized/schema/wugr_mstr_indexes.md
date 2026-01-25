# wugr_mstr - User-Group Membership Table - Indexes

Database indexes for the wugr_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on wugr_mstr?
- How do I query wugr_mstr efficiently?
- What is the primary key of wugr_mstr?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_wugr_id` | Primary + Unique | `wugr_gr_id`, `wugr_us_id` |
| `by_wugr_us_id` | - | `wugr_us_id`, `wugr_gr_id` |