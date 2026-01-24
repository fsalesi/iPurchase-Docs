# JE_USE_EAM - iPurchase System Setting

**Category:** EAM Integration

TRUE | FALSE. If TRUE, uses EAM system for journal entry processing.

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
| **Setting Name** | JE_USE_EAM |
| **Category** | EAM Integration |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'JE_USE_EAM'
```