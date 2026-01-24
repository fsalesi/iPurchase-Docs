# REQUISITION_PREFIX - iPurchase System Setting

**Category:** Requisitions

This setting allows the administrator to set a special character to be used for the requisition prefix.

**Common questions this answers:**
- What is REQUISITION_PREFIX?
- What does REQUISITION_PREFIX do?
- What is the default value for REQUISITION_PREFIX?
- How do I configure REQUISITION_PREFIX?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQUISITION_PREFIX |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | T |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQUISITION_PREFIX'
```
