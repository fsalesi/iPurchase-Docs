# BG_COLOR_TEST - iPurchase System Setting

**Category:** Uncategorized

The background color of the Archive System - default pink

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BG_COLOR_TEST |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | #d9f2e5 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BG_COLOR_TEST'
```

### Related Settings

- [BG_COLOR_ARCHIVE](BG_COLOR_ARCHIVE.md)
