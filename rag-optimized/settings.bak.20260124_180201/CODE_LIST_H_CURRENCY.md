# CODE_LIST_H_CURRENCY - iPurchase System Setting

**Category:** Code Lists & Dropdowns

Currency List same as other lists - blank will use all currencies from QAD - cu_mstr

**Common questions this answers:**
- What is CODE_LIST_H_CURRENCY?
- What does CODE_LIST_H_CURRENCY do?
- What is the default value for CODE_LIST_H_CURRENCY?
- How do I configure CODE_LIST_H_CURRENCY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_CURRENCY |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_CURRENCY'
```
