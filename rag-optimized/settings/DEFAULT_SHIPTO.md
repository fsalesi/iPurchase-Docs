# DEFAULT_SHIPTO - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for "Ship To" field.

### How It Works

See the description above for details on how this setting affects system behavior.

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