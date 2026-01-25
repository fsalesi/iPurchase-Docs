# ITEM_SEARCH_RECENT - iPurchase System Setting

**Category:** Uncategorized

When entering line items

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ITEM_SEARCH_RECENT |
| **Category** | Uncategorized |
| **Owner** | iPurchase will look for matches from previous requisitions." |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ITEM_SEARCH_RECENT'
```

### Related Settings

- [ITEM_LOOKUP_NO_VP](ITEM_LOOKUP_NO_VP.md)