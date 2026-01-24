# REMOVE_SAVE_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Removes the options of saving your password on the login screen. Users will need to enter their password every time.

**Common questions this answers:**
- What is REMOVE_SAVE_PASSWORD?
- What does REMOVE_SAVE_PASSWORD do?
- What is the default value for REMOVE_SAVE_PASSWORD?
- How do I configure REMOVE_SAVE_PASSWORD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_SAVE_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_SAVE_PASSWORD'
```
