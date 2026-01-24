# ITEM_SEARCH_RECENT - iPurchase System Setting

**Category:** Uncategorized

When entering line items

**Common questions this answers:**
- What is ITEM_SEARCH_RECENT?
- What does ITEM_SEARCH_RECENT do?
- What is the default value for ITEM_SEARCH_RECENT?
- How do I configure ITEM_SEARCH_RECENT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ITEM_SEARCH_RECENT |
| **Category** | Uncategorized |
| **Owner** | iPurchase will look for matches from previous requisitions." |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ITEM_SEARCH_RECENT'
```
