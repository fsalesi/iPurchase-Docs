# DEFAULT_BILLTO - iPurchase System Setting

**Category:** System Configuration

The administrator can enter a default value for the "Bill To" field.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BILLTO |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BILLTO'
```

### Related Settings

- [DEFAULT_ACCT](DEFAULT_ACCT.md)
- [DEFAULT_BLANKET_CYCLE](DEFAULT_BLANKET_CYCLE.md)
- [DEFAULT_CC](DEFAULT_CC.md)
