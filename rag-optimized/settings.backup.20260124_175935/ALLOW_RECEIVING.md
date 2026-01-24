# ALLOW_RECEIVING - iPurchase System Setting

**Category:** Receiving

Can-Do list. Users/groups allowed to receive against purchase orders. Can include $xxreq_buyer to allow the buyer on the PO to receive.

**Common questions this answers:**
- What is ALLOW_RECEIVING?
- What does ALLOW_RECEIVING do?
- What is the default value for ALLOW_RECEIVING?
- How do I configure ALLOW_RECEIVING?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_RECEIVING |
| **Category** | Receiving |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_RECEIVING'
```
