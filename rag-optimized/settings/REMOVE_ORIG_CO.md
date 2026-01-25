# REMOVE_ORIG_CO - iPurchase System Setting

**Category:** Approval Workflow

Controls whether the requisition originator is automatically removed from the approval routing for change orders. When enabled, users cannot approve their own change orders.

### How It Works

When a change order is submitted, if this setting is TRUE, the system removes the originator from any approval step where they would otherwise appear. This ensures someone other than the person making the change must approve it.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Remove originator from change order approval routing |
| `FALSE` | Originator can appear in change order approval routing (DEFAULT) |

### Common Questions

- What is REMOVE_ORIG_CO?
- Can I approve my own change order?
- How do I prevent self-approval of change orders?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_ORIG_CO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIG_CO'
```

### Related Settings

- [REMOVE_APPROVER_FROM_GROUPS](REMOVE_APPROVER_FROM_GROUPS.md)
- [REMOVE_APPROVER_ROLE_LIST](REMOVE_APPROVER_ROLE_LIST.md)
- [REMOVE_ORIGINATOR_FROM_GROUP_CO](REMOVE_ORIGINATOR_FROM_GROUP_CO.md)
