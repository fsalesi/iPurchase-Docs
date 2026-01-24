# ADD_REQ_NBR_TO_PO - iPurchase System Setting

**Category:** Requisitions

When a PO is created do you want to add the requisition number and line to pod_req and pod_req_line fields. This should be set to False if using 2009SE or above; or if GRS is being used

### How It Works

See the description above for valid values and usage.

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
