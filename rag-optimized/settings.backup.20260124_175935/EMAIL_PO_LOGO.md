# EMAIL_PO_LOGO - iPurchase System Setting

**Category:** Email Configuration

Image URL or file path. Company logo displayed in purchase order emails.

**Common questions this answers:**
- What is EMAIL_PO_LOGO?
- What does EMAIL_PO_LOGO do?
- What is the default value for EMAIL_PO_LOGO?
- How do I configure EMAIL_PO_LOGO?
- How does EMAIL_PO_LOGO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_LOGO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_LOGO'
```
