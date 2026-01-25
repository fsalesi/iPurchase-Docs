# USE_SINGLE_LANGUAGE - iPurchase System Setting

**Category:** Uncategorized

If this is set to something like en-us"

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_SINGLE_LANGUAGE |
| **Category** | Uncategorized |
| **Owner** | then this will be the language selected for all users and the language selection box on the login screen will not be displayed." |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_SINGLE_LANGUAGE'
```

### Related Settings

- [USE_CHAINED_DELEGATES](USE_CHAINED_DELEGATES.md)
- [USE_LYNC](USE_LYNC.md)