# EMAIL_HEADER - iPurchase System Setting

**Category:** Email Configuration

HTML content. Custom header included in email templates. Used for branding/styling emails.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HEADER |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HEADER'
```
