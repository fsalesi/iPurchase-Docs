# CART_SUM_LINES - iPurchase System Setting

**Category:** Uncategorized

Within a catalog requisition, iPurchase will add up the quantities of all the items chosen by default.  If the administrator sets this setting to true the system will display number of lines instead of adding up the quantities.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CART_SUM_LINES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | False  |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CART_SUM_LINES'
```