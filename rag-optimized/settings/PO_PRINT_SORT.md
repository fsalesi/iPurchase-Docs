# PO_PRINT_SORT - iPurchase System Setting

**Category:** Purchase Orders

This setting determines the value which will be used to sort the Purchase Order on the PO Print screen.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_SORT |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | LINE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_SORT'
```