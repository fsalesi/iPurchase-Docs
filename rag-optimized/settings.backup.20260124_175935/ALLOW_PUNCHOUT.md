# ALLOW_PUNCHOUT - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to use punchouts. Asterisk indicates everyone, a blank indicates no one. This setting turns on or off the Punch-out functionality fo...

**Common questions this answers:**
- What is ALLOW_PUNCHOUT?
- What does ALLOW_PUNCHOUT do?
- What is the default value for ALLOW_PUNCHOUT?
- How do I configure ALLOW_PUNCHOUT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_PUNCHOUT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_PUNCHOUT'
```
