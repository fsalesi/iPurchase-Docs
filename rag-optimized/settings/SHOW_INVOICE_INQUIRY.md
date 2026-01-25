# SHOW_INVOICE_INQUIRY - iPurchase System Setting

**Category:** System Configuration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This display setting controls what information is visible to users in the interface.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_INVOICE_INQUIRY |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_INVOICE_INQUIRY'
```

### Related Settings

- [SHOW_PO_REV_ON_INQUIRY](SHOW_PO_REV_ON_INQUIRY.md)
- [SHOW_PO_STATUS_ON_REQ_INQUIRY](SHOW_PO_STATUS_ON_REQ_INQUIRY.md)
- [SHOW_REQ_REV_ON_INQUIRY](SHOW_REQ_REV_ON_INQUIRY.md)
