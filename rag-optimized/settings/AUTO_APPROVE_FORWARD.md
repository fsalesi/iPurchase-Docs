# AUTO_APPROVE_FORWARD - iPurchase System Setting

**Category:** Approval Workflow

1 if a user approves go through all other approvals where that user is listed in a group. If that user is the only member of the group, then automatically approve. 2 Last approval is never automati...

**Common questions this answers:**
- What is AUTO_APPROVE_FORWARD?
- What does AUTO_APPROVE_FORWARD do?
- What is the default value for AUTO_APPROVE_FORWARD?
- How do I configure AUTO_APPROVE_FORWARD?
- How does AUTO_APPROVE_FORWARD affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_APPROVE_FORWARD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_APPROVE_FORWARD'
```

**Related settings:** MULTIPLE_APPROVALS