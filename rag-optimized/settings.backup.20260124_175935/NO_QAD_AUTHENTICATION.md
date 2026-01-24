# NO_QAD_AUTHENTICATION - iPurchase System Setting

**Category:** Security & Authentication

Do not use QAD passwords for users that are also in QAD. Let iPurchase manage those passwords.

**Common questions this answers:**
- What is NO_QAD_AUTHENTICATION?
- What does NO_QAD_AUTHENTICATION do?
- What is the default value for NO_QAD_AUTHENTICATION?
- How do I configure NO_QAD_AUTHENTICATION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_QAD_AUTHENTICATION |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | true |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_QAD_AUTHENTICATION'
```
