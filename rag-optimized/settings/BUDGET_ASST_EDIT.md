# BUDGET_ASST_EDIT - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow the budget assistant managers specified in a budget the ability to modify the sub budgets.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

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

### Related Settings

- [BUDGET_ADMINISTRATOR](BUDGET_ADMINISTRATOR.md)
- [BUDGET_HIDE_OTHER](BUDGET_HIDE_OTHER.md)
- [BUDGET_MGR_EDIT](BUDGET_MGR_EDIT.md)
