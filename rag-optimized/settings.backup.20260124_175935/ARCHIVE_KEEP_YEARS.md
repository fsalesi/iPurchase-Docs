# ARCHIVE_KEEP_YEARS - iPurchase System Setting

**Category:** GL Accounts & Finance

The number of years to keep requisitions. Note: Pending Requisitions can't be archived.

**Common questions this answers:**
- What is ARCHIVE_KEEP_YEARS?
- What does ARCHIVE_KEEP_YEARS do?
- What is the default value for ARCHIVE_KEEP_YEARS?
- How do I configure ARCHIVE_KEEP_YEARS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ARCHIVE_KEEP_YEARS |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ARCHIVE_KEEP_YEARS'
```
