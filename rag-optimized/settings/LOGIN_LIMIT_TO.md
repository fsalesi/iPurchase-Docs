# LOGIN_LIMIT_TO - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User ID's or Group ID's that are allowed to login to the system. This setting is used for when putting the system in Admin mode (upgrade or new release). Asterisk indicates everyone, a blank indicates no one.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_LIMIT_TO |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_LIMIT_TO'
```
