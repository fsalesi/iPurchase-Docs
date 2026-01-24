# AUDIT_TRAIL_DOMAIN_EXEMPTION - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_DOMAIN_EXEMPTION |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | pf_mstr,wus_mstr,wgr_mstr,wugr_mstr |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_DOMAIN_EXEMPTION'
```
