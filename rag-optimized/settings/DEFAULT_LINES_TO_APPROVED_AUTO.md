# DEFAULT_LINES_TO_APPROVED_AUTO - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated List of User ID's or Group ID's. If setting DEFAULT_LINES_TO_APPROVED is set to false, then adding a user or group to this setting will automatically approve any line items which are in the yellow status, after the user approves the requisition.  Therefore, the users listed here will not need to physically approve all line items individually.

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
| **Setting Name** | DEFAULT_LINES_TO_APPROVED_AUTO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_LINES_TO_APPROVED_AUTO'
```