# EMAILS_TO - iPurchase System Setting

**Category:** Email Configuration

Comma-separated email address(s) where all emails from the service will be sent to. This overrides the actual user's email addresses.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILS_TO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILS_TO'
```
