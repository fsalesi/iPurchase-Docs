# REQ_INQUIRY_BUYER_ALWAYS - iPurchase System Setting

**Category:** Requisitions

TRUE | FALSE. If TRUE, buyers can always see all requisitions in inquiry.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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