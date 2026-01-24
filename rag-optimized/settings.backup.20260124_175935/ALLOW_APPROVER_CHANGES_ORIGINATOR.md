# ALLOW_APPROVER_CHANGES_ORIGINATOR - iPurchase System Setting

**Category:** Approval Workflow

Indicates whether the originator is allowed to add or remove approvers. In order for this to be enabled, Allow_Approver_Changes must also be set to TRUE.

**Common questions this answers:**
- What is ALLOW_APPROVER_CHANGES_ORIGINATOR?
- What does ALLOW_APPROVER_CHANGES_ORIGINATOR do?
- What is the default value for ALLOW_APPROVER_CHANGES_ORIGINATOR?
- How do I configure ALLOW_APPROVER_CHANGES_ORIGINATOR?
- How does ALLOW_APPROVER_CHANGES_ORIGINATOR affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_ORIGINATOR |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_ORIGINATOR'
```
