# EMAIL_OPEN_PO_INCLUDE_TYPES - iPurchase System Setting

**Category:** Email Configuration



**Common questions this answers:**
- What is EMAIL_OPEN_PO_INCLUDE_TYPES?
- What does EMAIL_OPEN_PO_INCLUDE_TYPES do?
- What is the default value for EMAIL_OPEN_PO_INCLUDE_TYPES?
- How do I configure EMAIL_OPEN_PO_INCLUDE_TYPES?
- How does EMAIL_OPEN_PO_INCLUDE_TYPES affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_INCLUDE_TYPES |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | !Inventory,* |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_INCLUDE_TYPES'
```
