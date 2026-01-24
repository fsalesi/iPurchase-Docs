# PRINT_COMMAND - iPurchase System Setting

**Category:** System Configuration

OS command for printing documents (e.g., lp, lpr).

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PRINT_COMMAND |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PRINT_COMMAND'
```
