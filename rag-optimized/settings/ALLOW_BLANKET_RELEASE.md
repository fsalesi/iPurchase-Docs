# ALLOW_BLANKET_RELEASE - iPurchase System Setting

**Category:** Purchase Orders

Controls which users can create releases against blanket purchase orders.

### How It Works

Users/groups in this list can create release orders against existing blanket POs. Blanket POs are long-term agreements with vendors; releases draw down against them.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users/groups can create releases |
| `*` (asterisk) | Everyone can create releases |
| Blank/empty | No one can create releases |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_BLANKET_RELEASE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_BLANKET_RELEASE'
```
