# CO_IGNORE_COST - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | cost changes are ignored when determining if change order is material (requires re-routing) |
| **FALSE** | Disables this feature |

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_IGNORE_COST |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_IGNORE_COST'
```

### Related Settings

- [CO_DELETE_CANCELLED_LINES](CO_DELETE_CANCELLED_LINES.md)
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md)
- [CO_ITEM_REROUTE_FIELDS](CO_ITEM_REROUTE_FIELDS.md)