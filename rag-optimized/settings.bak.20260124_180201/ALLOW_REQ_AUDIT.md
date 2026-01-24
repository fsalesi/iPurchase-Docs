# ALLOW_REQ_AUDIT - iPurchase System Setting

**Category:** User Management

Can-Do list. Users/groups allowed to view requisition audit trail. Automatically disabled in archive systems.

**Common questions this answers:**
- What is ALLOW_REQ_AUDIT?
- What does ALLOW_REQ_AUDIT do?
- What is the default value for ALLOW_REQ_AUDIT?
- How do I configure ALLOW_REQ_AUDIT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_REQ_AUDIT |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_REQ_AUDIT'
```
