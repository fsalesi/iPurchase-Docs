# EMAIL_AUTH_USER - iPurchase System Setting

**Category:** Email Configuration

Technical setting that specifies the username for SMTP authentication when sending emails.

### How It Works

When EMAIL_AUTH_TYPE is set to BASIC or OAUTH2, this setting provides the username credential for authenticating with the mail server.

**⚠️ Technical Setting:** Do not modify without consulting your ISS representative or IT department. Incorrect configuration will prevent all email notifications from being sent.

**Common formats:**
- Email address: `ipurchase@company.com`
- Domain username: `DOMAIN\serviceaccount`
- Plain username: `ipurchase_service`

The format depends on your mail server configuration.

### Valid Values

Username string appropriate for your email server authentication.

### Common Questions

- What username should I use for email authentication?
- Why is iPurchase failing to send emails?
- How do I configure the email service account?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_AUTH_USER |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_AUTH_USER'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_DEBUG_LEVEL](EMAIL_DEBUG_LEVEL.md)
