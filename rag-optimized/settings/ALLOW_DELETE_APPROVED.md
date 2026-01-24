# ALLOW_DELETE_APPROVED - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's who are allowed to delete an approved requisition.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_DELETE_APPROVED?
- What does ALLOW_DELETE_APPROVED do?
- What is the default value for ALLOW_DELETE_APPROVED?
- How do I configure ALLOW_DELETE_APPROVED?
- How does ALLOW_DELETE_APPROVED affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_APPROVED |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_APPROVED'
```
