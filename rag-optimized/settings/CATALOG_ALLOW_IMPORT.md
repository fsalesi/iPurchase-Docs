# CATALOG_ALLOW_IMPORT - iPurchase System Setting

**Category:** User Management

Comma Separated list of User ID's or Group ID's that are allowed to import catalogs.

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
| **Setting Name** | CATALOG_ALLOW_IMPORT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_ALLOW_IMPORT'
```

### Related Settings

- [CATALOG_ALLOW_EXPORT](CATALOG_ALLOW_EXPORT.md)
- [CATALOG_REQUEST_ALLOW_IMPORT](CATALOG_REQUEST_ALLOW_IMPORT.md)
