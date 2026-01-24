# PASSWORD_RULES - iPurchase System Setting

**Category:** Security & Authentication

Comma-Separated list of preferences (no spaces). There are 7 entries in this field: 1. Require a number in the password 2. Require a non alpha-numeric character in the password 3. Require a number ...

**Common questions this answers:**
- What is PASSWORD_RULES?
- What does PASSWORD_RULES do?
- What is the default value for PASSWORD_RULES?
- How do I configure PASSWORD_RULES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_RULES |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 1,0,0,0,0,6,0 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_RULES'
```
