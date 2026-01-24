# EMAIL_OPEN_PO_INCLUDE_TYPES - iPurchase System Setting

**Category:** Email Configuration



### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_INCLUDE_TYPES |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | !Inventory,* |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_INCLUDE_TYPES'
```
