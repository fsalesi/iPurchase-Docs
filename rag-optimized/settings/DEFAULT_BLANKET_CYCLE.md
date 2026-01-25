# DEFAULT_BLANKET_CYCLE - iPurchase System Setting

**Category:** System Configuration

After the administrator has added values to the CODE_LIST_H_BLANKET_CYCLE setting, they can add one of the values in that setting to this setting, to be the default value for the cycle code drop down menu on the blanket information tab on a requisition.

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BLANKET_CYCLE |
| **Category** | System Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BLANKET_CYCLE'
```

### Related Settings

- [DEFAULT_ACCT](DEFAULT_ACCT.md)
- [DEFAULT_BILLTO](DEFAULT_BILLTO.md)
- [DEFAULT_CC](DEFAULT_CC.md)
