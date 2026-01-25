# INQUIRY_REFRESH_SECONDS - iPurchase System Setting

**Category:** Reporting & Inquiry

How often the system automatically refreshes the inquiry screen in seconds.

### How It Works

This setting configures reporting & inquiry behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_REFRESH_SECONDS |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | 120 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_REFRESH_SECONDS'
```

### Related Settings

- [INQUIRY_AFTER_REJECT](INQUIRY_AFTER_REJECT.md)
- [INQUIRY_LAST_REV_DEFAULT](INQUIRY_LAST_REV_DEFAULT.md)
- [INQUIRY_NOTES_MATCHES](INQUIRY_NOTES_MATCHES.md)
