# PURGE_REQ_DAYS - iPurchase System Setting

**Category:** Requisitions

This setting allows the administrator to set how many days a requisition will be purged based on no activity from either the entry date, last audit record date(header or detail), or last approval r...

**Common questions this answers:**
- What is PURGE_REQ_DAYS?
- What does PURGE_REQ_DAYS do?
- What is the default value for PURGE_REQ_DAYS?
- How do I configure PURGE_REQ_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PURGE_REQ_DAYS |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | 90 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PURGE_REQ_DAYS'
```
