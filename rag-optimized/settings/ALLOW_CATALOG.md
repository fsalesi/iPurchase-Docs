# ALLOW_CATALOG - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that have access to the catalog function within iPurchase.

**Common questions this answers:**
- What is ALLOW_CATALOG?
- What does ALLOW_CATALOG do?
- What is the default value for ALLOW_CATALOG?
- How do I configure ALLOW_CATALOG?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CATALOG |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CATALOG'
```
