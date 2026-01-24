# PO_UPDATE_TOLERANCE_AMOUNT - iPurchase System Setting

**Category:** Purchase Orders

This is the amount that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order.

**Common questions this answers:**
- What is PO_UPDATE_TOLERANCE_AMOUNT?
- What does PO_UPDATE_TOLERANCE_AMOUNT do?
- What is the default value for PO_UPDATE_TOLERANCE_AMOUNT?
- How do I configure PO_UPDATE_TOLERANCE_AMOUNT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_TOLERANCE_AMOUNT |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | 100 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_TOLERANCE_AMOUNT'
```
