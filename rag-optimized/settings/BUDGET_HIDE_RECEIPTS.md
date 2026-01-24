# BUDGET_HIDE_RECEIPTS - iPurchase System Setting

**Category:** Receiving

Do not show nor use the Receipts column on Budgets.

**Common questions this answers:**
- What is BUDGET_HIDE_RECEIPTS?
- What does BUDGET_HIDE_RECEIPTS do?
- What is the default value for BUDGET_HIDE_RECEIPTS?
- How do I configure BUDGET_HIDE_RECEIPTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_HIDE_RECEIPTS |
| **Category** | Receiving |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_HIDE_RECEIPTS'
```
