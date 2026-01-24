# MRP_SORT - iPurchase System Setting

**Category:** Inventory & MRP

Sort field for MRP (Material Requirements Planning) item listings.

**Common questions this answers:**
- What is MRP_SORT?
- What does MRP_SORT do?
- What is the default value for MRP_SORT?
- How do I configure MRP_SORT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MRP_SORT |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MRP_SORT'
```
