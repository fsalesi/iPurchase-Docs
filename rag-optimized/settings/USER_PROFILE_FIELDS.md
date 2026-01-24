# USER_PROFILE_FIELDS - iPurchase System Setting

**Category:** User Management

Comma-separated field names. Custom user profile fields to display/edit.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_PROFILE_FIELDS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_PROFILE_FIELDS'
```
