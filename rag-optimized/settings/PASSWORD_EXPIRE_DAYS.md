# PASSWORD_EXPIRE_DAYS - iPurchase System Setting

**Category:** Security & Authentication

Defines how many days a password remains valid before the user must change it. Set to 0 to disable password expiration.

### How It Works

iPurchase tracks the last password change date for each user. When the current date exceeds last change date + PASSWORD_EXPIRE_DAYS, the user is forced to change their password at next login.

### Valid Values

| Value | Behavior |
|-------|----------|
| Number | Days until password expires (e.g., "45") |
| 0 | Passwords never expire |

### Common Questions

- What is PASSWORD_EXPIRE_DAYS?
- How often do passwords expire?
- How do I disable password expiration?
- Why am I being asked to change my password?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_EXPIRE_DAYS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 45 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_EXPIRE_DAYS'
```

### Related Settings

- [PASSWORD_RULES](PASSWORD_RULES.md) - Password complexity requirements
- [PASSWORD_REMINDER_DAYS](PASSWORD_REMINDER_DAYS.md) - Days before expiration to warn user
