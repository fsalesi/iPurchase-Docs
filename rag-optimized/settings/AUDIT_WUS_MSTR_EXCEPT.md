# AUDIT_WUS_MSTR_EXCEPT - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify   The list of fields from the wus_mstr table will not be audited when changed.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_WUS_MSTR_EXCEPT |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | wus_last_login |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_WUS_MSTR_EXCEPT'
```

### Related Settings

- [AUDIT_TRAIL_ACTION_LIST](AUDIT_TRAIL_ACTION_LIST.md)
- [AUDIT_TRAIL_DOMAIN_EXEMPTION](AUDIT_TRAIL_DOMAIN_EXEMPTION.md)
- [AUDIT_TRAIL_TABLE_LABEL](AUDIT_TRAIL_TABLE_LABEL.md)
