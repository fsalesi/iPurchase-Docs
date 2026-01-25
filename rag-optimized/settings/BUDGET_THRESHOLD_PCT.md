# BUDGET_THRESHOLD_PCT - iPurchase System Setting

**Category:** GL Accounts & Finance

Threshold pct added to defined budget amount before error that you can not create another item using that budget.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

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

### Related Settings

- [BUDGET_ADMINISTRATOR](BUDGET_ADMINISTRATOR.md)
- [BUDGET_ASST_EDIT](BUDGET_ASST_EDIT.md)
- [BUDGET_HIDE_OTHER](BUDGET_HIDE_OTHER.md)
