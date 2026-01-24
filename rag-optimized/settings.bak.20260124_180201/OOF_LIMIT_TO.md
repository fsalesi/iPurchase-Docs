# OOF_LIMIT_TO - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or Group ID's that that can be chosen as delegates. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is OOF_LIMIT_TO?
- What does OOF_LIMIT_TO do?
- What is the default value for OOF_LIMIT_TO?
- How do I configure OOF_LIMIT_TO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_TO |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_TO'
```
