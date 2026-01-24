# SUPERVISOR_APPROVAL_FIELD - iPurchase System Setting

**Category:** Approval Workflow

Field name. Database field used to determine supervisor chain (default: wus_supervisor).

**Common questions this answers:**
- What is SUPERVISOR_APPROVAL_FIELD?
- What does SUPERVISOR_APPROVAL_FIELD do?
- What is the default value for SUPERVISOR_APPROVAL_FIELD?
- How do I configure SUPERVISOR_APPROVAL_FIELD?
- How does SUPERVISOR_APPROVAL_FIELD affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_APPROVAL_FIELD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | wus_supervisor |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_APPROVAL_FIELD'
```
