# ITEM_LOOKUP_NO_VP - iPurchase System Setting

**Category:** Uncategorized

Do not show vendor parts (vp_mstr) when searching for items in line entry.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ITEM_LOOKUP_NO_VP |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ITEM_LOOKUP_NO_VP'
```