# RECEIPT_EMAIL_SUBJECT - iPurchase System Setting

**Category:** Email Configuration

Email subject for receipt notifications.

**Common questions this answers:**
- What is RECEIPT_EMAIL_SUBJECT?
- What does RECEIPT_EMAIL_SUBJECT do?
- What is the default value for RECEIPT_EMAIL_SUBJECT?
- How do I configure RECEIPT_EMAIL_SUBJECT?
- How does RECEIPT_EMAIL_SUBJECT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_SUBJECT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | Receipt Notification |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_SUBJECT'
```
