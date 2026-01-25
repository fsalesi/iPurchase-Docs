# AUTO_COMMENTS_LINE_SITE - iPurchase System Setting

**Category:** Purchase Orders

Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_LINE_SITE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_LINE_SITE'
```

### Related Settings

- [AUTO_COMMENTS_BUYER](AUTO_COMMENTS_BUYER.md)
- [AUTO_COMMENTS_CO](AUTO_COMMENTS_CO.md)
- [AUTO_COMMENTS_OTHER](AUTO_COMMENTS_OTHER.md)
