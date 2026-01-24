# EMAIL_OPEN_PO_INCLUDE_USERS - iPurchase System Setting

**Category:** Email Configuration



**Common questions this answers:**
- What is EMAIL_OPEN_PO_INCLUDE_USERS?
- What does EMAIL_OPEN_PO_INCLUDE_USERS do?
- What is the default value for EMAIL_OPEN_PO_INCLUDE_USERS?
- How do I configure EMAIL_OPEN_PO_INCLUDE_USERS?
- How does EMAIL_OPEN_PO_INCLUDE_USERS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_INCLUDE_USERS |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_INCLUDE_USERS'
```
