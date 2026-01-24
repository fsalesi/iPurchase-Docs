# AUDIT_XXREQD_DET_EXCEPT - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

### How It Works

See the description above for details on how this setting affects system behavior.

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