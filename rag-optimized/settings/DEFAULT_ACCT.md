# DEFAULT_ACCT - iPurchase System Setting

**Category:** System Configuration

The Default Account is used when creating requisition from catalogs and punchouts.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_ACCT |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_ACCT'
```

### Related Settings

- [DEFAULT_BILLTO](DEFAULT_BILLTO.md)
- [DEFAULT_BLANKET_CYCLE](DEFAULT_BLANKET_CYCLE.md)
- [DEFAULT_CC](DEFAULT_CC.md)
