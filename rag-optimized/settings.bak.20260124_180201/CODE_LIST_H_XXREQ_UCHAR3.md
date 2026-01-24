# CODE_LIST_H_XXREQ_UCHAR3 - iPurchase System Setting

**Category:** Requisitions

List for User Field 3

**Common questions this answers:**
- What is CODE_LIST_H_XXREQ_UCHAR3?
- What does CODE_LIST_H_XXREQ_UCHAR3 do?
- What is the default value for CODE_LIST_H_XXREQ_UCHAR3?
- How do I configure CODE_LIST_H_XXREQ_UCHAR3?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_XXREQ_UCHAR3 |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | List:Apples:Apples,Bananas:Bananas,Oranges:Oranges |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_XXREQ_UCHAR3'
```
