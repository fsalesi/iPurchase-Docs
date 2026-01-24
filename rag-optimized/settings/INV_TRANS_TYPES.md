# INV_TRANS_TYPES - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated transaction types. Valid inventory transaction types.

**Common questions this answers:**
- What is INV_TRANS_TYPES?
- What does INV_TRANS_TYPES do?
- What is the default value for INV_TRANS_TYPES?
- How do I configure INV_TRANS_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INV_TRANS_TYPES |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INV_TRANS_TYPES'
```
