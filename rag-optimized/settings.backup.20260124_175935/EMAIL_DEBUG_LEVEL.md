# EMAIL_DEBUG_LEVEL - iPurchase System Setting

**Category:** Email Configuration

Numeric 0-3. Email system debug verbosity. 0=off, 1=basic, 2=detailed, 3=verbose. Used for troubleshooting email issues.

**Common questions this answers:**
- What is EMAIL_DEBUG_LEVEL?
- What does EMAIL_DEBUG_LEVEL do?
- What is the default value for EMAIL_DEBUG_LEVEL?
- How do I configure EMAIL_DEBUG_LEVEL?
- How does EMAIL_DEBUG_LEVEL affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_DEBUG_LEVEL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 0 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_DEBUG_LEVEL'
```
