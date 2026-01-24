# DEFAULT_FREIGHTTERMS - iPurchase System Setting

**Category:** System Configuration

Administrator can set the default value for "Who's Paying Freight" field.

**Common questions this answers:**
- What is DEFAULT_FREIGHTTERMS?
- What does DEFAULT_FREIGHTTERMS do?
- What is the default value for DEFAULT_FREIGHTTERMS?
- How do I configure DEFAULT_FREIGHTTERMS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_FREIGHTTERMS |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_FREIGHTTERMS'
```
