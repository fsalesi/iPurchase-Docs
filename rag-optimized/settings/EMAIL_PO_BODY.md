# EMAIL_PO_BODY - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for new PO.

**Common questions this answers:**
- What is EMAIL_PO_BODY?
- What does EMAIL_PO_BODY do?
- What is the default value for EMAIL_PO_BODY?
- How do I configure EMAIL_PO_BODY?
- How does EMAIL_PO_BODY affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | This should be line one. <br><br> |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY'
```
