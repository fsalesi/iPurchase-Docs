# RECEIPT_EMAIL_USERS - iPurchase System Setting

**Category:** Email Configuration

Can-Do list. Users who receive receipt notification emails.

**Common questions this answers:**
- What is RECEIPT_EMAIL_USERS?
- What does RECEIPT_EMAIL_USERS do?
- What is the default value for RECEIPT_EMAIL_USERS?
- How do I configure RECEIPT_EMAIL_USERS?
- How does RECEIPT_EMAIL_USERS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_USERS |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_USERS'
```
