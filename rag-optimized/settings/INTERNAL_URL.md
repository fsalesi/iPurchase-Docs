# INTERNAL_URL - iPurchase System Setting

**Category:** Email Configuration

Internal network URL for application.

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INTERNAL_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INTERNAL_URL'
```