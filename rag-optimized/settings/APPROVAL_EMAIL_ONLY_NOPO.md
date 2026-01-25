# APPROVAL_EMAIL_ONLY_NOPO - iPurchase System Setting

**Category:** Email Configuration

Controls whether approval notification emails are sent for all requisitions or only for those that don't require a purchase order.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Send approval emails only for non-PO requisitions |
| **FALSE** | Send approval emails for all requisitions (DEFAULT) |

### How It Works

Some organizations want to reduce email volume by limiting approval notifications. When enabled, this setting suppresses approval emails for requisitions that will generate a PO, sending notifications only for memo-only or non-PO requisitions.

**Use case:** Organizations where PO requisitions have their own notification workflow through ERP integration, so iPurchase approval emails are redundant.

**Behavior:**
- `xxreq_po_required = TRUE` → No approval email sent
- `xxreq_po_required = FALSE` → Approval email sent normally

### Common Questions

- How do I reduce the number of approval emails?
- Why aren't approvers getting emails for some requisitions?
- Can I limit emails to certain requisition types?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_EMAIL_ONLY_NOPO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_EMAIL_ONLY_NOPO'
```
