# CATALOG_PO_DIFFERENCE - iPurchase System Setting

**Category:** Purchase Orders

Possible Values: Blank, Punchout, Catalog, Lowest.  During a punchout, if an item ordered via a punchout site also exists in the catalog, do you want to use the Catalog's price rather than the price returned from the punchout?

### How It Works

See the description above for valid values and usage.

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
