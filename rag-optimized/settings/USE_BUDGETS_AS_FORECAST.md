# USE_BUDGETS_AS_FORECAST - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow full budget functionality but allow reqs to be created and processed even if overbudget.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_BUDGETS_AS_FORECAST |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_BUDGETS_AS_FORECAST'
```
