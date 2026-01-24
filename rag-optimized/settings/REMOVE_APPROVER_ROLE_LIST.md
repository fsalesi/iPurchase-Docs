# REMOVE_APPROVER_ROLE_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that are allowed to remove an Approver from any requisition. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is REMOVE_APPROVER_ROLE_LIST?
- What does REMOVE_APPROVER_ROLE_LIST do?
- What is the default value for REMOVE_APPROVER_ROLE_LIST?
- How do I configure REMOVE_APPROVER_ROLE_LIST?
- How does REMOVE_APPROVER_ROLE_LIST affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_APPROVER_ROLE_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_APPROVER_ROLE_LIST'
```
