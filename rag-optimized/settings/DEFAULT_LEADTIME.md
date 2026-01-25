# DEFAULT_LEADTIME - iPurchase System Setting

**Category:** System Configuration

This setting will set the number of days to add to today's date in order to calculate the Need Date on the requisition header.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_LEADTIME |
| **Category** | System Configuration |
| **Owner** | Purchasing |
| **Default Value** | 0 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_LEADTIME'
```

### Related Settings

- [DEFAULT_ACCT](DEFAULT_ACCT.md)
- [DEFAULT_BILLTO](DEFAULT_BILLTO.md)
- [DEFAULT_BLANKET_CYCLE](DEFAULT_BLANKET_CYCLE.md)