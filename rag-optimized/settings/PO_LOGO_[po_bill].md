# PO_LOGO_[po_bill] - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to enter a PO Logo based on the PO Bill To Field. The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase or logo or frank.jpg". If the logo is in the wdm or agents folder then you only need to put filename not path. Ex. "frank.jpg". The PO Logo will be placed in the top left hand corner of the purchase order.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_LOGO_[po_bill] |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_LOGO_[po_bill]'
```