# BUDGET_ASST_EDIT - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow the budget assistant managers specified in a budget the ability to modify the sub budgets. Assistant Managers can't modify the budget header.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_ASST_EDIT |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_ASST_EDIT'
```
