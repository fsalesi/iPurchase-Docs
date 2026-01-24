# ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR - iPurchase System Setting

**Category:** User Management

The users listed here will be allowed to modify a requisition while it's being approved if the following scenarios are true: 1) They are listed as the originator or on behalf of. 2) They are an app...

**Common questions this answers:**
- What is ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR?
- What does ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR do?
- What is the default value for ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR?
- How do I configure ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR'
```
