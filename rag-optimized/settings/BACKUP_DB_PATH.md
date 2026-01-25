# BACKUP_DB_PATH - iPurchase System Setting

**Category:** Uncategorized

The location where database backups are stored

### How It Works

This setting configures uncategorized behavior in iPurchase.

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

### Related Settings

- [BACKUP_DB](BACKUP_DB.md)
- [BACKUP_DB_KEEP_DAYS](BACKUP_DB_KEEP_DAYS.md)