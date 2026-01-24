# CODE_LIST_H_XXREQ_UCHAR2 - iPurchase System Setting

**Category:** Requisitions

List for User Field 2

**Common questions this answers:**
- What is CODE_LIST_H_XXREQ_UCHAR2?
- What does CODE_LIST_H_XXREQ_UCHAR2 do?
- What is the default value for CODE_LIST_H_XXREQ_UCHAR2?
- How do I configure CODE_LIST_H_XXREQ_UCHAR2?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_XXREQ_UCHAR2 |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | List:1:Maybe,2:Maybe Not |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_XXREQ_UCHAR2'
```
