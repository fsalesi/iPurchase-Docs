# QX_PO_VERSION - iPurchase System Setting

**Category:** Purchase Orders

Version of the qxtend PO method for this environment

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_PO_VERSION |
| **Category** | Purchase Orders |
| **Owner** |  |
| **Default Value** | eB2_3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_PO_VERSION'
```
