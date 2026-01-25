# AUTO_RECEIVE_TIME - iPurchase System Setting

**Category:** Receiving

Time value.

### How It Works

This setting configures receiving behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_RECEIVE_TIME |
| **Category** | Receiving |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_RECEIVE_TIME'
```

### Related Settings

- [AUTO_RECEIVE](AUTO_RECEIVE.md)