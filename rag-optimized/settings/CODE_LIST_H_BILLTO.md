# CODE_LIST_H_BILLTO - iPurchase System Setting

**Category:** Code Lists & Dropdowns

This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Bill To selection list and validation.  Leaving this value blank will tell iPurchase to use the si_mstr ...

**Common questions this answers:**
- What is CODE_LIST_H_BILLTO?
- What does CODE_LIST_H_BILLTO do?
- What is the default value for CODE_LIST_H_BILLTO?
- How do I configure CODE_LIST_H_BILLTO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_BILLTO |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_BILLTO'
```
