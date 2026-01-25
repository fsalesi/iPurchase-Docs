# BUDGET_HIDE_OTHER - iPurchase System Setting

**Category:** GL Accounts & Finance

Do not show nor use the Other column on Budgets.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This display setting controls what information is visible to users in the interface.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_HIDE_OTHER |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_HIDE_OTHER'
```

### Related Settings

- [BUDGET_ADMINISTRATOR](BUDGET_ADMINISTRATOR.md)
- [BUDGET_ASST_EDIT](BUDGET_ASST_EDIT.md)
- [BUDGET_MGR_EDIT](BUDGET_MGR_EDIT.md)
