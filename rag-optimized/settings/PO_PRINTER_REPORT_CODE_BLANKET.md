# PO_PRINTER_REPORT_CODE_BLANKET - iPurchase System Setting

**Category:** Purchase Orders

Report code used for printing blanket purchase orders.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_REPORT_CODE_BLANKET |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_REPORT_CODE_BLANKET'
```
