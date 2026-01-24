# DROP_SHIP_EXCLUDE_SUPPLIER_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-Separated list of Supplier Types that should not show in the drop ship search. For example you may want to exclude employee addresses

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
| **Setting Name** | DROP_SHIP_EXCLUDE_SUPPLIER_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** |  |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DROP_SHIP_EXCLUDE_SUPPLIER_TYPES'
```
