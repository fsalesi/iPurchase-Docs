# CODE_LIST_H_SHIPTO - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname  or  blank This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Ship To selection list and validation.  Leaving this value blank will tell iPurc...

**Common questions this answers:**
- What is CODE_LIST_H_SHIPTO?
- What does CODE_LIST_H_SHIPTO do?
- What is the default value for CODE_LIST_H_SHIPTO?
- How do I configure CODE_LIST_H_SHIPTO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_SHIPTO |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_SHIPTO'
```
