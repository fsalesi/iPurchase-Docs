# ALLOW_DELETE_PROCESSED - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has been approved and a PO is already created.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_DELETE_PROCESSED?
- What does ALLOW_DELETE_PROCESSED do?
- What is the default value for ALLOW_DELETE_PROCESSED?
- How do I configure ALLOW_DELETE_PROCESSED?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_PROCESSED |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_PROCESSED'
```
