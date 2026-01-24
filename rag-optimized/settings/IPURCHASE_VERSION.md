# IPURCHASE_VERSION - iPurchase System Setting

**Category:** Uncategorized

Do Not Modify

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IPURCHASE_VERSION |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | 2023.0426 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IPURCHASE_VERSION'
```