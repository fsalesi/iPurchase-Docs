# RT_CATALOG EXCEPTION_PP - iPurchase System Setting

**Category:** Catalog & Vendors

Technical - Do Not Modify without consulting ISS

### How It Works

This setting controls catalog functionality, affecting how users browse and select items from supplier catalogs.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_CATALOG EXCEPTION_PP |
| **Category** | Catalog & Vendors |
| **Owner** | ISS |
| **Default Value** | catexceptload.p |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_CATALOG EXCEPTION_PP'
```

### Related Settings

- [RT_VENDOR_ITEM_ONLY](RT_VENDOR_ITEM_ONLY.md)