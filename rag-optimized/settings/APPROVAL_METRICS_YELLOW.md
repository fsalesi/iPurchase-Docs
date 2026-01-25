# APPROVAL_METRICS_YELLOW - iPurchase System Setting

**Category:** Approval Workflow

This setting allows the administrator to set how long the approval time should take before it will turn yellow on the approval metrics.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_METRICS_YELLOW |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 30 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_METRICS_YELLOW'
```

### Related Settings

- [APPROVAL_EMAIL_REPLY_TO](APPROVAL_EMAIL_REPLY_TO.md)
- [APPROVAL_INCLUDE_FIELDS](APPROVAL_INCLUDE_FIELDS.md)
- [APPROVAL_METRICS_RED](APPROVAL_METRICS_RED.md)