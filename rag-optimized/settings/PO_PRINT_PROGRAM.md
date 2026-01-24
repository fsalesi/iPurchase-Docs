# PO_PRINT_PROGRAM - iPurchase System Setting

**Category:** Purchase Orders

Progress program If you have a custom purchase order print program then enter the Progress program name here.

**Common questions this answers:**
- What is PO_PRINT_PROGRAM?
- What does PO_PRINT_PROGRAM do?
- What is the default value for PO_PRINT_PROGRAM?
- How do I configure PO_PRINT_PROGRAM?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_PROGRAM |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | us/po/poporp03.p |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_PROGRAM'
```
