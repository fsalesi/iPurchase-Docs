# ALLOW_APPROVER_CHANGES_ROLES - iPurchase System Setting

**Category:** Approval Workflow

Any member of a group in this list will be allowed to add approvers.  If Allow_Approver_Changes_Remove_Approver is also enabled, then any member of these groups is also allowed to remove approvers....

**Common questions this answers:**
- What is ALLOW_APPROVER_CHANGES_ROLES?
- What does ALLOW_APPROVER_CHANGES_ROLES do?
- What is the default value for ALLOW_APPROVER_CHANGES_ROLES?
- How do I configure ALLOW_APPROVER_CHANGES_ROLES?
- How does ALLOW_APPROVER_CHANGES_ROLES affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_ROLES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_ROLES'
```
