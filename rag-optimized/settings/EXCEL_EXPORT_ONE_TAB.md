# EXCEL_EXPORT_ONE_TAB - iPurchase System Setting

**Category:** Reporting & Inquiry

Will export a consolidated view of the requisition when the Excel link is clicked in Requisition Inquiry. Default FALSE

### How It Works

See the description above for valid values and usage.

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
