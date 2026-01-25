# DEFAULT_SHIPTO - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for "Ship To" field.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SHIPTO |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SHIPTO'
```

### Related Settings

- [DEFAULT_BUYER](DEFAULT_BUYER.md)
- [DEFAULT_BUYER_[SITE]](DEFAULT_BUYER_[SITE].md)
- [DEFAULT_SHIPVIA](DEFAULT_SHIPVIA.md)