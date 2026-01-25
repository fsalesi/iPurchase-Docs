# LOGIN_GOTO_CATALOG - iPurchase System Setting

**Category:** Security & Authentication

Comma Separated list of User ID's or Group ID's that will be directed to the catalog screen as their landing page.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) to specify which users or groups have access.

**Common configurations:**
- `*` - All users/everyone
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_GOTO_CATALOG |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_GOTO_CATALOG'
```

### Related Settings

- [LOGIN_BACK_IN_OFFICE](LOGIN_BACK_IN_OFFICE.md)
- [LOGIN_GOTO_MNT](LOGIN_GOTO_MNT.md)
- [LOGIN_HIDE_FORGOT_PASSWORD](LOGIN_HIDE_FORGOT_PASSWORD.md)