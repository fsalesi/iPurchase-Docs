# CODE_LIST_MRP_BUYERS - iPurchase System Setting

**Category:** Inventory & MRP

Only use this setting if you want to have a different buyer list show up in the MRP Action Center. This list is in the format 'list:code:desc,code:desc' or a generalized code field name like 'ptp_b...

**Common questions this answers:**
- What is CODE_LIST_MRP_BUYERS?
- What does CODE_LIST_MRP_BUYERS do?
- What is the default value for CODE_LIST_MRP_BUYERS?
- How do I configure CODE_LIST_MRP_BUYERS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_MRP_BUYERS |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_MRP_BUYERS'
```
