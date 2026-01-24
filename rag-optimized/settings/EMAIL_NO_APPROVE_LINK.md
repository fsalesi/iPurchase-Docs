# EMAIL_NO_APPROVE_LINK - iPurchase System Setting

**Category:** Approval Workflow

True or False - Include link to Approve in email that goes out to approver. Default FALSE

**Common questions this answers:**
- What is EMAIL_NO_APPROVE_LINK?
- What does EMAIL_NO_APPROVE_LINK do?
- What is the default value for EMAIL_NO_APPROVE_LINK?
- How do I configure EMAIL_NO_APPROVE_LINK?
- How does EMAIL_NO_APPROVE_LINK affect approval routing?
- How does EMAIL_NO_APPROVE_LINK affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NO_APPROVE_LINK |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NO_APPROVE_LINK'
```
