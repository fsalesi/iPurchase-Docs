# CATALOG_CAN_DELETE - iPurchase System Setting

**Category:** Catalog & Vendors

Comma Separated list of User ID's or Group ID's that are allowed to delete catalogs.

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
| **Setting Name** | CATALOG_CAN_DELETE |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_CAN_DELETE'
```

### Related Settings

- [CATALOG_ACCESS_[Supplier NBR]](<CATALOG_ACCESS_[Supplier NBR].md>)
- [CATALOG_CAN_RATE](CATALOG_CAN_RATE.md)
- [CATALOG_CART_SHOW_DETAILS](CATALOG_CART_SHOW_DETAILS.md)
