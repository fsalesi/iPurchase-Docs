# LOGIN_BACK_IN_OFFICE - iPurchase System Setting

**Category:** Security & Authentication

If you currently have the Out-Of-Office setting on, this setting can automatically turn it off when you login.

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_BACK_IN_OFFICE |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | ASK |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_BACK_IN_OFFICE'
```

### Related Settings

- [LOGIN_GOTO_CATALOG](LOGIN_GOTO_CATALOG.md)
- [LOGIN_GOTO_MNT](LOGIN_GOTO_MNT.md)
- [LOGIN_HIDE_FORGOT_PASSWORD](LOGIN_HIDE_FORGOT_PASSWORD.md)