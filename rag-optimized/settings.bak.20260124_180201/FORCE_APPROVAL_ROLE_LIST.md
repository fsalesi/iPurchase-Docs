# FORCE_APPROVAL_ROLE_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma Separated list of User ID's or Group ID's that are allowed to Force Approve any requisition.  Force Approval bypasses all open approvals and creates a PO. A history of this action is maintain...

**Common questions this answers:**
- What is FORCE_APPROVAL_ROLE_LIST?
- What does FORCE_APPROVAL_ROLE_LIST do?
- What is the default value for FORCE_APPROVAL_ROLE_LIST?
- How do I configure FORCE_APPROVAL_ROLE_LIST?
- How does FORCE_APPROVAL_ROLE_LIST affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FORCE_APPROVAL_ROLE_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FORCE_APPROVAL_ROLE_LIST'
```
