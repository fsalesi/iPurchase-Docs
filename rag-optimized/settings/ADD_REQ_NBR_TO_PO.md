# ADD_REQ_NBR_TO_PO - iPurchase System Setting

**Category:** Requisitions

When a PO is created do you want to add the requisition number and line to pod_req and pod_req_line fields.

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
| **Setting Name** | ADD_REQ_NBR_TO_PO |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ADD_REQ_NBR_TO_PO'
```