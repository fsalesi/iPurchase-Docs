# PROD_LINES_DERMIS - iPurchase System Setting

**Category:** Custom/Product Management

Product line categorization for Dermis business unit. Customer-specific.

**Common questions this answers:**
- What is PROD_LINES_DERMIS?
- What does PROD_LINES_DERMIS do?
- What is the default value for PROD_LINES_DERMIS?
- How do I configure PROD_LINES_DERMIS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PROD_LINES_DERMIS |
| **Category** | Custom/Product Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PROD_LINES_DERMIS'
```
