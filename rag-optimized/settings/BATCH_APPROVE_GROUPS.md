# BATCH_APPROVE_GROUPS - iPurchase System Setting

**Category:** Approval Workflow

Comma Separated list of User ID's or Group ID's that will allow an approver to approve multiple requisitions simultaneously from the Requisition Inquiry screen.  If the user is a member of the spec...

**Common questions this answers:**
- What is BATCH_APPROVE_GROUPS?
- What does BATCH_APPROVE_GROUPS do?
- What is the default value for BATCH_APPROVE_GROUPS?
- How do I configure BATCH_APPROVE_GROUPS?
- How does BATCH_APPROVE_GROUPS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_APPROVE_GROUPS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_APPROVE_GROUPS'
```

**Related settings:** BATCH_APPROVE_GROUPS_ALWAYS, BATCH_APPROVE_GROUPS_FINAL