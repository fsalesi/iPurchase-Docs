# LOGIN_USE_AD_CMD - iPurchase System Setting

**Category:** Security & Authentication

Command for AD authentication validation.

**Common questions this answers:**
- What is LOGIN_USE_AD_CMD?
- What does LOGIN_USE_AD_CMD do?
- What is the default value for LOGIN_USE_AD_CMD?
- How do I configure LOGIN_USE_AD_CMD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_USE_AD_CMD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_USE_AD_CMD'
```
