# LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

A comma separated list of User ID's or Group ID's that will always be logged into their pending queue, regardless of whether they do or do not have pending requisition to approve. Asterisk indicate...

**Common questions this answers:**
- What is LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS?
- What does LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS do?
- What is the default value for LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS?
- How do I configure LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS?
- How does LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS'
```
