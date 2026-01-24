# APPLICATION_URL - iPurchase System Setting

**Category:** Email Configuration

Full application URL (e.g., https://ipurchase.company.com). Used by scheduled jobs for email links. On test/backup systems, should be updated to match environment.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPLICATION_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPLICATION_URL'
```
