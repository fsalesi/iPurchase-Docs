# DEFAULT_BUYER_[SITE] - iPurchase System Setting

**Category:** Purchase Orders

This is the userid of the default buyer for the specified site, used on all new requisitions.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BUYER_[SITE] |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BUYER_[SITE]'
```

### Related Settings

- [DEFAULT_BUYER](DEFAULT_BUYER.md)
- [DEFAULT_SHIPTO](DEFAULT_SHIPTO.md)
- [DEFAULT_SHIPVIA](DEFAULT_SHIPVIA.md)