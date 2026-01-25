# ALWAYS_ALLOW_ATTACHMENTS - iPurchase System Setting

**Category:** Approval Workflow

Controls which users can always add attachments to requisitions, even after submission.

### How It Works

Users in this list can add attachments at any point in the requisition lifecycle, including after submission and during approval. Others can only add attachments before submission.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users can always add attachments |
| `*` (asterisk) | Everyone can always add attachments |
| Blank/empty | Attachments only allowed before submission |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_ATTACHMENTS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_ATTACHMENTS'
```
