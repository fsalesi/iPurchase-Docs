# USER_IMPORT_FOLDER - iPurchase System Setting

**Category:** User Management

Directory path on application server.

### How It Works

This setting configures user management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_IMPORT_FOLDER |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_IMPORT_FOLDER'
```

### Related Settings

- [USER_PROFILE_FIELDS](USER_PROFILE_FIELDS.md)