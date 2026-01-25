# PO_UPDATE_CHECK_REROUTE - iPurchase System Setting

**Category:** Change Orders

Controls whether the system compares approval routing between the original requisition and a change order. When enabled, any difference in approvers forces re-routing regardless of tolerance settings.

### How It Works

During change order submission, the system:
1. Calculates who would approve the change order with current values
2. Compares to who approved the original requisition
3. If different, forces re-routing even if dollar/percentage tolerances are met

This ensures that changes affecting approval routing get proper oversight.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Compare approvers and re-route if different (DEFAULT) |
| `FALSE` | Only use tolerance settings to determine re-routing |

### Example

```
Original req: $500, routes to Manager A
Change order: $520 (+$20, within tolerance), but now routes to Manager B

With PO_UPDATE_CHECK_REROUTE = TRUE:
-> Re-routes because approvers changed (Manager A vs Manager B)

With PO_UPDATE_CHECK_REROUTE = FALSE:
-> No re-route because within dollar/percentage tolerance
```

### Common Questions

- What is PO_UPDATE_CHECK_REROUTE?
- Why did my change order re-route when it was within tolerance?
- How do I control re-routing based on approver changes?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_CHECK_REROUTE |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_CHECK_REROUTE'
```

### Related Settings

- [PO_UPDATE_CHECK_REROUTE_RELEASES](PO_UPDATE_CHECK_REROUTE_RELEASES.md)
