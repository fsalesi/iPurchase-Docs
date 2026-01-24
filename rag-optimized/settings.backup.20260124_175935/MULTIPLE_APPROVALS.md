# MULTIPLE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

When an approver or approval group appears in the approval routing more than once, which approval record is actually added to the routing. When KEEP_ALL is chosen then all approval records for the ...

**Common questions this answers:**
- What is MULTIPLE_APPROVALS?
- What does MULTIPLE_APPROVALS do?
- What is the default value for MULTIPLE_APPROVALS?
- How do I configure MULTIPLE_APPROVALS?
- How does MULTIPLE_APPROVALS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MULTIPLE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | KEEP_LAST |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MULTIPLE_APPROVALS'
```

**Related settings:** AUTO_APPROVE_FORWARD, REMOVE_APPROVER_FROM_GROUPS