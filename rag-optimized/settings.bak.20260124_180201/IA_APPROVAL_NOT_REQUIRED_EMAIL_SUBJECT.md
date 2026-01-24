# IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT - iPurchase System Setting

**Category:** iApprove Integration

Email subject line for iApprove notifications when approval is not required.

**Common questions this answers:**
- What is IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT?
- What does IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT do?
- What is the default value for IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT?
- How do I configure IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT?
- How does IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT affect approval routing?
- How does IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | Approval Not Required |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT'
```
