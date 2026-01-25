# CODE_LIST_TAX_USAGE - iPurchase System Setting

**Category:** GL Accounts & Finance

Configuration setting for gl accounts & finance.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_USAGE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | comma-separated list of tax usage. List: is not needed on this setting |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_USAGE'
```

### Related Settings

- [CODE_LIST_TAX_CLASS](CODE_LIST_TAX_CLASS.md)
- [CODE_LIST_TAX_ENVIRONMENT](CODE_LIST_TAX_ENVIRONMENT.md)