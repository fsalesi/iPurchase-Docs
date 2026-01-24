# ITEM_LOOKUP_NO_VP - iPurchase System Setting

**Category:** Uncategorized

Do not show vendor parts (vp_mstr) when searching for items in line entry.

**Common questions this answers:**
- What is ITEM_LOOKUP_NO_VP?
- What does ITEM_LOOKUP_NO_VP do?
- What is the default value for ITEM_LOOKUP_NO_VP?
- How do I configure ITEM_LOOKUP_NO_VP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ITEM_LOOKUP_NO_VP |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ITEM_LOOKUP_NO_VP'
```
