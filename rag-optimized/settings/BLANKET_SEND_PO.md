# BLANKET_SEND_PO - iPurchase System Setting

**Category:** Email Configuration

Controls whether blanket PO emails are automatically sent to suppliers.

### How It Works

When TRUE, blanket purchase orders are automatically emailed to suppliers upon creation or update, similar to regular PO emailing.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Auto-email blanket POs to suppliers |
| `FALSE` | Don't auto-email blanket POs |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BLANKET_SEND_PO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BLANKET_SEND_PO'
```

### Related Settings

- [EMAIL_SUPPLIER_PO](EMAIL_SUPPLIER_PO.md) - Auto-email regular POs
- [ALLOW_BLANKET_RELEASE](ALLOW_BLANKET_RELEASE.md) - Who can create blanket releases
