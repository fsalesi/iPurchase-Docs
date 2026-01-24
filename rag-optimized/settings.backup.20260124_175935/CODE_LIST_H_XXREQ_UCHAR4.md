# CODE_LIST_H_XXREQ_UCHAR4 - iPurchase System Setting

**Category:** Requisitions

List for User Field 4

**Common questions this answers:**
- What is CODE_LIST_H_XXREQ_UCHAR4?
- What does CODE_LIST_H_XXREQ_UCHAR4 do?
- What is the default value for CODE_LIST_H_XXREQ_UCHAR4?
- How do I configure CODE_LIST_H_XXREQ_UCHAR4?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_XXREQ_UCHAR4 |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | List:True:True,False:False |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_XXREQ_UCHAR4'
```
