# EXCEL_EXPORT_ONE_TAB - iPurchase System Setting

**Category:** Reporting & Inquiry

Will export a consolidated view of the requisition when the Excel link is clicked in Requisition Inquiry.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures reporting & inquiry behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EXCEL_EXPORT_ONE_TAB |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EXCEL_EXPORT_ONE_TAB'
```

### Related Settings

- [EXCEL_EXPORT_FIELDS](EXCEL_EXPORT_FIELDS.md)