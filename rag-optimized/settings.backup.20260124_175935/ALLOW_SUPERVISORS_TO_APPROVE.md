# ALLOW_SUPERVISORS_TO_APPROVE - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that are allowed to approve for a subordinate. Asterisk indicates everyone, a blank indicates no one. This setting allows a supervisor to Approve or ...

**Common questions this answers:**
- What is ALLOW_SUPERVISORS_TO_APPROVE?
- What does ALLOW_SUPERVISORS_TO_APPROVE do?
- What is the default value for ALLOW_SUPERVISORS_TO_APPROVE?
- How do I configure ALLOW_SUPERVISORS_TO_APPROVE?
- How does ALLOW_SUPERVISORS_TO_APPROVE affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_SUPERVISORS_TO_APPROVE |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_SUPERVISORS_TO_APPROVE'
```

**Related settings:** USE_SUPERVISORS_TO_APPROVE, SUPERVISOR_ESCALATION_DAYS, SUPERVISOR_ESCALATION_LEVEL