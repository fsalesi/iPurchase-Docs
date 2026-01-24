# DEFAULT_SITE - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for the "Site" field. Must be a valid site.

**Common questions this answers:**
- What is DEFAULT_SITE?
- What does DEFAULT_SITE do?
- What is the default value for DEFAULT_SITE?
- How do I configure DEFAULT_SITE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SITE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SITE'
```
