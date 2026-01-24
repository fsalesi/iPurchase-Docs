# CODE_LIST_H_XXREQ_UCHAR4 - iPurchase System Setting

**Category:** Requisitions

List for User Field 4

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_XXREQ_UCHAR4 |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | List:True:True,False:False |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_XXREQ_UCHAR4'
```