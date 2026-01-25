# DEFAULT_SUB_ACCOUNT - iPurchase System Setting

**Category:** GL Accounts & Finance

The default sub account is used when creating requisition from catalogs and punchouts.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SUB_ACCOUNT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SUB_ACCOUNT'
```

### Related Settings

- [DEFAULT_TAX_CLASS](DEFAULT_TAX_CLASS.md)
- [DEFAULT_TAX_ENVIRONMENT](DEFAULT_TAX_ENVIRONMENT.md)
- [DEFAULT_TAX_USAGE](DEFAULT_TAX_USAGE.md)