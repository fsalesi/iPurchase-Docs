# EMAIL_OPEN_PO_REMINDER_SUBJECT - iPurchase System Setting

**Category:** Email Configuration



**Common questions this answers:**
- What is EMAIL_OPEN_PO_REMINDER_SUBJECT?
- What does EMAIL_OPEN_PO_REMINDER_SUBJECT do?
- What is the default value for EMAIL_OPEN_PO_REMINDER_SUBJECT?
- How do I configure EMAIL_OPEN_PO_REMINDER_SUBJECT?
- How does EMAIL_OPEN_PO_REMINDER_SUBJECT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_REMINDER_SUBJECT |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | Open POs in IPurchase |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_REMINDER_SUBJECT'
```
