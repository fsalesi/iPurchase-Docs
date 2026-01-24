# PO_PRINTER_OUTPUT_DIRECTORY_BLANKET - iPurchase System Setting

**Category:** Purchase Orders

Directory path. Output folder for blanket purchase order print files.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_OUTPUT_DIRECTORY_BLANKET |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_OUTPUT_DIRECTORY_BLANKET'
```