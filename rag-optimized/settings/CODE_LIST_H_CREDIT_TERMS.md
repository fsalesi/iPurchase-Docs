# CODE_LIST_H_CREDIT_TERMS - iPurchase System Setting

**Category:** System Configuration

LIST format.

### How It Works

This setting configures system configuration behavior in iPurchase.

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