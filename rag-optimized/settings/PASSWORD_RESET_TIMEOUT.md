# PASSWORD_RESET_TIMEOUT - iPurchase System Setting

**Category:** Security & Authentication

Technical - Do Not Modify without consulting ISS

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_RESET_TIMEOUT |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_RESET_TIMEOUT'
```

### Related Settings

- [PASSWORD_EXPIRE_DAYS](PASSWORD_EXPIRE_DAYS.md)
- [PASSWORD_REMINDER_DAYS](PASSWORD_REMINDER_DAYS.md)
- [PASSWORD_RULES](PASSWORD_RULES.md)
