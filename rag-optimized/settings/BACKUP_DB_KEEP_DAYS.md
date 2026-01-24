# BACKUP_DB_KEEP_DAYS - iPurchase System Setting

**Category:** Uncategorized

How many days worth of iPurchase database backups to keep

**Common questions this answers:**
- What is BACKUP_DB_KEEP_DAYS?
- What does BACKUP_DB_KEEP_DAYS do?
- What is the default value for BACKUP_DB_KEEP_DAYS?
- How do I configure BACKUP_DB_KEEP_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB_KEEP_DAYS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | 7 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB_KEEP_DAYS'
```
