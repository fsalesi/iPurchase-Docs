# INQUIRY_ALLOW_VIEWS - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to see views.

**Common questions this answers:**
- What is INQUIRY_ALLOW_VIEWS?
- What does INQUIRY_ALLOW_VIEWS do?
- What is the default value for INQUIRY_ALLOW_VIEWS?
- How do I configure INQUIRY_ALLOW_VIEWS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_ALLOW_VIEWS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_ALLOW_VIEWS'
```
