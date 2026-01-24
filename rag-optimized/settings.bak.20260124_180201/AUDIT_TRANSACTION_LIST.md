# AUDIT_TRANSACTION_LIST - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is AUDIT_TRANSACTION_LIST?
- What does AUDIT_TRANSACTION_LIST do?
- What is the default value for AUDIT_TRANSACTION_LIST?
- How do I configure AUDIT_TRANSACTION_LIST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRANSACTION_LIST |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRANSACTION_LIST'
```
