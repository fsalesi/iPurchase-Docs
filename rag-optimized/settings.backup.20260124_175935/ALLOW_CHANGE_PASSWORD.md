# ALLOW_CHANGE_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User IDs or Group ID's that are allowed to change passwords. Asterisk indicates everyone, a blank indicates no one. This setting determines whether a user will have the opti...

**Common questions this answers:**
- What is ALLOW_CHANGE_PASSWORD?
- What does ALLOW_CHANGE_PASSWORD do?
- What is the default value for ALLOW_CHANGE_PASSWORD?
- How do I configure ALLOW_CHANGE_PASSWORD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CHANGE_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CHANGE_PASSWORD'
```
