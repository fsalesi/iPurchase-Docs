# EXCEL_EXPORT_APPROVALS - iPurchase System Setting

**Category:** System Configuration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | allows exporting approval data to Excel format |
| **FALSE** | Disables this feature |

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EXCEL_EXPORT_APPROVALS |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EXCEL_EXPORT_APPROVALS'
```