# EA_EXPORT_FOLDER - iPurchase System Setting

**Category:** System Configuration

Directory path on application server.

### How It Works

This setting configures system configuration behavior in iPurchase.

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