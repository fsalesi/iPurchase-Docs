# CO_REROUTE_EXCLUDE_TYPES - iPurchase System Setting

**Category:** Change Orders

Comma-separated requisition types.

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_REROUTE_EXCLUDE_TYPES |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_REROUTE_EXCLUDE_TYPES'
```

### Related Settings

- [CO_DELETE_CANCELLED_LINES](CO_DELETE_CANCELLED_LINES.md)
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md)
- [CO_IGNORE_COST](CO_IGNORE_COST.md)