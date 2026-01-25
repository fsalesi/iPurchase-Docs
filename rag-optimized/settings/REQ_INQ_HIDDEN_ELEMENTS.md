# REQ_INQ_HIDDEN_ELEMENTS - iPurchase System Setting

**Category:** Requisitions

Technical - Do Not Modify without consulting ISS

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_INQ_HIDDEN_ELEMENTS |
| **Category** | Requisitions |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_INQ_HIDDEN_ELEMENTS'
```

### Related Settings

- [REQ_INQUIRY_BUYER_ALWAYS](REQ_INQUIRY_BUYER_ALWAYS.md)
- [REQ_INQUIRY_FIELDS](REQ_INQUIRY_FIELDS.md)
- [REQ_MNT_HIDDEN_ELEMENTS](REQ_MNT_HIDDEN_ELEMENTS.md)
