# MANDATORY_FIELDS - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated list of field names.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MANDATORY_FIELDS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | h_buyer,xh_supplier_contact,xh_supplier_phone,xh_supplier_fax,xh_deliver_to2,xh_req_type,xh_supplier_email,xh_bill_to,xh_req_need,xh_site,xh_freight_terms,xh_ship_via |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MANDATORY_FIELDS'
```