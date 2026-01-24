# SUPERVISOR_ESCALATION_DAYS - iPurchase System Setting

**Category:** Approval Workflow

This is the number of days which must elapse before an approver can Approve or Reject a requisition on behalf of someone else who reports to this given supervisor. See SUPERVISOR_ESCALATION_LEVEL a...

**Common questions this answers:**
- What is SUPERVISOR_ESCALATION_DAYS?
- What does SUPERVISOR_ESCALATION_DAYS do?
- What is the default value for SUPERVISOR_ESCALATION_DAYS?
- How do I configure SUPERVISOR_ESCALATION_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_DAYS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_DAYS'
```

**Related settings:** SUPERVISOR_ESCALATION_LEVEL, ALLOW_SUPERVISORS_TO_APPROVE