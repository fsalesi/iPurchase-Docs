# DELIVER_TO_BLANK_DEFAULT - iPurchase System Setting

**Category:** Requisitions

Default deliver-to value used when deliver-to field is left blank on requisition.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DELIVER_TO_BLANK_DEFAULT |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DELIVER_TO_BLANK_DEFAULT'
```