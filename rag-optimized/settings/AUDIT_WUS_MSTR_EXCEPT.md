# AUDIT_WUS_MSTR_EXCEPT - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify   The list of fields from the wus_mstr table will not be audited when changed. All other fields will show up in Audit when changed.

### How It Works

See the description above for details on how this setting affects system behavior.

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