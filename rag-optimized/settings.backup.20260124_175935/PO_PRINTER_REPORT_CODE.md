# PO_PRINTER_REPORT_CODE - iPurchase System Setting

**Category:** Purchase Orders

This setting holds the report code for the print version you are using. ex: Custom_PurchaseOrderPrint. QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names Q...

**Common questions this answers:**
- What is PO_PRINTER_REPORT_CODE?
- What does PO_PRINTER_REPORT_CODE do?
- What is the default value for PO_PRINTER_REPORT_CODE?
- How do I configure PO_PRINTER_REPORT_CODE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_REPORT_CODE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | PurchaseOrderPrint  |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_REPORT_CODE'
```
