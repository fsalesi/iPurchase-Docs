# EMAIL_SUPPLIER_PO_FROM - iPurchase System Setting

**Category:** Email Configuration

This is the email address to be used as the "From" field on the email. This can be a static email address or one of $xxreq_buyer, $xxreq_User ID, $xxreq_obo. If this field is left blank then the setting "EMAILSFROM" is used.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_FROM |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | $xxreq_buyer |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_FROM'
```