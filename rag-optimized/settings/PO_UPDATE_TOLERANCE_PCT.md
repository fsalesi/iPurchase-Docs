# PO_UPDATE_TOLERANCE_PCT - iPurchase System Setting

**Category:** Purchase Orders

This is the percentage that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order.

**Common questions this answers:**
- What is PO_UPDATE_TOLERANCE_PCT?
- What does PO_UPDATE_TOLERANCE_PCT do?
- What is the default value for PO_UPDATE_TOLERANCE_PCT?
- How do I configure PO_UPDATE_TOLERANCE_PCT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_TOLERANCE_PCT |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | 10 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_TOLERANCE_PCT'
```
