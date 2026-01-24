# SYNC_REQ_DET - iPurchase System Setting

**Category:** Requisitions

A setting of True will synchronize iPurchase Requisition Lines with the requisition (req_det) functionality in QAD. Only items which are planned by MRP will be synchronized

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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