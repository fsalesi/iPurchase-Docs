# EMAIL_AUTH_PASSWORD - iPurchase System Setting

**Category:** Email Configuration

⚠️ **SENSITIVE** - SMTP authentication password. Do not modify without consulting ISS.

### Purpose

Password used to authenticate with the SMTP server when sending emails. Required when your email server requires authentication.

### Security Notes

- This value should be treated as sensitive
- Coordinate with your IT team when changing
- Ensure proper access controls on system settings

### Common Questions

- What is EMAIL_AUTH_PASSWORD?
- How do I configure SMTP authentication?
- Why are emails failing to send?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_AUTH_PASSWORD |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |
| **Sensitivity** | ⚠️ SENSITIVE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_AUTH_PASSWORD'
```

### Related Settings

- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
- [EMAIL_DEBUG_LEVEL](EMAIL_DEBUG_LEVEL.md)
