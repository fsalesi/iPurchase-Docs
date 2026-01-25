# LOGIN_HIDE_FORGOT_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Hide the Forgot Password link on the login screen

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_FORGOT_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_FORGOT_PASSWORD'
```

### Related Settings

- [LOGIN_BACK_IN_OFFICE](LOGIN_BACK_IN_OFFICE.md)
- [LOGIN_GOTO_CATALOG](LOGIN_GOTO_CATALOG.md)
- [LOGIN_GOTO_MNT](LOGIN_GOTO_MNT.md)