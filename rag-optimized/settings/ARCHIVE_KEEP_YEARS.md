# ARCHIVE_KEEP_YEARS - iPurchase System Setting

**Category:** GL Accounts & Finance

The number of years to keep requisitions.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ARCHIVE_KEEP_YEARS |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ARCHIVE_KEEP_YEARS'
```