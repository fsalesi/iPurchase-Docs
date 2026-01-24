# DEFAULT_SITE - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for the "Site" field. Must be a valid site.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SITE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SITE'
```
