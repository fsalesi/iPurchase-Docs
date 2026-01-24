# APP_RULE_LABELS - iPurchase System Setting

**Category:** Uncategorized

List of labels for the fields listed in setting APP_RULE_FIELDS

**Common questions this answers:**
- What is APP_RULE_LABELS?
- What does APP_RULE_LABELS do?
- What is the default value for APP_RULE_LABELS?
- How do I configure APP_RULE_LABELS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_RULE_LABELS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_RULE_LABELS'
```
