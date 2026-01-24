# PO_SIGNATURE_BUYER_[domain code]_[site code] - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to enter a buyers signature based on the domain and the site of the buyer user record The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or frank.jpg". If the signature is in the wdm or agents folder then you only need to put filename not path. Ex "frank.jpg". The signature file should be 250x60 pixels.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_SIGNATURE_BUYER_[domain code]_[site code] |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_SIGNATURE_BUYER_[domain code]_[site code]'
```