# QAD_COMMENT_TYPE - iPurchase System Setting

**Category:** QAD Integration

This is the comment type to be used when creating PO Header and PO Line comments.

### How It Works

This setting configures qad integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_COMMENT_TYPE |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | IP |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_COMMENT_TYPE'
```

### Related Settings

- [QAD_INTERFACE_PASSWORD](QAD_INTERFACE_PASSWORD.md)
- [QAD_REQUESTED_BY](QAD_REQUESTED_BY.md)
