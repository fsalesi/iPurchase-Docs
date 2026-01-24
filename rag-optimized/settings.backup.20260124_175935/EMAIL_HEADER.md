# EMAIL_HEADER - iPurchase System Setting

**Category:** Email Configuration

HTML content. Custom header included in email templates. Used for branding/styling emails.

**Common questions this answers:**
- What is EMAIL_HEADER?
- What does EMAIL_HEADER do?
- What is the default value for EMAIL_HEADER?
- How do I configure EMAIL_HEADER?
- How does EMAIL_HEADER affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HEADER |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HEADER'
```
