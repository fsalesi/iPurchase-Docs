# RT_[Requisition Type]_ACCOUNT_RANGE - iPurchase System Setting

**Category:** Requisitions

Substitute the requisition type for "[REQUISITION TYPE]".

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
| **Setting Name** | RT_[Requisition Type]_ACCOUNT_RANGE |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_ACCOUNT_RANGE'
```

### Related Settings

- [RT_INVENTORY_ITEM_ONLY](RT_INVENTORY_ITEM_ONLY.md)
- [RT_[Requisition Type]_ACCESS](<RT_[Requisition Type]_ACCESS.md>)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](<RT_[Requisition Type]_ACCOUNT_DEFAULT.md>)
