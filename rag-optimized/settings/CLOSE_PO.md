# CLOSE_PO - iPurchase System Setting

**Category:** Purchase Orders

Comma Separated list of User ID's or Group ID's that will have the ability to close PO  or  PO line on Purchase order.  Either Line or whole PO can be closed. Close or canceled depends on Receipts. Asterisk indicates everyone, a blank indicates no one.

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
| **Setting Name** | CLOSE_PO |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CLOSE_PO'
```
