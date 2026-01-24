# CO_REROUTE_EXCLUDE_TYPES - iPurchase System Setting

**Category:** Change Orders

Comma-separated requisition types. Types excluded from change order re-routing even when changes are material.

**Common questions this answers:**
- What is CO_REROUTE_EXCLUDE_TYPES?
- What does CO_REROUTE_EXCLUDE_TYPES do?
- What is the default value for CO_REROUTE_EXCLUDE_TYPES?
- How do I configure CO_REROUTE_EXCLUDE_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_REROUTE_EXCLUDE_TYPES |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_REROUTE_EXCLUDE_TYPES'
```
