# BATCH_APPROVE_GROUPS_FINAL - iPurchase System Setting

**Category:** Approval Workflow

Can-Do list. Groups allowed to perform batch approval as the final approver. Restricts batch approval to specific approval steps.

**Common questions this answers:**
- What is BATCH_APPROVE_GROUPS_FINAL?
- What does BATCH_APPROVE_GROUPS_FINAL do?
- What is the default value for BATCH_APPROVE_GROUPS_FINAL?
- How do I configure BATCH_APPROVE_GROUPS_FINAL?
- How does BATCH_APPROVE_GROUPS_FINAL affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_APPROVE_GROUPS_FINAL |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_APPROVE_GROUPS_FINAL'
```

**Related settings:** BATCH_APPROVE_GROUPS