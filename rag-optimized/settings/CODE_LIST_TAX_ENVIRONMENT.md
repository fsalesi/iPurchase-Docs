# CODE_LIST_TAX_ENVIRONMENT - iPurchase System Setting

**Category:** GL Accounts & Finance

LIST format.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_ENVIRONMENT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_ENVIRONMENT'
```

### Related Settings

- [CODE_LIST_TAX_CLASS](CODE_LIST_TAX_CLASS.md)
- [CODE_LIST_TAX_USAGE](CODE_LIST_TAX_USAGE.md)