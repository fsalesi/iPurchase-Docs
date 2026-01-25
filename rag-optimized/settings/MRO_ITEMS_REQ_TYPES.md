# MRO_ITEMS_REQ_TYPES - iPurchase System Setting

**Category:** Requisitions

Comma-separated requisition types.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MRO_ITEMS_REQ_TYPES |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MRO_ITEMS_REQ_TYPES'
```