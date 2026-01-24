# ALLOW_HOLD - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's who are allowed to put a requisition on hold while it is pending. Asterisk indicates everyone, a blank indicates no one. Example: It would go on hold if an approver is waiting for information from the supplier.

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
| **Setting Name** | ALLOW_HOLD |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_HOLD'
```
