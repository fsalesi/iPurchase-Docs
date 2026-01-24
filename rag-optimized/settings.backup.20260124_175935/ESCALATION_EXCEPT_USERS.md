# ESCALATION_EXCEPT_USERS - iPurchase System Setting

**Category:** Approval Workflow

Can-Do list. Users/groups exempt from approval escalation timeouts. Their pending approvals won't escalate.

**Common questions this answers:**
- What is ESCALATION_EXCEPT_USERS?
- What does ESCALATION_EXCEPT_USERS do?
- What is the default value for ESCALATION_EXCEPT_USERS?
- How do I configure ESCALATION_EXCEPT_USERS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ESCALATION_EXCEPT_USERS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ESCALATION_EXCEPT_USERS'
```
