# CODE_LIST_REJECTION_CODES - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Rejection Code selection list and validation. A value of blank or a non-existing setting will turn...

**Common questions this answers:**
- What is CODE_LIST_REJECTION_CODES?
- What does CODE_LIST_REJECTION_CODES do?
- What is the default value for CODE_LIST_REJECTION_CODES?
- How do I configure CODE_LIST_REJECTION_CODES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_REJECTION_CODES |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Power Users |
| **Default Value** | List:001:Invalid Prices,002:Invalid Accounts |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_REJECTION_CODES'
```
