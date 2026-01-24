# NO_APPROVAL_EMAILS - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of requisition types that will not send approval emails to approvers.

**Common questions this answers:**
- What is NO_APPROVAL_EMAILS?
- What does NO_APPROVAL_EMAILS do?
- What is the default value for NO_APPROVAL_EMAILS?
- How do I configure NO_APPROVAL_EMAILS?
- How does NO_APPROVAL_EMAILS affect approval routing?
- How does NO_APPROVAL_EMAILS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_APPROVAL_EMAILS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_APPROVAL_EMAILS'
```
