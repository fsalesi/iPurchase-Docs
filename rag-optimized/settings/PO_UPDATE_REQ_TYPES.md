# PO_UPDATE_REQ_TYPES - iPurchase System Setting

**Category:** Purchase Orders

You can control the list of requisition types that will allow a change order, or * for all requisition types.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_REQ_TYPES |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_REQ_TYPES'
```
