# USER_IMPORT_FOLDER - iPurchase System Setting

**Category:** User Management

Directory path on application server. Folder where user import files are placed for processing.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_IMPORT_FOLDER |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_IMPORT_FOLDER'
```