# BUDGET_THRESHOLD_PCT - iPurchase System Setting

**Category:** GL Accounts & Finance

Threshold pct added to defined budget amount before error that you can not create another item using that budget.

**Common questions this answers:**
- What is BUDGET_THRESHOLD_PCT?
- What does BUDGET_THRESHOLD_PCT do?
- What is the default value for BUDGET_THRESHOLD_PCT?
- How do I configure BUDGET_THRESHOLD_PCT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_THRESHOLD_PCT |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_THRESHOLD_PCT'
```
