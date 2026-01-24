# SSO_CLIENT_REDIRECT_URL - iPurchase System Setting

**Category:** Security & Authentication

URL to redirect to after SSO authentication.

**Common questions this answers:**
- What is SSO_CLIENT_REDIRECT_URL?
- What does SSO_CLIENT_REDIRECT_URL do?
- What is the default value for SSO_CLIENT_REDIRECT_URL?
- How do I configure SSO_CLIENT_REDIRECT_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SSO_CLIENT_REDIRECT_URL |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SSO_CLIENT_REDIRECT_URL'
```
