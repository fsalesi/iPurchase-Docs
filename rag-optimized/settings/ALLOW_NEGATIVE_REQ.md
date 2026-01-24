# ALLOW_NEGATIVE_REQ - iPurchase System Setting

**Category:** User Management

This setting will allow negative total requisition cost if set to True.

**Common questions this answers:**
- What is ALLOW_NEGATIVE_REQ?
- What does ALLOW_NEGATIVE_REQ do?
- What is the default value for ALLOW_NEGATIVE_REQ?
- How do I configure ALLOW_NEGATIVE_REQ?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_NEGATIVE_REQ |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_NEGATIVE_REQ'
```
