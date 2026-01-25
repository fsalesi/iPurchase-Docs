# PUNCHOUT_DISABLE_USERS - iPurchase System Setting

**Category:** Catalog & Vendors

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
| **Setting Name** | PUNCHOUT_DISABLE_USERS |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_DISABLE_USERS'
```

### Related Settings

- [PUNCHOUT_LEADTIME](PUNCHOUT_LEADTIME.md)
- [PUNCHOUT_NOFRAMES](PUNCHOUT_NOFRAMES.md)
- [PUNCHOUT_NO_ITEM_DESC](PUNCHOUT_NO_ITEM_DESC.md)
