# SHOW_ALLOCATION_CODES - iPurchase System Setting

**Category:** Uncategorized

True/false to Show/Hide allocation codes in the account dropdown in req line maintenance.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This display setting controls what information is visible to users in the interface.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_ALLOCATION_CODES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_ALLOCATION_CODES'
```

### Related Settings

- [SHOW_GRAPH](SHOW_GRAPH.md)
- [SHOW_RULE_INFO](SHOW_RULE_INFO.md)
