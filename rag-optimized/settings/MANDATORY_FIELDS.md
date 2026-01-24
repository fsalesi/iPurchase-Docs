# MANDATORY_FIELDS - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated list of field names. The following fields can be either mandatory or optional. h_buyer,h_supplier_contact,h_supplier_phone,h_supplier_fax,h_deliver_to2,h_req_type,h_supplier_email,h_bill_to,h_req_need,h_site,h_freight_terms,h_ship_via To make a field mandatory, add the field to this list. To make it optional, remove the field from the list, or simply add an "x" to the beginning or end of the field identifier. Adding the "x" is the recommended approach.  All fields other than those listed above (Supplier, Ship To, Bill To, etc), are mandatory.

### How It Works

See the description above for details on how this setting affects system behavior.

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