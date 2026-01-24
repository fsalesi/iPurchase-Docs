# ALWAYS_ALLOW_REQ_EDITS - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to modify any requisition at any time until it has been approved. You may also use "$xxreq_buyer" (without the quotes) as one of the...

**Common questions this answers:**
- What is ALWAYS_ALLOW_REQ_EDITS?
- What does ALWAYS_ALLOW_REQ_EDITS do?
- What is the default value for ALWAYS_ALLOW_REQ_EDITS?
- How do I configure ALWAYS_ALLOW_REQ_EDITS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_REQ_EDITS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_REQ_EDITS'
```
