# PO_BREAK_BY - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of fields on a requisition that will be used to split the requisition into multiple PO's. Or Comma separated list of fields on a requisition that will be used to consolidate PO's from multiple requisitions. Ex: xxreqd_vendor,xxreq_site

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
| **Setting Name** | PO_BREAK_BY |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | xxreqd_vendor |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_BREAK_BY'
```
