# SUPPLIER_PO_MERGE_ATTACHMENTS - iPurchase System Setting

**Category:** Purchase Orders

This setting is where the filename, with the full path to the pdf file or a space delimited list of pdf files that are to be merged in to the PO PDF file which is printed. If you're on windows then...

**Common questions this answers:**
- What is SUPPLIER_PO_MERGE_ATTACHMENTS?
- What does SUPPLIER_PO_MERGE_ATTACHMENTS do?
- What is the default value for SUPPLIER_PO_MERGE_ATTACHMENTS?
- How do I configure SUPPLIER_PO_MERGE_ATTACHMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_MERGE_ATTACHMENTS |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_MERGE_ATTACHMENTS'
```
