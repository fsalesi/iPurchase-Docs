# MESSAGE_WARNING_TIMEOUT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator the ability to set the duration of how long the warning message will stay on the screen.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MESSAGE_WARNING_TIMEOUT |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | 5 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MESSAGE_WARNING_TIMEOUT'
```

### Related Settings

- [MESSAGE_ERROR_TIMEOUT](MESSAGE_ERROR_TIMEOUT.md)