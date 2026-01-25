# AUDIT_TRAIL_[XXX] - iPurchase System Setting

**Category:** Uncategorized

There are several settings all beginning with "AUDIT_TRAIL".

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_[XXX] |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_[XXX]'
```

### Related Settings

- [AUDIT_TRAIL_ACTION_LIST](AUDIT_TRAIL_ACTION_LIST.md)
- [AUDIT_TRAIL_DOMAIN_EXEMPTION](AUDIT_TRAIL_DOMAIN_EXEMPTION.md)
- [AUDIT_TRAIL_TABLE_LABEL](AUDIT_TRAIL_TABLE_LABEL.md)