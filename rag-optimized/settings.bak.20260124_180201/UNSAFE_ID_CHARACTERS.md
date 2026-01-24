# UNSAFE_ID_CHARACTERS - iPurchase System Setting

**Category:** Security & Authentication

Characters prohibited in user IDs and identifiers for security.

**Common questions this answers:**
- What is UNSAFE_ID_CHARACTERS?
- What does UNSAFE_ID_CHARACTERS do?
- What is the default value for UNSAFE_ID_CHARACTERS?
- How do I configure UNSAFE_ID_CHARACTERS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UNSAFE_ID_CHARACTERS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UNSAFE_ID_CHARACTERS'
```
