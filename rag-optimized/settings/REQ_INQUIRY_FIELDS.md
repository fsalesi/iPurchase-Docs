# REQ_INQUIRY_FIELDS - iPurchase System Setting

**Category:** Requisitions

Comma separated list of fields that will be shown as columns in requisition inquiry.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_INQUIRY_FIELDS |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_INQUIRY_FIELDS'
```

### Related Settings

- [REQ_INQUIRY_BUYER_ALWAYS](REQ_INQUIRY_BUYER_ALWAYS.md)
- [REQ_INQ_HIDDEN_ELEMENTS](REQ_INQ_HIDDEN_ELEMENTS.md)
- [REQ_MNT_HIDDEN_ELEMENTS](REQ_MNT_HIDDEN_ELEMENTS.md)