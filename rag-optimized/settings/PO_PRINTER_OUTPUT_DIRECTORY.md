# PO_PRINTER_OUTPUT_DIRECTORY - iPurchase System Setting

**Category:** Purchase Orders

Is a directory on the iPurchase application server where the QAD Reporting Framework will save the file. If you are using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the name of the directory where pdf files will be placed by the third-party forms package, otherwise leave blank. QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names QAD user. Settings QAD_AUTHENTICATION_USER and QAD_AUTHENTICATION_PASSWORD must be set. The user specified in QAD_AUTHENTICATION_USER must be setup in QAD with a role of "rptAdmin"

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_OUTPUT_DIRECTORY |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_OUTPUT_DIRECTORY'
```
