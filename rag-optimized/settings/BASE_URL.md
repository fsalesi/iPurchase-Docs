# BASE_URL - iPurchase System Setting

**Category:** Email Configuration

Base URL/hostname (e.g., https://server.company.com). Used in email notifications and scheduled job links. Should be updated on test/backup systems.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BASE_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BASE_URL'
```