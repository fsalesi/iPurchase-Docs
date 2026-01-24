# LOGIN_USE_AD_URL - iPurchase System Setting

**Category:** Security & Authentication

URL for AD authentication service.

**Common questions this answers:**
- What is LOGIN_USE_AD_URL?
- What does LOGIN_USE_AD_URL do?
- What is the default value for LOGIN_USE_AD_URL?
- How do I configure LOGIN_USE_AD_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_USE_AD_URL |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_USE_AD_URL'
```
