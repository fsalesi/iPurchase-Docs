# PUNCHOUT_REQ_TYPE_[supplier] - iPurchase System Setting

**Category:** Catalog & Vendors

This setting allows the administrator to set a default requisition type by supplier for punchout requisitions.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_REQ_TYPE_[supplier] |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_REQ_TYPE_[supplier]'
```

### Related Settings

- [PUNCHOUT_DISABLE_USERS](PUNCHOUT_DISABLE_USERS.md)
- [PUNCHOUT_LEADTIME](PUNCHOUT_LEADTIME.md)
- [PUNCHOUT_NOFRAMES](PUNCHOUT_NOFRAMES.md)