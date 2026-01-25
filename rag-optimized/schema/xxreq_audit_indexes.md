# xxreq_audit - Requisition Approval Audit Trail Table - Indexes

Database indexes for the xxreq_audit table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxreq_audit?
- How do I query xxreq_audit efficiently?
- What is the primary key of xxreq_audit?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `active_date` | - | `xxreq_domain`, `xxreq_active_date`, `xxreq_active_time` |
| `approver` | - | `xxreq_domain`, `xxreq_nbr`, `xxreq_submit_attempt`, `xxreq_app_id` |
| `decomposed` | Word | `xxreq_decom_app_id` |
| `pri` | Primary + Unique | `xxreq_unique` |
| `xxreq_reject_code` | - | `xxreq_reject_code` |