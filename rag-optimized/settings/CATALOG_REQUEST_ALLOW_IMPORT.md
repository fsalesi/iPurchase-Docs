# CATALOG_REQUEST_ALLOW_IMPORT - iPurchase System Setting

**Category:** User Management

Comma Separated list of User ID's or Group ID's that can load a new approved catalog into iPurchase.  Asterisk indicates everyone, a blank indicates no one. This setting is related to CATALOG_ALLOW_IMPORT

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
| **Setting Name** | CATALOG_REQUEST_ALLOW_IMPORT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_REQUEST_ALLOW_IMPORT'
```
