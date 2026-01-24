# OOF_LIMIT_TO_APPROVERS - iPurchase System Setting

**Category:** Approval Workflow

A setting of TRUE will allow a user to delegate only to other Approvers. A False value will allow a user to delegate to anyone.

**Common questions this answers:**
- What is OOF_LIMIT_TO_APPROVERS?
- What does OOF_LIMIT_TO_APPROVERS do?
- What is the default value for OOF_LIMIT_TO_APPROVERS?
- How do I configure OOF_LIMIT_TO_APPROVERS?
- How does OOF_LIMIT_TO_APPROVERS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_TO_APPROVERS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_TO_APPROVERS'
```

**Related settings:** USE_CHAINED_DELEGATES