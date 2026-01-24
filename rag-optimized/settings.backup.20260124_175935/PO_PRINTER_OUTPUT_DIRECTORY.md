# PO_PRINTER_OUTPUT_DIRECTORY - iPurchase System Setting

**Category:** Purchase Orders

Is a directory on the iPurchase application server where the QAD Reporting Framework will save the file. If you are using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the n...

**Common questions this answers:**
- What is PO_PRINTER_OUTPUT_DIRECTORY?
- What does PO_PRINTER_OUTPUT_DIRECTORY do?
- What is the default value for PO_PRINTER_OUTPUT_DIRECTORY?
- How do I configure PO_PRINTER_OUTPUT_DIRECTORY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_OUTPUT_DIRECTORY |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_OUTPUT_DIRECTORY'
```
