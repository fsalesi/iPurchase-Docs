# ALLOW_DELETE_NOT_SUBMITTED - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has not been submitted.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_DELETE_NOT_SUBMITTED?
- What does ALLOW_DELETE_NOT_SUBMITTED do?
- What is the default value for ALLOW_DELETE_NOT_SUBMITTED?
- How do I configure ALLOW_DELETE_NOT_SUBMITTED?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_NOT_SUBMITTED |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_NOT_SUBMITTED'
```
