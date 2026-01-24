# ACH_ARCHIVE_FOLDER - iPurchase System Setting

**Category:** ACH Integration

Directory path on application server. Archive folder where processed ACH files are moved after being polled and processed. Used in job_iaach_poller.p. Related: ACH_POLLING_FOLDER

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACH_ARCHIVE_FOLDER |
| **Category** | ACH Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACH_ARCHIVE_FOLDER'
```
