# CODE_LIST_H_CREDIT_TERMS - iPurchase System Setting

**Category:** System Configuration

LIST format. Dropdown values for credit terms. Format: LIST:code:description,code:description

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_CREDIT_TERMS |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_CREDIT_TERMS'
```
