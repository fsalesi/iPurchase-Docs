# QX_PO_VERSION - iPurchase System Setting

**Category:** Purchase Orders

Version of the qxtend PO method for this environment

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_PO_VERSION |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | eB2_3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_PO_VERSION'
```

### Related Settings

- [QX_PO_NAME](QX_PO_NAME.md)