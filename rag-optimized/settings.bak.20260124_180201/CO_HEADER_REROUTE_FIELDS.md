# CO_HEADER_REROUTE_FIELDS - iPurchase System Setting

**Category:** Change Orders

Comma Separated list of header fields which will force a change order to automatically re-route if they are changed.

**Common questions this answers:**
- What is CO_HEADER_REROUTE_FIELDS?
- What does CO_HEADER_REROUTE_FIELDS do?
- What is the default value for CO_HEADER_REROUTE_FIELDS?
- How do I configure CO_HEADER_REROUTE_FIELDS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_HEADER_REROUTE_FIELDS |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_HEADER_REROUTE_FIELDS'
```
