# REQ_MNT_HIDDEN_HEADER_FIELDS - iPurchase System Setting

**Category:** Requisitions

Comma separated list of fields that are hidden at the header.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_MNT_HIDDEN_HEADER_FIELDS |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | h_production,h_xxreq_uchar1,h_xxreq_uchar2,h_xxreq_uchar3,h_xxreq_uchar4,h_xxreq_uchar5,h_all_items,h_supplier_fax,h_req_perf,h_req_cons,h_xxreq_blanket,h_high_priority |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_MNT_HIDDEN_HEADER_FIELDS'
```

### Related Settings

- [REQ_INQUIRY_BUYER_ALWAYS](REQ_INQUIRY_BUYER_ALWAYS.md)
- [REQ_INQUIRY_FIELDS](REQ_INQUIRY_FIELDS.md)
- [REQ_INQ_HIDDEN_ELEMENTS](REQ_INQ_HIDDEN_ELEMENTS.md)