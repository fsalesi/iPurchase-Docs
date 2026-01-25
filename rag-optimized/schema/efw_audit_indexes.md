# efw_audit - efw_audit Table - Indexes

Database indexes for the efw_audit table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on efw_audit?
- How do I query efw_audit efficiently?
- What is the primary key of efw_audit?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_action` | - | `efw_audit_action` |
| `by_datetime` | - | `efw_audit_datetime` |
| `by_keyvalue` | - | `efw_audit_key_value` |
| `by_table` | - | `efw_audit_table` |
| `by_userid` | - | `efw_audit_userid` |
| `dom-seq` | Unique | `efw_audit_domain`, `efw_audit_sequence` |
| `keyvalue` | Unique | `efw_audit_domain`, `efw_audit_table`, `efw_audit_key_value`, `efw_audit_sequence` |
| `pri` | Primary + Unique | `efw_audit_sequence` |