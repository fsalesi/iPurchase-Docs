# ALLOW_PUNCHOUT - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to use punchouts. Asterisk indicates everyone, a blank indicates no one. This setting turns on or off the Punch-out functionality for the given user.

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
| **Setting Name** | ALLOW_PUNCHOUT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_PUNCHOUT'
```
