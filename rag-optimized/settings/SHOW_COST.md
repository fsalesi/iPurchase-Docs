# SHOW_COST - iPurchase System Setting

**Category:** Catalog & Vendors

Can-Do list. Users allowed to see item costs.

**Common questions this answers:**
- What is SHOW_COST?
- What does SHOW_COST do?
- What is the default value for SHOW_COST?
- How do I configure SHOW_COST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_COST |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_COST'
```
