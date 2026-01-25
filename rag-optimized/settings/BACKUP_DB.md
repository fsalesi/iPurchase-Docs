# BACKUP_DB - iPurchase System Setting

**Category:** Uncategorized

iPurchase provides a rudimentary backup system.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | ../db/ipurchase.db |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB'
```

### Related Settings

- [BACKUP_DB_KEEP_DAYS](BACKUP_DB_KEEP_DAYS.md)
- [BACKUP_DB_PATH](BACKUP_DB_PATH.md)
