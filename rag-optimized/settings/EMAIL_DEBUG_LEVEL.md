# EMAIL_DEBUG_LEVEL - iPurchase System Setting

**Category:** Email Configuration

Controls the verbosity of email system logging for troubleshooting delivery issues.

### Valid Values

| Value | Behavior |
|-------|----------|
| **0** | Off - No debug logging (DEFAULT) |
| **1** | Basic - Log send attempts and failures |
| **2** | Detailed - Include message headers and recipients |
| **3** | Verbose - Full SMTP conversation logging |

### How It Works

When troubleshooting email delivery problems, increase this setting to capture detailed logs about the email sending process. The logs help identify issues like:
- SMTP authentication failures
- Connection timeouts
- Rejected recipients
- TLS/SSL handshake problems

**⚠️ Warning:** Higher debug levels may log sensitive information. Reset to 0 after troubleshooting.

### Common Questions

- Why aren't emails being delivered?
- How do I troubleshoot SMTP connection issues?
- Where do email debug logs appear?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_DEBUG_LEVEL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 0 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_DEBUG_LEVEL'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
