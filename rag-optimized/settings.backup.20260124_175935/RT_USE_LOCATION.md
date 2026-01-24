# RT_USE_LOCATION - iPurchase System Setting

**Category:** Requisition Types

List of requisition types which will allow a Item Location to be entered during line item entry

**Common questions this answers:**
- What is RT_USE_LOCATION?
- What does RT_USE_LOCATION do?
- What is the default value for RT_USE_LOCATION?
- How do I configure RT_USE_LOCATION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_USE_LOCATION |
| **Category** | Requisition Types |
| **Owner** | Purchasing |
| **Default Value** | Inventory |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_USE_LOCATION'
```
