# JE_USE_EAM - iPurchase System Setting

**Category:** EAM Integration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | uses EAM system for journal entry processing |
| **FALSE** | Disables this feature |

### How It Works

This setting configures eam integration behavior in iPurchase.

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