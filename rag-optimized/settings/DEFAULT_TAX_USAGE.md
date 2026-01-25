# DEFAULT_TAX_USAGE - iPurchase System Setting

**Category:** GL Accounts & Finance

You can use this to set the Tax Usage field in QAD.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_TAX_USAGE |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_TAX_USAGE'
```

### Related Settings

- [DEFAULT_SUB_ACCOUNT](DEFAULT_SUB_ACCOUNT.md)
- [DEFAULT_TAX_CLASS](DEFAULT_TAX_CLASS.md)
- [DEFAULT_TAX_ENVIRONMENT](DEFAULT_TAX_ENVIRONMENT.md)
