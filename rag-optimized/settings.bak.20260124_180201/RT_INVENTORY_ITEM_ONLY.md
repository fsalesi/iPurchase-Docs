# RT_INVENTORY_ITEM_ONLY - iPurchase System Setting

**Category:** Requisitions

Comma-separated req types. Types that require items to be in inventory catalog.

**Common questions this answers:**
- What is RT_INVENTORY_ITEM_ONLY?
- What does RT_INVENTORY_ITEM_ONLY do?
- What is the default value for RT_INVENTORY_ITEM_ONLY?
- How do I configure RT_INVENTORY_ITEM_ONLY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_INVENTORY_ITEM_ONLY |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_INVENTORY_ITEM_ONLY'
```
