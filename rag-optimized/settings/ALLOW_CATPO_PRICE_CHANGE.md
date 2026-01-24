# ALLOW_CATPO_PRICE_CHANGE - iPurchase System Setting

**Category:** User Management

Comma separated list of User IDs or Group ID's that are allowed to change prices on catalog and punchout items. Asterisk indicates everyone, a blank indicates no one

**Common questions this answers:**
- What is ALLOW_CATPO_PRICE_CHANGE?
- What does ALLOW_CATPO_PRICE_CHANGE do?
- What is the default value for ALLOW_CATPO_PRICE_CHANGE?
- How do I configure ALLOW_CATPO_PRICE_CHANGE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CATPO_PRICE_CHANGE |
| **Category** | User Management |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CATPO_PRICE_CHANGE'
```
