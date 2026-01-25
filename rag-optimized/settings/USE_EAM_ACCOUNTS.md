# USE_EAM_ACCOUNTS - iPurchase System Setting

**Category:** EAM Integration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures eam integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_EAM_ACCOUNTS |
| **Category** | EAM Integration |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_EAM_ACCOUNTS'
```

### Related Settings

- [USE_SINGLE_CURRENCY](USE_SINGLE_CURRENCY.md)
