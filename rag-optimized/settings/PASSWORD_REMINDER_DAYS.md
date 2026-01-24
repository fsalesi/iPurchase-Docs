# PASSWORD_REMINDER_DAYS - iPurchase System Setting

**Category:** Security & Authentication

This setting allows the administrator to set how many days before the password expires to notify user when logging in.

**Common questions this answers:**
- What is PASSWORD_REMINDER_DAYS?
- What does PASSWORD_REMINDER_DAYS do?
- What is the default value for PASSWORD_REMINDER_DAYS?
- How do I configure PASSWORD_REMINDER_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_REMINDER_DAYS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 7 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_REMINDER_DAYS'
```
