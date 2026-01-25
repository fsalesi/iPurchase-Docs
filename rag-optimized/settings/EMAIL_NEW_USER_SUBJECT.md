# EMAIL_NEW_USER_SUBJECT - iPurchase System Setting

**Category:** Email Configuration

Subject line for the welcome email sent to newly created users.

### How It Works

When a new user account is created and a welcome email is sent, this setting provides the email subject line. Keep it clear and recognizable so users don't mistake it for spam.

**Example:**
```
EMAIL_NEW_USER_SUBJECT = "Welcome to iPurchase - Your Account is Ready"
```

### Valid Values

Text string for the email subject.

### Common Questions

- How do I customize the new user email subject?
- What subject line should I use for welcome emails?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NEW_USER_SUBJECT |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NEW_USER_SUBJECT'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
