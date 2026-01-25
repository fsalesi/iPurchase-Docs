# APP_RULE_FIELDS - iPurchase System Setting

**Category:** Uncategorized

List of field name from xxreq_mstr and xxreqd_det which appear in the Approval Rule Maintenance Screen for which you want to change the labels for.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_RULE_FIELDS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_RULE_FIELDS'
```

### Related Settings

- [APP_RULE_LABELS](APP_RULE_LABELS.md)
- [APP_RULE_SKIP_FIELDS](APP_RULE_SKIP_FIELDS.md)
