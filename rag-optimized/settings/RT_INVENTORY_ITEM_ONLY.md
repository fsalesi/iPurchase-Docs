# RT_INVENTORY_ITEM_ONLY - iPurchase System Setting

**Category:** Requisitions

Comma-separated req types. Types that require items to be in inventory catalog.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_INVENTORY_ITEM_ONLY |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_INVENTORY_ITEM_ONLY'
```