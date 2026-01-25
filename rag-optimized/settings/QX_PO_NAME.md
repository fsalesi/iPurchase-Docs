# QX_PO_NAME - iPurchase System Setting

**Category:** Purchase Orders

Name of the qxtend instance for Purchase Orders in this environment

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_PO_NAME |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | QADERP |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_PO_NAME'
```

### Related Settings

- [QX_PO_VERSION](QX_PO_VERSION.md)