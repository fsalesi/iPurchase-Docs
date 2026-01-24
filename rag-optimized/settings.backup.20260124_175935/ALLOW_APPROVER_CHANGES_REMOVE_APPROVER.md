# ALLOW_APPROVER_CHANGES_REMOVE_APPROVER - iPurchase System Setting

**Category:** Approval Workflow

Allow a user to remove an approver from the routing rules.  If this is enabled and Allow_Approver_Changes_Originator is enabled then the originator will also be allowed to remove approvers from the...

**Common questions this answers:**
- What is ALLOW_APPROVER_CHANGES_REMOVE_APPROVER?
- What does ALLOW_APPROVER_CHANGES_REMOVE_APPROVER do?
- What is the default value for ALLOW_APPROVER_CHANGES_REMOVE_APPROVER?
- How do I configure ALLOW_APPROVER_CHANGES_REMOVE_APPROVER?
- How does ALLOW_APPROVER_CHANGES_REMOVE_APPROVER affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_REMOVE_APPROVER |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_REMOVE_APPROVER'
```
