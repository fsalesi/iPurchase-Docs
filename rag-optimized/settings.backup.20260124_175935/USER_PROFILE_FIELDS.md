# USER_PROFILE_FIELDS - iPurchase System Setting

**Category:** User Management

Comma-separated field names. Custom user profile fields to display/edit.

**Common questions this answers:**
- What is USER_PROFILE_FIELDS?
- What does USER_PROFILE_FIELDS do?
- What is the default value for USER_PROFILE_FIELDS?
- How do I configure USER_PROFILE_FIELDS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_PROFILE_FIELDS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_PROFILE_FIELDS'
```
