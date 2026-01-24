# USE_EAM_ACCOUNTS - iPurchase System Setting

**Category:** EAM Integration

TRUE | FALSE. Use EAM account structure.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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