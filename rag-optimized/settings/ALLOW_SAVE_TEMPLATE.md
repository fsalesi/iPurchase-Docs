# ALLOW_SAVE_TEMPLATE - iPurchase System Setting

**Category:** Requisitions

Can-Do list. Users/groups allowed to save requisition templates.

**Common questions this answers:**
- What is ALLOW_SAVE_TEMPLATE?
- What does ALLOW_SAVE_TEMPLATE do?
- What is the default value for ALLOW_SAVE_TEMPLATE?
- How do I configure ALLOW_SAVE_TEMPLATE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_SAVE_TEMPLATE |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_SAVE_TEMPLATE'
```
