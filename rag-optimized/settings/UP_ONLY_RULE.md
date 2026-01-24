# UP_ONLY_RULE - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE. Enable Update PO Only routing rule for change orders that don't require full re-routing.

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
| **Setting Name** | UP_ONLY_RULE |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UP_ONLY_RULE'
```