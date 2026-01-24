# IA_EMAIL_SUBJECT_APPEND - iPurchase System Setting

**Category:** iApprove Integration

Text appended to all iApprove email subject lines. Used for environment identification (e.g., [TEST]).

**Common questions this answers:**
- What is IA_EMAIL_SUBJECT_APPEND?
- What does IA_EMAIL_SUBJECT_APPEND do?
- What is the default value for IA_EMAIL_SUBJECT_APPEND?
- How do I configure IA_EMAIL_SUBJECT_APPEND?
- How does IA_EMAIL_SUBJECT_APPEND affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_EMAIL_SUBJECT_APPEND |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_EMAIL_SUBJECT_APPEND'
```
