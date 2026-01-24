# CODE_LIST_H_SITE - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Site selection list and validation.  Leaving this value blank will tell iPurchase to use th...

**Common questions this answers:**
- What is CODE_LIST_H_SITE?
- What does CODE_LIST_H_SITE do?
- What is the default value for CODE_LIST_H_SITE?
- How do I configure CODE_LIST_H_SITE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_SITE |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_SITE'
```
