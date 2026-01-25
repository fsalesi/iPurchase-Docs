# USE_BUDGETS_AS_FORECAST - iPurchase System Setting

**Category:** GL Accounts & Finance

Allow full budget functionality but allow reqs to be created and processed even if overbudget.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

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

### Related Settings

- [USE_BUDGETS](USE_BUDGETS.md)
