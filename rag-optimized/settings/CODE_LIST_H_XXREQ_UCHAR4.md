# CODE_LIST_H_XXREQ_UCHAR4 - iPurchase System Setting

**Category:** Requisitions

List for User Field 4

### How It Works

This setting configures requisitions behavior in iPurchase.

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

### Related Settings

- [CODE_LIST_H_XXREQ_UCHAR1](CODE_LIST_H_XXREQ_UCHAR1.md)
- [CODE_LIST_H_XXREQ_UCHAR2](CODE_LIST_H_XXREQ_UCHAR2.md)
- [CODE_LIST_H_XXREQ_UCHAR3](CODE_LIST_H_XXREQ_UCHAR3.md)
