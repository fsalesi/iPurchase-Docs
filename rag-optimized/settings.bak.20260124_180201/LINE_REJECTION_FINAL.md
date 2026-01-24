# LINE_REJECTION_FINAL - iPurchase System Setting

**Category:** Uncategorized

If USE_LINE_APPROVALS = TRUE then you can also set whether or not any items which were previously rejected, can be re-approved by a subsequent approver. A value of TRUE will disallow anyone from ap...

**Common questions this answers:**
- What is LINE_REJECTION_FINAL?
- What does LINE_REJECTION_FINAL do?
- What is the default value for LINE_REJECTION_FINAL?
- How do I configure LINE_REJECTION_FINAL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LINE_REJECTION_FINAL |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LINE_REJECTION_FINAL'
```
