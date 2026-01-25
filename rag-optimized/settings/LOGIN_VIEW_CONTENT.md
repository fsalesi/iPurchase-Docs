# LOGIN_VIEW_CONTENT - iPurchase System Setting

**Category:** Security & Authentication

This setting allows the administrator to turn off the recent news, events, and video sections from the login page.

### How It Works

This security setting affects user authentication and login behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_VIEW_CONTENT |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | 1,0,1 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_VIEW_CONTENT'
```

### Related Settings

- [LOGIN_BACK_IN_OFFICE](LOGIN_BACK_IN_OFFICE.md)
- [LOGIN_GOTO_CATALOG](LOGIN_GOTO_CATALOG.md)
- [LOGIN_GOTO_MNT](LOGIN_GOTO_MNT.md)
