# DEFAULT_REQTYPE - iPurchase System Setting

**Category:** System Configuration

In this setting the administrator can set the default value for "Requisition Type" field.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_REQTYPE |
| **Category** | System Configuration |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_REQTYPE'
```

### Related Settings

- [DEFAULT_ACCT](DEFAULT_ACCT.md)
- [DEFAULT_BILLTO](DEFAULT_BILLTO.md)
- [DEFAULT_BLANKET_CYCLE](DEFAULT_BLANKET_CYCLE.md)