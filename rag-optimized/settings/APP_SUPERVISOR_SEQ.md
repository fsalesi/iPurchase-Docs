# APP_SUPERVISOR_SEQ - iPurchase System Setting

**Category:** Approval Workflow

This is the Approval Level or Sequence when adding supervisors to the approval routing.

**Common questions this answers:**
- What is APP_SUPERVISOR_SEQ?
- What does APP_SUPERVISOR_SEQ do?
- What is the default value for APP_SUPERVISOR_SEQ?
- How do I configure APP_SUPERVISOR_SEQ?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_SUPERVISOR_SEQ |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 10 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_SUPERVISOR_SEQ'
```
