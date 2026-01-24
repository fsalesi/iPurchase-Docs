# ACH_POLLING_FOLDER - iPurchase System Setting

**Category:** ACH Integration

Directory path on application server. Folder where incoming ACH files (*.txt) are placed for processing by the ACH polling job. Processed files are moved to ACH_ARCHIVE_FOLDER. Used in job_iaach_po...

**Common questions this answers:**
- What is ACH_POLLING_FOLDER?
- What does ACH_POLLING_FOLDER do?
- What is the default value for ACH_POLLING_FOLDER?
- How do I configure ACH_POLLING_FOLDER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACH_POLLING_FOLDER |
| **Category** | ACH Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACH_POLLING_FOLDER'
```
