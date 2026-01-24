# PO_UPDATE_CHECK_REROUTE_RELEASES - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE. If TRUE, checks blanket PO releases for material changes requiring reroute.

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
| **Setting Name** | PO_UPDATE_CHECK_REROUTE_RELEASES |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_CHECK_REROUTE_RELEASES'
```