# CODE_LIST_H_BLANKET_CYCLE - iPurchase System Setting

**Category:** Code Lists & Dropdowns

Enter a comma-separated list of cycle codes to be entered in the cycle code drop down menu on the blanket information tab on a requisition.

**Common questions this answers:**
- What is CODE_LIST_H_BLANKET_CYCLE?
- What does CODE_LIST_H_BLANKET_CYCLE do?
- What is the default value for CODE_LIST_H_BLANKET_CYCLE?
- How do I configure CODE_LIST_H_BLANKET_CYCLE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_BLANKET_CYCLE |
| **Category** | Code Lists & Dropdowns |
| **Owner** | ISS |
| **Default Value** | List:MO:Monthly,WK:Weekly,DA:Daily |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_BLANKET_CYCLE'
```
