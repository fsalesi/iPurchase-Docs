# IA_EMAIL_SUBJECT_APPEND - iPurchase System Setting

**Category:** iApprove Integration

Text appended to all iApprove email subject lines.

### How It Works

This setting customizes the subject line for outgoing emails. Choose text that clearly identifies the email purpose to improve open rates and avoid spam filters.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_EMAIL_SUBJECT_APPEND |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_EMAIL_SUBJECT_APPEND'
```

### Related Settings

- [IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT](IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT.md)
- [IA_APPROVAL_REMINDER_EMAIL_SUBJECT](IA_APPROVAL_REMINDER_EMAIL_SUBJECT.md)
- [IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT](IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT.md)