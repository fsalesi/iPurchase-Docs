# ALLOW_AUTO_REROUTE - iPurchase System Setting

**Category:** Change Orders

Controls whether iPurchase automatically re-routes a requisition when an approver makes changes that affect the approval path. When enabled, the system recalculates approvers after changes and re-routes if the new approver set differs from the current one.

### How It Works

When an approver with edit permissions modifies a requisition (e.g., changes cost center, account, or amount), the system:
1. Recalculates who should approve based on the new values
2. Compares the new approver set to the current approvers
3. If different, automatically re-routes the requisition when the approver clicks Approve

This ensures changes always get appropriate approval, even if the original routing was different.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Enable automatic re-routing when approvers change (DEFAULT) |
| `FALSE` | Disable automatic re-routing - original approvers remain |

### Example

```
Original requisition: $500, Cost Center 1000 -> Routes to Manager A
Approver changes cost center to 2000 -> Would route to Manager B

With ALLOW_AUTO_REROUTE = TRUE:
-> Requisition re-routes to Manager B

With ALLOW_AUTO_REROUTE = FALSE:
-> Requisition continues with Manager A (original routing)
```

### Common Questions

- What is ALLOW_AUTO_REROUTE?
- Why did my requisition re-route after I approved it?
- How do I control automatic re-routing?
- Can I disable re-routing for approver changes?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_AUTO_REROUTE |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_AUTO_REROUTE'
```

### Related Settings

- [ALLOWED_DOLLAR_INCREASE](ALLOWED_DOLLAR_INCREASE.md) - Dollar threshold before re-routing
- [ALLOWED_PERCENT_INCREASE](ALLOWED_PERCENT_INCREASE.md) - Percentage threshold before re-routing
- [PO_UPDATE_CHECK_REROUTE](PO_UPDATE_CHECK_REROUTE.md) - Check approver changes for change orders
