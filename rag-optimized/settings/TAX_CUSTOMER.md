# TAX_CUSTOMER - iPurchase System Setting

**Category:** GL Accounts & Finance

Default tax customer code for tax calculations.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TAX_CUSTOMER |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TAX_CUSTOMER'
```

### Related Settings

- [TAX_CLASS_FIELD](TAX_CLASS_FIELD.md)
- [TAX_USAGE_FIELD](TAX_USAGE_FIELD.md)
