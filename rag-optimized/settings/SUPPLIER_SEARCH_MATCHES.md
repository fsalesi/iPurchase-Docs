# SUPPLIER_SEARCH_MATCHES - iPurchase System Setting

**Category:** Catalog & Vendors

If set to True then a user can search for a supplier using any character in the suppliers name.  If set to True, the supplier lookup will run slower.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_SEARCH_MATCHES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_SEARCH_MATCHES'
```