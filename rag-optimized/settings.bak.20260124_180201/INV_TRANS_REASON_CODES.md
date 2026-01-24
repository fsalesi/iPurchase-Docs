# INV_TRANS_REASON_CODES - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated reason codes. Valid transaction reason codes for inventory movements.

**Common questions this answers:**
- What is INV_TRANS_REASON_CODES?
- What does INV_TRANS_REASON_CODES do?
- What is the default value for INV_TRANS_REASON_CODES?
- How do I configure INV_TRANS_REASON_CODES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INV_TRANS_REASON_CODES |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INV_TRANS_REASON_CODES'
```
