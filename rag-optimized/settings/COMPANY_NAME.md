# COMPANY_NAME - iPurchase System Setting

**Category:** System Configuration

Company name displayed on reports, purchase orders, and printed documents.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COMPANY_NAME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COMPANY_NAME'
```
