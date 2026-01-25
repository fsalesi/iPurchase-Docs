# QAD_REQUESTED_BY - iPurchase System Setting

**Category:** QAD Integration

This setting will use OBO as the Requested By.

### How It Works

This setting configures qad integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_REQUESTED_BY |
| **Category** | QAD Integration |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_REQUESTED_BY'
```

### Related Settings

- [QAD_COMMENT_TYPE](QAD_COMMENT_TYPE.md)
- [QAD_INTERFACE_PASSWORD](QAD_INTERFACE_PASSWORD.md)