# REMOVE_ORIG_CO - iPurchase System Setting

**Category:** Uncategorized

This setting does not allow originator to be an approver for their own requisition for Change Orders if set to true.

**Common questions this answers:**
- What is REMOVE_ORIG_CO?
- What does REMOVE_ORIG_CO do?
- What is the default value for REMOVE_ORIG_CO?
- How do I configure REMOVE_ORIG_CO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_ORIG_CO |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIG_CO'
```
