# CATALOG_PO_DIFFERENCE - iPurchase System Setting

**Category:** Purchase Orders

Possible Values: Blank, Punchout, Catalog, Lowest.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_PO_DIFFERENCE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | Lowest |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_PO_DIFFERENCE'
```