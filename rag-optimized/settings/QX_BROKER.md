# QX_BROKER - iPurchase System Setting

**Category:** Qxtend Integration

Qxtend broker server address for Qxtend integration.

### How It Works

This setting configures qxtend integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_BROKER |
| **Category** | Qxtend Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_BROKER'
```

### Related Settings

- [QX_CODEPAGE](QX_CODEPAGE.md)
- [QX_URL](QX_URL.md)
- [QX_VERSION](QX_VERSION.md)