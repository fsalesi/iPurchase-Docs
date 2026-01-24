# RT_MRP - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated req types. Types that trigger MRP (Material Requirements Planning).

**Common questions this answers:**
- What is RT_MRP?
- What does RT_MRP do?
- What is the default value for RT_MRP?
- How do I configure RT_MRP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_MRP |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_MRP'
```
