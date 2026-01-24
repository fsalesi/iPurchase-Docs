# BACKUP_DB_PATH - iPurchase System Setting

**Category:** Uncategorized

The location where database backups are stored

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB_PATH |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | ../dbbackups |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB_PATH'
```
