# PO_PRINTER_BATCH_NAME - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to set the Queue that the report will be processed on.  ex: "POPrint" QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Na...

**Common questions this answers:**
- What is PO_PRINTER_BATCH_NAME?
- What does PO_PRINTER_BATCH_NAME do?
- What is the default value for PO_PRINTER_BATCH_NAME?
- How do I configure PO_PRINTER_BATCH_NAME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_BATCH_NAME |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | QADSVC |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_BATCH_NAME'
```
