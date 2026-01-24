# DATE_FORMAT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator to globally change the format of the date fields in iPurchase.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DATE_FORMAT |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | mdy |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DATE_FORMAT'
```
