# EMT_REQ_TYPE - iPurchase System Setting

**Category:** Requisitions

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is EMT_REQ_TYPE?
- What does EMT_REQ_TYPE do?
- What is the default value for EMT_REQ_TYPE?
- How do I configure EMT_REQ_TYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMT_REQ_TYPE |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMT_REQ_TYPE'
```
