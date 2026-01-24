# BACKUP_DB_PATH - iPurchase System Setting

**Category:** Uncategorized

The location where database backups are stored

**Common questions this answers:**
- What is BACKUP_DB_PATH?
- What does BACKUP_DB_PATH do?
- What is the default value for BACKUP_DB_PATH?
- How do I configure BACKUP_DB_PATH?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB_PATH |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | ../dbbackups |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB_PATH'
```
