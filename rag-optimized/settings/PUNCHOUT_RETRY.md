# PUNCHOUT_RETRY - iPurchase System Setting

**Category:** Catalog & Vendors

Numeric.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_RETRY |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_RETRY'
```

### Related Settings

- [PUNCHOUT_DISABLE_USERS](PUNCHOUT_DISABLE_USERS.md)
- [PUNCHOUT_LEADTIME](PUNCHOUT_LEADTIME.md)
- [PUNCHOUT_NOFRAMES](PUNCHOUT_NOFRAMES.md)
