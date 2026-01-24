# UP_ONLY_APP_LEVEL_EXCLUDED - iPurchase System Setting

**Category:** Change Orders

Comma-separated approval levels. Approval levels to exclude from UP_ONLY rule evaluation.

**Common questions this answers:**
- What is UP_ONLY_APP_LEVEL_EXCLUDED?
- What does UP_ONLY_APP_LEVEL_EXCLUDED do?
- What is the default value for UP_ONLY_APP_LEVEL_EXCLUDED?
- How do I configure UP_ONLY_APP_LEVEL_EXCLUDED?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UP_ONLY_APP_LEVEL_EXCLUDED |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UP_ONLY_APP_LEVEL_EXCLUDED'
```
