# SUPERVISOR_ESCALATION_LEVEL - iPurchase System Setting

**Category:** Approval Workflow

This setting determines how many supervisors up the supervisor tree (organization chart) are allowed to approve or reject a requisition.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_LEVEL |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 99 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_LEVEL'
```

### Related Settings

- [SUPERVISOR_APPROVAL_FIELD](SUPERVISOR_APPROVAL_FIELD.md)
- [SUPERVISOR_ESCALATION_ANYTIME](SUPERVISOR_ESCALATION_ANYTIME.md)
- [SUPERVISOR_ESCALATION_DAYS](SUPERVISOR_ESCALATION_DAYS.md)