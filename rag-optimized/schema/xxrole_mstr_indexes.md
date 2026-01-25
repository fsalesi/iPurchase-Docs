# xxrole_mstr - xxrole_mstr Table - Indexes

Database indexes for the xxrole_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxrole_mstr?
- How do I query xxrole_mstr efficiently?
- What is the primary key of xxrole_mstr?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byapprover` | - | `xxrole_domain`, `xxrole_approver` |
| `byrole` | - | `xxrole_domain`, `xxrole_role` |
| `byvalue` | - | `xxrole_domain`, `xxrole_value` |
| `oid` | Unique | `oid_xxrole_mstr` |
| `pri` | Primary + Unique | `xxrole_domain`, `xxrole_type`, `xxrole_role`, `xxrole_value` |