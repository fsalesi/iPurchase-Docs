# INTERNAL_URL - iPurchase System Setting

**Category:** Email Configuration

Internal network URL for application. Used when APPLICATION_URL/BASE_URL are external-facing.

**Common questions this answers:**
- What is INTERNAL_URL?
- What does INTERNAL_URL do?
- What is the default value for INTERNAL_URL?
- How do I configure INTERNAL_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INTERNAL_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INTERNAL_URL'
```
