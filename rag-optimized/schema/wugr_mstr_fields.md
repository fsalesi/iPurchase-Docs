# wugr_mstr - User-Group Membership Table - Fields

Links users to groups. Each record represents one user belonging to one group. Used to determine group membership for approval routing.

**Common questions this answers:**
- What fields are in the wugr_mstr table?
- What fields are in the user-group membership table?

**Related tables:** wus_mstr (users), wgr_mstr (groups)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `wugr_gr_id` | char | im | Group ID (FK to wgr_mstr) |
| `wugr_us_id` | char | im | User ID (FK to wus_mstr) |
| `wugr_create_date` | date |  |  |
| `wugr_create_by` | char |  |  |
| `wugr_disable` | logi |  | TRUE = membership disabled |
| `wugr_expire_date` | date |  |  |