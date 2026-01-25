# REQ_INQUIRY_BUYER_ALWAYS - iPurchase System Setting

**Category:** Requisitions

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | buyers can always see all requisitions in inquiry |
| **FALSE** | Disables this feature |

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_INQUIRY_BUYER_ALWAYS |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_INQUIRY_BUYER_ALWAYS'
```

### Related Settings

- [REQ_INQUIRY_FIELDS](REQ_INQUIRY_FIELDS.md)
- [REQ_INQ_HIDDEN_ELEMENTS](REQ_INQ_HIDDEN_ELEMENTS.md)
- [REQ_MNT_HIDDEN_ELEMENTS](REQ_MNT_HIDDEN_ELEMENTS.md)
