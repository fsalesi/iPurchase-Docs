# SUPERVISOR_ESCALATION_LEVEL - iPurchase System Setting

**Category:** Approval Workflow

This setting determines how many supervisors up the supervisor tree (organization chart) are allowed to approve or reject a requisition. A value of one will only allow the approver's immediate supe...

**Common questions this answers:**
- What is SUPERVISOR_ESCALATION_LEVEL?
- What does SUPERVISOR_ESCALATION_LEVEL do?
- What is the default value for SUPERVISOR_ESCALATION_LEVEL?
- How do I configure SUPERVISOR_ESCALATION_LEVEL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_LEVEL |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 99 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_LEVEL'
```

**Related settings:** SUPERVISOR_ESCALATION_DAYS, ALLOW_SUPERVISORS_TO_APPROVE