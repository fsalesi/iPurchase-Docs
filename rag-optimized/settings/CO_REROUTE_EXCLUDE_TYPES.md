# CO_REROUTE_EXCLUDE_TYPES - iPurchase System Setting

**Category:** Change Orders

Comma-separated requisition types. Types excluded from change order re-routing even when changes are material.

### How It Works

See the description above for valid values and usage.

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
