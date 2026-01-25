# PO_UPDATE_CHECK_REROUTE_RELEASES - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | checks blanket PO releases for material changes requiring reroute |
| **FALSE** | Disables this feature |

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

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

### Related Settings

- [PO_UPDATE_CHECK_REROUTE](PO_UPDATE_CHECK_REROUTE.md)