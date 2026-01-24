# RECEIPT_EMAIL_REQ_TYPES - iPurchase System Setting

**Category:** Email Configuration

Comma-separated req types. Types that trigger receipt emails.

**Common questions this answers:**
- What is RECEIPT_EMAIL_REQ_TYPES?
- What does RECEIPT_EMAIL_REQ_TYPES do?
- What is the default value for RECEIPT_EMAIL_REQ_TYPES?
- How do I configure RECEIPT_EMAIL_REQ_TYPES?
- How does RECEIPT_EMAIL_REQ_TYPES affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_REQ_TYPES |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_REQ_TYPES'
```
