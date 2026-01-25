# USE_LYNC - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator to allow the use of Lync within the iPurchase solution.

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
| **Setting Name** | USE_LYNC |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_LYNC'
```

### Related Settings

- [USE_CHAINED_DELEGATES](USE_CHAINED_DELEGATES.md)
- [USE_SINGLE_LANGUAGE](USE_SINGLE_LANGUAGE.md)
