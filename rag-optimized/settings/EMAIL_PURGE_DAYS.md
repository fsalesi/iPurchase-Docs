# EMAIL_PURGE_DAYS - iPurchase System Setting

**Category:** Email Configuration

How often iPurchase will purge emails that have error-ed . Value is in days.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PURGE_DAYS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 30 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PURGE_DAYS'
```
