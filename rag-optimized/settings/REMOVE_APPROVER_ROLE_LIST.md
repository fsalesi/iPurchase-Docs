# REMOVE_APPROVER_ROLE_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that are allowed to remove an Approver from any requisition. Asterisk indicates everyone, a blank indicates no one.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

**Common patterns:**
- `*` - Everyone/all values allowed
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_APPROVER_ROLE_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_APPROVER_ROLE_LIST'
```