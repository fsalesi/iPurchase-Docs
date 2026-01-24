# APPROVAL_INCLUDE_FIELDS - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated list of fields from xxreq_mstr and xxreqd_det tables. You can limit the fields which display in the approval rules screen to only those in this list.

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
| **Setting Name** | APPROVAL_INCLUDE_FIELDS |
| **Category** | Approval Workflow |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_INCLUDE_FIELDS'
```
