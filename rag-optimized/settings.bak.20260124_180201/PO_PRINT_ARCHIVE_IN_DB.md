# PO_PRINT_ARCHIVE_IN_DB - iPurchase System Setting

**Category:** Purchase Orders

Store Purchase Order PDF files in database. A setting of true will display a clock icon next to Purchase Order numbers in iPurchase. Clicking the clock icon will display a list of all original prin...

**Common questions this answers:**
- What is PO_PRINT_ARCHIVE_IN_DB?
- What does PO_PRINT_ARCHIVE_IN_DB do?
- What is the default value for PO_PRINT_ARCHIVE_IN_DB?
- How do I configure PO_PRINT_ARCHIVE_IN_DB?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_ARCHIVE_IN_DB |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_ARCHIVE_IN_DB'
```
