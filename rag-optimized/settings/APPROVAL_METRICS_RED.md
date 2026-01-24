# APPROVAL_METRICS_RED - iPurchase System Setting

**Category:** Approval Workflow

This setting allows the administrator to set how long the approval time should take before it will turn red on the approval metrics.  MINUTES

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_METRICS_RED |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 90 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_METRICS_RED'
```
