# CO_ITEM_REROUTE_NEW - iPurchase System Setting

**Category:** Change Orders

Automatically re-route a change order if a new line is added to the requisition.

**Common questions this answers:**
- What is CO_ITEM_REROUTE_NEW?
- What does CO_ITEM_REROUTE_NEW do?
- What is the default value for CO_ITEM_REROUTE_NEW?
- How do I configure CO_ITEM_REROUTE_NEW?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_ITEM_REROUTE_NEW |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_ITEM_REROUTE_NEW'
```
