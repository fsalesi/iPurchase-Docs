# EMAIL_PO_BODY_REVISION - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for PO revision emails.

**Common questions this answers:**
- What is EMAIL_PO_BODY_REVISION?
- What does EMAIL_PO_BODY_REVISION do?
- What is the default value for EMAIL_PO_BODY_REVISION?
- How do I configure EMAIL_PO_BODY_REVISION?
- How does EMAIL_PO_BODY_REVISION affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY_REVISION |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY_REVISION'
```
