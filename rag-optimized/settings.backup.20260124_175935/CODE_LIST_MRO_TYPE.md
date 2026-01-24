# CODE_LIST_MRO_TYPE - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line MRO Type selection list, and validation. You can also use the prefix "LIST:" followed by a co...

**Common questions this answers:**
- What is CODE_LIST_MRO_TYPE?
- What does CODE_LIST_MRO_TYPE do?
- What is the default value for CODE_LIST_MRO_TYPE?
- How do I configure CODE_LIST_MRO_TYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_MRO_TYPE |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_MRO_TYPE'
```
