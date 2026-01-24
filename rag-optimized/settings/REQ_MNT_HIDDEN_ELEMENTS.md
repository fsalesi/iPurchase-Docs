# REQ_MNT_HIDDEN_ELEMENTS - iPurchase System Setting

**Category:** Requisitions

Technical - Do Not Modify without consulting ISS

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_MNT_HIDDEN_ELEMENTS |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_MNT_HIDDEN_ELEMENTS'
```
