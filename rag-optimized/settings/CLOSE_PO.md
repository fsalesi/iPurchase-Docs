# CLOSE_PO - iPurchase System Setting

**Category:** Purchase Orders

Comma Separated list of User ID's or Group ID's that will have the ability to close PO  or  PO line on Purchase order.

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
| **Setting Name** | CLOSE_PO |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CLOSE_PO'
```