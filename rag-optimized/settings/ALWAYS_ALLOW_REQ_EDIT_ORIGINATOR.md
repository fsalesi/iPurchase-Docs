# ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR - iPurchase System Setting

**Category:** Approval Workflow

Controls whether the requisition originator can always edit their own requisitions.

### How It Works

When TRUE, the person who created a requisition can edit it at any stage. Works in conjunction with ALWAYS_ALLOW_REQ_EDITS for role-based edit permissions.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Originator can always edit their own reqs |
| `FALSE` | Normal edit restrictions apply to originator |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR'
```
