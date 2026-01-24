# DEFAULT_BUYER_[SITE] - iPurchase System Setting

**Category:** Purchase Orders

This is the userid of the default buyer for the specified site, used on all new requisitions. See DEFAULT_BUYER

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BUYER_[SITE] |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BUYER_[SITE]'
```