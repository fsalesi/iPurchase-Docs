# ROLES - iPurchase System Setting

**Category:** Approval Workflow

Comma-separated list of role names that can be assigned in the User Roles screen. These roles are combined with hard-coded Types (Account, Cost Center, Project, Site, Sub Account) to create approval rule variables like $Cost Center:Manager or $Project:Director. Example: Manager,Director,VP,SVP

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
| **Setting Name** | ROLES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ROLES'
```
