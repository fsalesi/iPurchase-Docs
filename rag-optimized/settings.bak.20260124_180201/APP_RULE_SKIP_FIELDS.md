# APP_RULE_SKIP_FIELDS - iPurchase System Setting

**Category:** Uncategorized

List of fields from xxreq_mstr and xxreqd_det that you don't want to show in the Approval Rule Maintenance Screen.

**Common questions this answers:**
- What is APP_RULE_SKIP_FIELDS?
- What does APP_RULE_SKIP_FIELDS do?
- What is the default value for APP_RULE_SKIP_FIELDS?
- How do I configure APP_RULE_SKIP_FIELDS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_RULE_SKIP_FIELDS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_RULE_SKIP_FIELDS'
```
