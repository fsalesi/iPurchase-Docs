# EMAIL_PO_ADDITIONAL - iPurchase System Setting

**Category:** Email Configuration

Comma-separated email addresses. Additional recipients for purchase order emails beyond default recipients.

**Common questions this answers:**
- What is EMAIL_PO_ADDITIONAL?
- What does EMAIL_PO_ADDITIONAL do?
- What is the default value for EMAIL_PO_ADDITIONAL?
- How do I configure EMAIL_PO_ADDITIONAL?
- How does EMAIL_PO_ADDITIONAL affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_ADDITIONAL |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_ADDITIONAL'
```
