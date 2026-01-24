# MRO_ITEMS_REQ_TYPES - iPurchase System Setting

**Category:** Requisitions

Comma-separated requisition types. Types that allow MRO (Maintenance, Repair, Operations) items.

**Common questions this answers:**
- What is MRO_ITEMS_REQ_TYPES?
- What does MRO_ITEMS_REQ_TYPES do?
- What is the default value for MRO_ITEMS_REQ_TYPES?
- How do I configure MRO_ITEMS_REQ_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MRO_ITEMS_REQ_TYPES |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MRO_ITEMS_REQ_TYPES'
```
