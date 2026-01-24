# DEFAULT_SHIPTO - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for "Ship To" field.

**Common questions this answers:**
- What is DEFAULT_SHIPTO?
- What does DEFAULT_SHIPTO do?
- What is the default value for DEFAULT_SHIPTO?
- How do I configure DEFAULT_SHIPTO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SHIPTO |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SHIPTO'
```
