# RECEIPT_EMAIL_MESSAGE - iPurchase System Setting

**Category:** Email Configuration

Custom message text for receipt notification emails.

**Common questions this answers:**
- What is RECEIPT_EMAIL_MESSAGE?
- What does RECEIPT_EMAIL_MESSAGE do?
- What is the default value for RECEIPT_EMAIL_MESSAGE?
- How do I configure RECEIPT_EMAIL_MESSAGE?
- How does RECEIPT_EMAIL_MESSAGE affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_MESSAGE |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_MESSAGE'
```
