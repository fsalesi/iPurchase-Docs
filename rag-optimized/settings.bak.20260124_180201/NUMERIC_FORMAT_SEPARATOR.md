# NUMERIC_FORMAT_SEPARATOR - iPurchase System Setting

**Category:** Uncategorized

Usually a comma

**Common questions this answers:**
- What is NUMERIC_FORMAT_SEPARATOR?
- What does NUMERIC_FORMAT_SEPARATOR do?
- What is the default value for NUMERIC_FORMAT_SEPARATOR?
- How do I configure NUMERIC_FORMAT_SEPARATOR?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NUMERIC_FORMAT_SEPARATOR |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | , |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NUMERIC_FORMAT_SEPARATOR'
```
