# SUPPLIER_PO_ATTACHMENTS - iPurchase System Setting

**Category:** Purchase Orders

Comma-Separated List of paths and files. This is a list of files which is to be emailed to the supplier as attachments to the Purchase Order.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_ATTACHMENTS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_ATTACHMENTS'
```