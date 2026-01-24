# USE_BUDGETS_AS_FORECAST - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow full budget functionality but allow reqs to be created and processed even if overbudget.

**Common questions this answers:**
- What is USE_BUDGETS_AS_FORECAST?
- What does USE_BUDGETS_AS_FORECAST do?
- What is the default value for USE_BUDGETS_AS_FORECAST?
- How do I configure USE_BUDGETS_AS_FORECAST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_BUDGETS_AS_FORECAST |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_BUDGETS_AS_FORECAST'
```
