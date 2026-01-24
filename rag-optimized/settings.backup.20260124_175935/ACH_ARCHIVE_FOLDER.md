# ACH_ARCHIVE_FOLDER - iPurchase System Setting

**Category:** ACH Integration

Directory path on application server. Archive folder where processed ACH files are moved after being polled and processed. Used in job_iaach_poller.p. Related: ACH_POLLING_FOLDER

**Common questions this answers:**
- What is ACH_ARCHIVE_FOLDER?
- What does ACH_ARCHIVE_FOLDER do?
- What is the default value for ACH_ARCHIVE_FOLDER?
- How do I configure ACH_ARCHIVE_FOLDER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACH_ARCHIVE_FOLDER |
| **Category** | ACH Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACH_ARCHIVE_FOLDER'
```
