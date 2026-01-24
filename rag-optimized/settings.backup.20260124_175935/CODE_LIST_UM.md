# CODE_LIST_UM - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line Unit of Measure selection list and validation. A value of blank or a non-existing setting wil...

**Common questions this answers:**
- What is CODE_LIST_UM?
- What does CODE_LIST_UM do?
- What is the default value for CODE_LIST_UM?
- How do I configure CODE_LIST_UM?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_UM |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Finance |
| **Default Value** | pt_um |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_UM'
```
