# SUPERVISOR_ESCALATION_DAYS - iPurchase System Setting

**Category:** Approval Workflow

This is the number of days which must elapse before an approver can Approve or Reject a requisition on behalf of someone else who reports to this given supervisor.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_DAYS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_DAYS'
```

### Related Settings

- [SUPERVISOR_APPROVAL_FIELD](SUPERVISOR_APPROVAL_FIELD.md)
- [SUPERVISOR_ESCALATION_ANYTIME](SUPERVISOR_ESCALATION_ANYTIME.md)
- [SUPERVISOR_ESCALATION_LEVEL](SUPERVISOR_ESCALATION_LEVEL.md)