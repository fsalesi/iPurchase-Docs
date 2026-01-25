# REOPEN_PO - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of User ID's or Group ID's that are allowed to re-open a closed or cancelled PO via a change order.

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
| **Setting Name** | REOPEN_PO |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REOPEN_PO'
```