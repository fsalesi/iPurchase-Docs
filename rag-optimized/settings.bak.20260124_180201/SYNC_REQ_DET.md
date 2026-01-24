# SYNC_REQ_DET - iPurchase System Setting

**Category:** Requisitions

A setting of True will synchronize iPurchase Requisition Lines with the requisition (req_det) functionality in QAD. Only items which are planned by MRP will be synchronized

**Common questions this answers:**
- What is SYNC_REQ_DET?
- What does SYNC_REQ_DET do?
- What is the default value for SYNC_REQ_DET?
- How do I configure SYNC_REQ_DET?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SYNC_REQ_DET |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SYNC_REQ_DET'
```
