# UPDATE_COST_ON_CO - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UPDATE_COST_ON_CO |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UPDATE_COST_ON_CO'
```

### Related Settings

- [UPDATE_COST_ON_COPY](UPDATE_COST_ON_COPY.md)