# ALLOW_NEW_REQUEST - iPurchase System Setting

**Category:** Requisitions

Can-Do list.

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
| **Setting Name** | ALLOW_NEW_REQUEST |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_NEW_REQUEST'
```

### Related Settings

- [ALLOW_NEGATIVE_LINE](ALLOW_NEGATIVE_LINE.md)
- [ALLOW_SAVE_TEMPLATE](ALLOW_SAVE_TEMPLATE.md)
