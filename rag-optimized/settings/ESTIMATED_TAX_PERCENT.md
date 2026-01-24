# ESTIMATED_TAX_PERCENT - iPurchase System Setting

**Category:** GL Accounts & Finance

If the taxable amounts need to figure into the approval rules, then use this setting to enter an estimate tax percentage that will be added on to all taxable requisition lines.  If 10% enter as "10"

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ESTIMATED_TAX_PERCENT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ESTIMATED_TAX_PERCENT'
```
