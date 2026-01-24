# APP_RULE_FIELDS - iPurchase System Setting

**Category:** Uncategorized

List of field name from xxreq_mstr and xxreqd_det which appear in the Approval Rule Maintenance Screen for which you want to change the labels for. This list must match in size with the list in setting APP_RULE_LABELS. Each field must have an associated label.

### How It Works

See the description above for valid values and usage.

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
