# CO_DELETE_CANCELLED_LINES - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | permanently deletes cancelled lines on change orders |
| **FALSE** | lines remain with cancelled status |

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_DELETE_CANCELLED_LINES |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_DELETE_CANCELLED_LINES'
```

### Related Settings

- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md)
- [CO_IGNORE_COST](CO_IGNORE_COST.md)
- [CO_ITEM_REROUTE_FIELDS](CO_ITEM_REROUTE_FIELDS.md)
