# PASSWORD_REMINDER_DAYS - iPurchase System Setting

**Category:** Security & Authentication

This setting allows the administrator to set how many days before the password expires to notify user when logging in.

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_REMINDER_DAYS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 7 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_REMINDER_DAYS'
```

### Related Settings

- [PASSWORD_EXPIRE_DAYS](PASSWORD_EXPIRE_DAYS.md)
- [PASSWORD_RESET_TIMEOUT](PASSWORD_RESET_TIMEOUT.md)
- [PASSWORD_RULES](PASSWORD_RULES.md)