# MASTER_COMMENTS_ROLE_LIST - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated list of group ID's or "*" for all. Only members of these groups will be allowed to enter or delete master comments from a requisition.

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
| **Setting Name** | MASTER_COMMENTS_ROLE_LIST |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MASTER_COMMENTS_ROLE_LIST'
```
