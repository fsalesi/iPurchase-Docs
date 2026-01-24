# PO_LOGO - iPurchase System Setting

**Category:** Purchase Orders

The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase or logo or frank.jpg". If the logo is in the wdm or agents folder then you only need to put filename not path. Ex. "logo.jpg". The PO Logo will be placed in the top left hand corner of the purchase order if using the GRAPHICAL PO_PRINT_PDF_FORMAT

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_LOGO |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_LOGO'
```
