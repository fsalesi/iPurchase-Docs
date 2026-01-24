# EMPLOYMENT_DEPT_LIST - iPurchase System Setting

**Category:** User Management

Comma-separated department codes. Valid departments for user employment records/profiles.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMPLOYMENT_DEPT_LIST |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMPLOYMENT_DEPT_LIST'
```