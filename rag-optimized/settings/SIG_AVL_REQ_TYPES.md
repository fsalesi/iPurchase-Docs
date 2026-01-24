# SIG_AVL_REQ_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-separated types. Types using signature-based approved vendor list. Related: AVL_REQ_TYPES, USE_SIG_AVL

**Common questions this answers:**
- What is SIG_AVL_REQ_TYPES?
- What does SIG_AVL_REQ_TYPES do?
- What is the default value for SIG_AVL_REQ_TYPES?
- How do I configure SIG_AVL_REQ_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SIG_AVL_REQ_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SIG_AVL_REQ_TYPES'
```
