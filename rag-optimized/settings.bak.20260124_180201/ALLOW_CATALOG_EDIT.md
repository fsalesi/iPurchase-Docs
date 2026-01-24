# ALLOW_CATALOG_EDIT - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are who are allowed to edit items in a Catalog within iPurchase. Asterisk indicates everyone, a blank indicates no one. In order for the user to...

**Common questions this answers:**
- What is ALLOW_CATALOG_EDIT?
- What does ALLOW_CATALOG_EDIT do?
- What is the default value for ALLOW_CATALOG_EDIT?
- How do I configure ALLOW_CATALOG_EDIT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CATALOG_EDIT |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CATALOG_EDIT'
```
