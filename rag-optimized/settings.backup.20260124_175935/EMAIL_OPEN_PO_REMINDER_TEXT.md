# EMAIL_OPEN_PO_REMINDER_TEXT - iPurchase System Setting

**Category:** Email Configuration



**Common questions this answers:**
- What is EMAIL_OPEN_PO_REMINDER_TEXT?
- What does EMAIL_OPEN_PO_REMINDER_TEXT do?
- What is the default value for EMAIL_OPEN_PO_REMINDER_TEXT?
- How do I configure EMAIL_OPEN_PO_REMINDER_TEXT?
- How does EMAIL_OPEN_PO_REMINDER_TEXT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_REMINDER_TEXT |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | Below is a list of your open purchase orders |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_REMINDER_TEXT'
```
