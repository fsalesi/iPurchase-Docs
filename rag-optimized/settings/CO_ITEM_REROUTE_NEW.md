# CO_ITEM_REROUTE_NEW - iPurchase System Setting

**Category:** Change Orders

Controls whether adding a new line item to a change order automatically forces re-routing for approval, regardless of tolerance settings.

### How It Works

When a user adds a completely new line to a change order (not modifying an existing line), this setting determines if the change order must go through the full approval workflow again.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | New lines force re-routing - change order goes back through approval |
| `FALSE` | New lines don't automatically force re-routing - tolerance rules still apply |

### Use Case

Organizations may want to re-approve any change order that adds new items because:
- New items may require different approvers (different cost center, project, etc.)
- Prevents users from adding items to approved POs without oversight
- Ensures all line items have proper approval

### Common Questions

- What is CO_ITEM_REROUTE_NEW?
- Why did my change order require re-approval when I added a line?
- How do I control re-routing for new line items?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_ITEM_REROUTE_NEW |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_ITEM_REROUTE_NEW'
```

### Related Settings

- [CO_ITEM_REROUTE_FIELDS](CO_ITEM_REROUTE_FIELDS.md) - Line fields that force re-routing when changed
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md) - Header fields that force re-routing
- [PO_UPDATE_TOLERANCE_AMOUNT](PO_UPDATE_TOLERANCE_AMOUNT.md) - Dollar tolerance for changes
- [PO_UPDATE_TOLERANCE_PCT](PO_UPDATE_TOLERANCE_PCT.md) - Percentage tolerance for changes
