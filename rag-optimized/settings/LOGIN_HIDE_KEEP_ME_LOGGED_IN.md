# LOGIN_HIDE_KEEP_ME_LOGGED_IN - iPurchase System Setting

**Category:** Security & Authentication

Hide the Keep me logged in link on the login screen

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_KEEP_ME_LOGGED_IN |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_KEEP_ME_LOGGED_IN'
```

### Related Settings

- [LOGIN_BACK_IN_OFFICE](LOGIN_BACK_IN_OFFICE.md)
- [LOGIN_GOTO_CATALOG](LOGIN_GOTO_CATALOG.md)
- [LOGIN_GOTO_MNT](LOGIN_GOTO_MNT.md)