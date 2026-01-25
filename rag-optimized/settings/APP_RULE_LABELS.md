# APP_RULE_LABELS - iPurchase System Setting

**Category:** Uncategorized

List of labels for the fields listed in setting APP_RULE_FIELDS

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_RULE_LABELS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_RULE_LABELS'
```

### Related Settings

- [APP_RULE_FIELDS](APP_RULE_FIELDS.md)
- [APP_RULE_SKIP_FIELDS](APP_RULE_SKIP_FIELDS.md)