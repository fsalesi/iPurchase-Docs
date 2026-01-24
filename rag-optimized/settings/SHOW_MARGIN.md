# SHOW_MARGIN - iPurchase System Setting

**Category:** Catalog & Vendors

Can-Do list. Users allowed to see profit margins.

**Common questions this answers:**
- What is SHOW_MARGIN?
- What does SHOW_MARGIN do?
- What is the default value for SHOW_MARGIN?
- How do I configure SHOW_MARGIN?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_MARGIN |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_MARGIN'
```
