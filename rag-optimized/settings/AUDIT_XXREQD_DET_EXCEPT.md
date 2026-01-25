# AUDIT_XXREQD_DET_EXCEPT - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_XXREQD_DET_EXCEPT |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | xxreqd_master_comments, |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_XXREQD_DET_EXCEPT'
```

### Related Settings

- [AUDIT_TRAIL_ACTION_LIST](AUDIT_TRAIL_ACTION_LIST.md)
- [AUDIT_TRAIL_DOMAIN_EXEMPTION](AUDIT_TRAIL_DOMAIN_EXEMPTION.md)
- [AUDIT_TRAIL_TABLE_LABEL](AUDIT_TRAIL_TABLE_LABEL.md)
