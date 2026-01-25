# APPROVAL_INCLUDE_FIELDS - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated list of fields from xxreq_mstr and xxreqd_det tables.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_INCLUDE_FIELDS |
| **Category** | Approval Workflow |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_INCLUDE_FIELDS'
```

### Related Settings

- [APPROVAL_EMAIL_REPLY_TO](APPROVAL_EMAIL_REPLY_TO.md)
- [APPROVAL_METRICS_RED](APPROVAL_METRICS_RED.md)
- [APPROVAL_METRICS_YELLOW](APPROVAL_METRICS_YELLOW.md)
