# xxmail_mstr - Email Queue Header Table - Indexes

Database indexes for the xxmail_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxmail_mstr?
- How do I query xxmail_mstr efficiently?
- What is the primary key of xxmail_mstr?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byDate` | - | `xxmail_date` |
| `byStatus` | - | `xxmail_status`, `xxmail_seq` |
| `byUser` | - | `xxmail_user` |
| `pri` | Primary + Unique | `xxmail_seq` |