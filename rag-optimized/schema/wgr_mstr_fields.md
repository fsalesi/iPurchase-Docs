# wgr_mstr - Group Master Table - Fields

Defines groups used for approval routing, permissions, and organizational structure. Groups can be referenced in approval rules as approvers.

**Common questions this answers:**
- What fields are in the wgr_mstr table?
- What fields are in the group master table?
- What is wgr_id?

**Related tables:** wugr_mstr (membership), xxapp_mstr (approval rules), wus_mstr (users)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `wgr_id` | char | im | Unique group identifier |
| `wgr_name` | char | i | Group display name |
| `wgr_desc` | char |  | Group description |
| `wgr_mgr` | char |  | Group manager user ID |
| `wgr_level` | char |  |  |
| `wgr_create_date` | date |  |  |
| `wgr_create_by` | char |  |  |
| `wgr_disable` | logi |  | TRUE = group disabled |
| `wgr_expire_date` | date |  |  |
| `wgr_type` | char | i | Group type classification |