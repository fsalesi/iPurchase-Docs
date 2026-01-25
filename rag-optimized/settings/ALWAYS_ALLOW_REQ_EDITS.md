# ALWAYS_ALLOW_REQ_EDITS - iPurchase System Setting

**Category:** Approval Workflow

Controls which users can always edit requisitions, regardless of status or approval stage.

### How It Works

Users in this list can edit requisition details at any point, including during and after approval. Changes may trigger re-routing depending on tolerance settings.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users can always edit |
| `*` (asterisk) | Everyone can always edit |
| Blank/empty | Normal edit restrictions apply |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_REQ_EDITS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_REQ_EDITS'
```
