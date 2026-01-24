# RT_VENDOR_ITEM_ONLY - iPurchase System Setting

**Category:** Catalog & Vendors

Comma separated list of requisition types which will mandate that an item selected to a requisition must exist in the vendor part cross-reference table in QAD.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_VENDOR_ITEM_ONLY |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_VENDOR_ITEM_ONLY'
```