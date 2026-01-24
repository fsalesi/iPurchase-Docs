# PO_PRINT_ARCHIVE_DIR - iPurchase System Setting

**Category:** Purchase Orders

Directory on application server. Enter the path to a directory on the application server where all purchase orders will be saved to when printing a revision through iPurchase for the first time. Th...

**Common questions this answers:**
- What is PO_PRINT_ARCHIVE_DIR?
- What does PO_PRINT_ARCHIVE_DIR do?
- What is the default value for PO_PRINT_ARCHIVE_DIR?
- How do I configure PO_PRINT_ARCHIVE_DIR?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_ARCHIVE_DIR |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_ARCHIVE_DIR'
```
