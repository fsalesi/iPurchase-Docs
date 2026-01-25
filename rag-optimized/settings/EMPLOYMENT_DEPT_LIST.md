# EMPLOYMENT_DEPT_LIST - iPurchase System Setting

**Category:** User Management

Comma-separated department codes.

### How It Works

This setting configures user management behavior in iPurchase.

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

### Related Settings

- [EMPLOYMENT_DIVISION_LIST](EMPLOYMENT_DIVISION_LIST.md)
