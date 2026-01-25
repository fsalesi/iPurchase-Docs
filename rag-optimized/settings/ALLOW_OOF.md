# ALLOW_OOF - iPurchase System Setting

**Category:** User Management

Controls which users can configure Out of Office (delegation) settings. When enabled, users can designate another person to approve requisitions on their behalf during absences.

### How It Works

When a user is in this list, they can access the Out of Office functionality to:
- Set a delegate to handle their approvals
- Specify start/end dates for the delegation
- Have pending approvals forwarded to the delegate

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can set OOF (DEFAULT) |
| Blank/empty | No one can set OOF |
| User/Group list | Only specified users or groups can set OOF |

### Common Questions

- What is ALLOW_OOF?
- How do I enable Out of Office?
- Who can set up delegation?
- How do I restrict OOF to certain users?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_OOF |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_OOF'
```

### Related Settings

- [ALLOW_BATCH_PO](ALLOW_BATCH_PO.md)
- [ALLOW_BLANKET_RELEASE](ALLOW_BLANKET_RELEASE.md)
- [ALLOW_BUG](ALLOW_BUG.md)
