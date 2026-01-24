# CODE_LIST_H_FOB - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header FOB selection list and validation. You can also use the prefix "LIST:" followed by a comma-...

**Common questions this answers:**
- What is CODE_LIST_H_FOB?
- What does CODE_LIST_H_FOB do?
- What is the default value for CODE_LIST_H_FOB?
- How do I configure CODE_LIST_H_FOB?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_FOB |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Finance |
| **Default Value** | po_fob |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_FOB'
```
