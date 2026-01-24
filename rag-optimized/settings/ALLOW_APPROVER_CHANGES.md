# ALLOW_APPROVER_CHANGES - iPurchase System Setting

**Category:** Approval Workflow

This is the global setting which controls whether Approvers can be manually added or deleted from the approval routing. It also controls whether the Force Approval functionality is enabled. Also se...

**Common questions this answers:**
- What is ALLOW_APPROVER_CHANGES?
- What does ALLOW_APPROVER_CHANGES do?
- What is the default value for ALLOW_APPROVER_CHANGES?
- How do I configure ALLOW_APPROVER_CHANGES?
- How does ALLOW_APPROVER_CHANGES affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES'
```
