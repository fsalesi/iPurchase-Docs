# PO_PRINT_ARCHIVE_IN_DB - iPurchase System Setting

**Category:** Purchase Orders

Store Purchase Order PDF files in database. A setting of true will display a clock icon next to Purchase Order numbers in iPurchase. Clicking the clock icon will display a list of all original prints for the given Purchase Order.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_ARCHIVE_IN_DB |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_ARCHIVE_IN_DB'
```