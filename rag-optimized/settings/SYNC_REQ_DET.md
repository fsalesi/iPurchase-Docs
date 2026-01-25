# SYNC_REQ_DET - iPurchase System Setting

**Category:** Requisitions

A setting of True will synchronize iPurchase Requisition Lines with the requisition (req_det) functionality in QAD.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SYNC_REQ_DET |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SYNC_REQ_DET'
```