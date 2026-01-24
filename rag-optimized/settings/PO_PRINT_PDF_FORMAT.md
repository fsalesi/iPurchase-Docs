# PO_PRINT_PDF_FORMAT - iPurchase System Setting

**Category:** Purchase Orders

Prints the POs using the built in iPurchase look. Valid choices are GRAPHICAL and PLAIN. A value of PLAIN will simply take the text based QAD output and convert it to PDF.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_PDF_FORMAT |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | PLAIN |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_PDF_FORMAT'
```
