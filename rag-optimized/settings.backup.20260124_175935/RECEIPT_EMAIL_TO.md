# RECEIPT_EMAIL_TO - iPurchase System Setting

**Category:** Email Configuration

Email addresses for receipt notifications.

**Common questions this answers:**
- What is RECEIPT_EMAIL_TO?
- What does RECEIPT_EMAIL_TO do?
- What is the default value for RECEIPT_EMAIL_TO?
- How do I configure RECEIPT_EMAIL_TO?
- How does RECEIPT_EMAIL_TO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_TO |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_TO'
```
