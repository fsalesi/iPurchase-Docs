# UP_ONLY_REQ_TYPES - iPurchase System Setting

**Category:** Change Orders

Comma-separated requisition types. Types that use UP_ONLY (Update PO Only) routing rule.

**Common questions this answers:**
- What is UP_ONLY_REQ_TYPES?
- What does UP_ONLY_REQ_TYPES do?
- What is the default value for UP_ONLY_REQ_TYPES?
- How do I configure UP_ONLY_REQ_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UP_ONLY_REQ_TYPES |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UP_ONLY_REQ_TYPES'
```
