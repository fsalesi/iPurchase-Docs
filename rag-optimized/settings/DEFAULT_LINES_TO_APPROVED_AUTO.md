# DEFAULT_LINES_TO_APPROVED_AUTO - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated List of User ID's or Group ID's.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) to specify which users or groups have access.

**Common configurations:**
- `*` - All users/everyone
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

### Related Settings

- [DEFAULT_LINES_TO_APPROVED](DEFAULT_LINES_TO_APPROVED.md)