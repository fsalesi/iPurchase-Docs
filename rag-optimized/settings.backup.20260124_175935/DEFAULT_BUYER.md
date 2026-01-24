# DEFAULT_BUYER - iPurchase System Setting

**Category:** Purchase Orders

This is the userid of the default buyer to be used on all new requisitions. This can be overridden by DEFAULT_BUYER_[SITE], RT_[REQ_TYPE]_DEFAULT_BUYER, RT_[REQ_TYPE]_[SITE]_DEFAULT_BUYER, and vd_b...

**Common questions this answers:**
- What is DEFAULT_BUYER?
- What does DEFAULT_BUYER do?
- What is the default value for DEFAULT_BUYER?
- How do I configure DEFAULT_BUYER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BUYER |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BUYER'
```
