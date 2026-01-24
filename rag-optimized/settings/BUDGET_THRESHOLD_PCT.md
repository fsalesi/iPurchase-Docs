# BUDGET_THRESHOLD_PCT - iPurchase System Setting

**Category:** GL Accounts & Finance

Threshold pct added to defined budget amount before error that you can not create another item using that budget.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_THRESHOLD_PCT |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_THRESHOLD_PCT'
```
