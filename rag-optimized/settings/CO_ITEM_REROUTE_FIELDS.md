# CO_ITEM_REROUTE_FIELDS - iPurchase System Setting

**Category:** Change Orders

Specifies which requisition line item fields, when changed in a change order, will automatically force re-routing for approval regardless of tolerance settings.

### How It Works

When a user modifies line items in a change order, the system checks if any of the fields listed in this setting have been changed from their original values. If so, the change order is flagged as a "material change" and must go through the full approval workflow.

### Valid Values

Comma-separated list of line field names from the xxreqd_det table.

| Example Value | Meaning |
|---------------|---------|
| `xxreqd_cc` | Changing cost center forces re-approval |
| `xxreqd_cc,xxreqd_acct` | Changing cost center OR account forces re-approval |
| (blank) | No line fields force re-routing |

### Common Line Fields

- `xxreqd_cc` - Cost center
- `xxreqd_acct` - GL account
- `xxreqd_sub` - Sub-account
- `xxreqd_project` - Project code
- `xxreqd_site` - Line site

### Common Questions

- What is CO_ITEM_REROUTE_FIELDS?
- Why did my change order require re-approval when I only changed the cost center?
- How do I control which line changes require re-approval?
- What line fields can I monitor for changes?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_ITEM_REROUTE_FIELDS |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_ITEM_REROUTE_FIELDS'
```

### Related Settings

- [CO_DELETE_CANCELLED_LINES](CO_DELETE_CANCELLED_LINES.md)
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md)
- [CO_IGNORE_COST](CO_IGNORE_COST.md)
