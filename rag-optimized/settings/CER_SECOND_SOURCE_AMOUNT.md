# CER_SECOND_SOURCE_AMOUNT - iPurchase System Setting

**Category:** Catalog & Vendors

Dollar amount. Threshold above which second source certification is required. Related to competitive bidding requirements.

**Common questions this answers:**
- What is CER_SECOND_SOURCE_AMOUNT?
- What does CER_SECOND_SOURCE_AMOUNT do?
- What is the default value for CER_SECOND_SOURCE_AMOUNT?
- How do I configure CER_SECOND_SOURCE_AMOUNT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CER_SECOND_SOURCE_AMOUNT |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CER_SECOND_SOURCE_AMOUNT'
```
