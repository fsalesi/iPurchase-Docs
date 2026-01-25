# INQUIRY_AFTER_APPROVAL - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or group id's that are re-directed to the pending queue once they have approved a requisition.

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
| **Setting Name** | INQUIRY_AFTER_APPROVAL |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_AFTER_APPROVAL'
```