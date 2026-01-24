# EA_EXPORT_FOLDER - iPurchase System Setting

**Category:** System Configuration

Directory path on application server. Folder where Enterprise Analytics export files are written.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EA_EXPORT_FOLDER |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EA_EXPORT_FOLDER'
```