# ALLOW_NEW_REQUEST - iPurchase System Setting

**Category:** Requisitions

Can-Do list. Users/groups allowed to create new requisitions. Controls visibility of New Request button in UI.

**Common questions this answers:**
- What is ALLOW_NEW_REQUEST?
- What does ALLOW_NEW_REQUEST do?
- What is the default value for ALLOW_NEW_REQUEST?
- How do I configure ALLOW_NEW_REQUEST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_NEW_REQUEST |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_NEW_REQUEST'
```
