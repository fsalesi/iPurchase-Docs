# CO_HEADER_REROUTE_FIELDS - iPurchase System Setting

**Category:** Change Orders

Specifies which requisition header fields, when changed in a change order, will automatically force re-routing for approval regardless of tolerance settings.

### How It Works

When a user modifies a change order, the system checks if any of the fields listed in this setting have been changed from their original values. If so, the change order is flagged as a "material change" and must go through the full approval workflow.

### Valid Values

Comma-separated list of header field names from the xxreq_mstr table.

| Example Value | Meaning |
|---------------|---------|
| `xxreq_vendor` | Changing vendor forces re-approval |
| `xxreq_vendor,xxreq_site` | Changing vendor OR site forces re-approval |
| (blank) | No header fields force re-routing |

### Common Header Fields

- `xxreq_vendor` - Vendor/supplier
- `xxreq_site` - Delivery site
- `xxreq_buyer` - Assigned buyer
- `xxreq_type` - Requisition type
- `xxreq_shipto` - Ship-to address

### Common Questions

- What is CO_HEADER_REROUTE_FIELDS?
- Why did my change order require re-approval when I only changed the vendor?
- How do I control which changes require re-approval?
- What header fields can I monitor for changes?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_HEADER_REROUTE_FIELDS |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_HEADER_REROUTE_FIELDS'
```

### Related Settings

- **CO_ITEM_REROUTE_FIELDS** - Line fields that force re-routing
- **CO_ITEM_REROUTE_NEW** - Whether new lines force re-routing
- **PO_UPDATE_CHECK_REROUTE** - Check if approvers changed
