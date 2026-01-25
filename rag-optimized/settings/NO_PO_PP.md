# NO_PO_PP - iPurchase System Setting

**Category:** Purchase Orders

Technical - Do Not Modify without consulting ISS

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PO_PP |
| **Category** | Purchase Orders |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PO_PP'
```