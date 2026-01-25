# ALLOW_CHANGE_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Controls which users can change their own password in iPurchase.

### How It Works

Users in this list see the "Change Password" option in their profile. Typically set to everyone (*) unless using external authentication like SSO/AD.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can change password (DEFAULT) |
| Blank/empty | No one can change password |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CHANGE_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CHANGE_PASSWORD'
```

### Related Settings

- [ALLOW_MULTIPLE_SESSIONS](ALLOW_MULTIPLE_SESSIONS.md)
