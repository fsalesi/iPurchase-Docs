# PO_PRINTER_BATCH_NAME - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to set the Queue that the report will be processed on.  ex: "POPrint" QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names QAD user. Settings QAD_AUTHENTICATION_USER and QAD_AUTHENTICATION_PASSWORD must be set. The user specified in QAD_AUTHENTICATION_USER must be setup in QAD with a role of "rptAdmin"

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_BATCH_NAME |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | QADSVC |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_BATCH_NAME'
```
