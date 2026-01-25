# IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT - iPurchase System Setting

**Category:** iApprove Integration

Email subject line when iApprove document requires re-approval.

### How It Works

This setting customizes the subject line for outgoing emails. Choose text that clearly identifies the email purpose to improve open rates and avoid spam filters.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | Approval Required Again |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT'
```

### Related Settings

- [IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT](IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT.md)
- [IA_APPROVAL_REMINDER_EMAIL_SUBJECT](IA_APPROVAL_REMINDER_EMAIL_SUBJECT.md)
- [IA_APPROVAL_REQUIRED_EMAIL_SUBJECT](IA_APPROVAL_REQUIRED_EMAIL_SUBJECT.md)