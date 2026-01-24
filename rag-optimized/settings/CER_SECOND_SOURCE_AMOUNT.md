# CER_SECOND_SOURCE_AMOUNT - iPurchase System Setting

**Category:** Catalog & Vendors

Dollar amount. Threshold above which second source certification is required. Related to competitive bidding requirements.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CER_SECOND_SOURCE_AMOUNT |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CER_SECOND_SOURCE_AMOUNT'
```