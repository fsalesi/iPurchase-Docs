# TERMS_DISPLAY - iPurchase System Setting

**Category:** Uncategorized

This setting will display the supplier terms on the requisition header.

**Common questions this answers:**
- What is TERMS_DISPLAY?
- What does TERMS_DISPLAY do?
- What is the default value for TERMS_DISPLAY?
- How do I configure TERMS_DISPLAY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TERMS_DISPLAY |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TERMS_DISPLAY'
```
