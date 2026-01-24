# CATALOG_ALLOW_IMPORT - iPurchase System Setting

**Category:** User Management

Comma Separated list of User ID's or Group ID's that are allowed to import catalogs.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is CATALOG_ALLOW_IMPORT?
- What does CATALOG_ALLOW_IMPORT do?
- What is the default value for CATALOG_ALLOW_IMPORT?
- How do I configure CATALOG_ALLOW_IMPORT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_ALLOW_IMPORT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_ALLOW_IMPORT'
```
