# PASSWORD_RESET_TIMEOUT - iPurchase System Setting

**Category:** Security & Authentication

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is PASSWORD_RESET_TIMEOUT?
- What does PASSWORD_RESET_TIMEOUT do?
- What is the default value for PASSWORD_RESET_TIMEOUT?
- How do I configure PASSWORD_RESET_TIMEOUT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_RESET_TIMEOUT |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_RESET_TIMEOUT'
```
