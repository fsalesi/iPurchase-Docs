# BUDGET_MGR_EDIT - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow the budget manager specified in a budget the ability to modify the entire budget

**Common questions this answers:**
- What is BUDGET_MGR_EDIT?
- What does BUDGET_MGR_EDIT do?
- What is the default value for BUDGET_MGR_EDIT?
- How do I configure BUDGET_MGR_EDIT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_MGR_EDIT |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_MGR_EDIT'
```
