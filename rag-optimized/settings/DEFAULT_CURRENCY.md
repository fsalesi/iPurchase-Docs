# DEFAULT_CURRENCY - iPurchase System Setting

**Category:** System Configuration

The administrator can set a default currency for iPurchase.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_CURRENCY |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_CURRENCY'
```

### Related Settings

- [DEFAULT_ACCT](DEFAULT_ACCT.md)
- [DEFAULT_BILLTO](DEFAULT_BILLTO.md)
- [DEFAULT_BLANKET_CYCLE](DEFAULT_BLANKET_CYCLE.md)
