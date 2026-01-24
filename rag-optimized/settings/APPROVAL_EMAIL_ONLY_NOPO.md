# APPROVAL_EMAIL_ONLY_NOPO - iPurchase System Setting

**Category:** Email Configuration

TRUE | FALSE. If TRUE, approval emails are sent only when the requisition does NOT require a PO (xxreq_po_required = TRUE). Used to reduce email volume.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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