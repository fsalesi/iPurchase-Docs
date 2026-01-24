# PUNCHOUT_CHANGE_ORDER_SEND - iPurchase System Setting

**Category:** Change Orders

Send PO revisions automatically to punchout suppliers via cXML. List of Vendor Numbers or * for all. CAN-DO functionality !staples,*

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
| **Setting Name** | PUNCHOUT_CHANGE_ORDER_SEND |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_CHANGE_ORDER_SEND'
```
