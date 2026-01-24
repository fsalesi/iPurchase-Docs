# AUDIT_TRAIL_TABLE_LIST - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_TABLE_LIST |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | ,xxreqd_det,xxreq_mstr,xxappfield,xxapprule,pf_mstr,wgr_mstr,wugr_mstr,wus_mstr |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_TABLE_LIST'
```