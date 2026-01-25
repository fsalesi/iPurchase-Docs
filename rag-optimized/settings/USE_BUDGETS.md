# USE_BUDGETS - iPurchase System Setting

**Category:** GL Accounts & Finance

[LEGACY/OBSOLETE] TRUE | FALSE.

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
| **Setting Name** | USE_BUDGETS |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_BUDGETS'
```

### Related Settings

- [USE_BUDGETS_AS_FORECAST](USE_BUDGETS_AS_FORECAST.md)
