# BUDGET_HIDE_OTHER - iPurchase System Setting

**Category:** GL Accounts & Finance

Do not show nor use the Other column on Budgets.

**Common questions this answers:**
- What is BUDGET_HIDE_OTHER?
- What does BUDGET_HIDE_OTHER do?
- What is the default value for BUDGET_HIDE_OTHER?
- How do I configure BUDGET_HIDE_OTHER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_HIDE_OTHER |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_HIDE_OTHER'
```
