# DEFAULT_TAX_USAGE - iPurchase System Setting

**Category:** GL Accounts & Finance

You can use this to set the Tax Usage field in QAD. If set this will default for all Purchase Orders.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_TAX_USAGE |
| **Category** | GL Accounts & Finance |
| **Owner** |  |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_TAX_USAGE'
```
