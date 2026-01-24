# RT_REQ_TAXABLE - iPurchase System Setting

**Category:** GL Accounts & Finance

Comma-separated req types. Types where tax is calculated. If blank, all types are taxable.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_REQ_TAXABLE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_REQ_TAXABLE'
```
