# LOGIN_GOTO_CATALOG - iPurchase System Setting

**Category:** Security & Authentication

Comma Separated list of User ID's or Group ID's that will be directed to the catalog screen as their landing page. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is LOGIN_GOTO_CATALOG?
- What does LOGIN_GOTO_CATALOG do?
- What is the default value for LOGIN_GOTO_CATALOG?
- How do I configure LOGIN_GOTO_CATALOG?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_GOTO_CATALOG |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_GOTO_CATALOG'
```
