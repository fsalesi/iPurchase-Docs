# EMAIL_HELP_TAG - iPurchase System Setting

**Category:** Email Configuration

Standard help text included in email notifications, typically containing contact information and guidance.

### How It Works

This text is appended to internal emails to provide users with guidance on getting help. The $HELPDESK token is replaced with the EMAIL_HELPDESK address.

**Default text:**
```
If questions, email the $HELPDESK, or contact the originator, or approver.
```

**Customization:** Modify to match your organization's support structure and escalation paths.

### Valid Values

Text string. Can include the $HELPDESK token for dynamic substitution.

### Common Questions

- How do I customize the help text in emails?
- What tokens can I use in email templates?
- How do I remove the help tag from emails?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HELP_TAG |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | If questions, email the $HELPDESK, or contact the originator, or approver. |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HELP_TAG'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
