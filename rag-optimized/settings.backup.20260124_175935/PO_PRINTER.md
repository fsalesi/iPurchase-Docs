# PO_PRINTER - iPurchase System Setting

**Category:** Purchase Orders

Printer name defined in QAD. If you're using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the name of the printer here, otherwise leave blank.

**Common questions this answers:**
- What is PO_PRINTER?
- What does PO_PRINTER do?
- What is the default value for PO_PRINTER?
- How do I configure PO_PRINTER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER'
```
