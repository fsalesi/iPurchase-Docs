# RT_[Requisition Type]_INVENTORY_ITEM_ONLY - iPurchase System Setting

**Category:** Requisitions

True or False For Inventory as an example, only Inventory items can be purchased

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_INVENTORY_ITEM_ONLY |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_INVENTORY_ITEM_ONLY'
```