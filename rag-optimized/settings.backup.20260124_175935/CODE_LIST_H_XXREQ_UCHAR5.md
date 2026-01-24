# CODE_LIST_H_XXREQ_UCHAR5 - iPurchase System Setting

**Category:** Requisitions

List for User Field 5

**Common questions this answers:**
- What is CODE_LIST_H_XXREQ_UCHAR5?
- What does CODE_LIST_H_XXREQ_UCHAR5 do?
- What is the default value for CODE_LIST_H_XXREQ_UCHAR5?
- How do I configure CODE_LIST_H_XXREQ_UCHAR5?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_XXREQ_UCHAR5 |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | List:True:Choice 1,False:Choice 2 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_XXREQ_UCHAR5'
```
