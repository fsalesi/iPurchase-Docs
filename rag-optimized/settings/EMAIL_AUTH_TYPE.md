# EMAIL_AUTH_TYPE - iPurchase System Setting

**Category:** Email Configuration

Technical setting that specifies the authentication method used when connecting to the SMTP email server.

### Valid Values

| Value | Description |
|-------|-------------|
| **NONE** | No authentication required |
| **BASIC** | Username/password authentication |
| **OAUTH2** | OAuth 2.0 authentication (for Office 365, Gmail) |

### How It Works

This setting works in conjunction with EMAIL_AUTH_USER and EMAIL_AUTH_PASSWORD to authenticate iPurchase with your mail server.

**⚠️ Technical Setting:** Do not modify without consulting your ISS representative or IT department. Incorrect configuration will prevent all email notifications from being sent.

**Configuration depends on your email provider:**
- **On-premises Exchange:** Usually BASIC or NONE
- **Office 365:** May require OAUTH2 depending on security settings
- **Gmail/Google Workspace:** Requires OAUTH2 or app-specific passwords

### Common Questions

- Why aren't emails being sent from iPurchase?
- How do I configure iPurchase for Office 365?
- What authentication does iPurchase support for email?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_AUTH_TYPE |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_AUTH_TYPE'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
- [EMAIL_DEBUG_LEVEL](EMAIL_DEBUG_LEVEL.md)
