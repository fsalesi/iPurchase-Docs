# TAX_CLASS_FIELD - iPurchase System Setting

**Category:** GL Accounts & Finance

[LEGACY/OBSOLETE] Field name for tax class in data upgrades.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TAX_CLASS_FIELD |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TAX_CLASS_FIELD'
```

### Related Settings

- [TAX_CUSTOMER](TAX_CUSTOMER.md)
- [TAX_USAGE_FIELD](TAX_USAGE_FIELD.md)
