# IPURCHASE_VERSION - iPurchase System Setting

**Category:** Uncategorized

Do Not Modify

**Common questions this answers:**
- What is IPURCHASE_VERSION?
- What does IPURCHASE_VERSION do?
- What is the default value for IPURCHASE_VERSION?
- How do I configure IPURCHASE_VERSION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IPURCHASE_VERSION |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | 2023.0426 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IPURCHASE_VERSION'
```
