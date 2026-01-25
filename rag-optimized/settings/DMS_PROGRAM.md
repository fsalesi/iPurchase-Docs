# DMS_PROGRAM - iPurchase System Setting

**Category:** Uncategorized

This is the name of the Progress Program which integrates with a document management system.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DMS_PROGRAM |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DMS_PROGRAM'
```