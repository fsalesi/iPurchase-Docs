# ACH_ARCHIVE_FOLDER - iPurchase System Setting

**Category:** ACH Integration

Directory path on application server.

### How It Works

This setting configures ach integration behavior in iPurchase.

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

### Related Settings

- [ACH_POLLING_FOLDER](ACH_POLLING_FOLDER.md)