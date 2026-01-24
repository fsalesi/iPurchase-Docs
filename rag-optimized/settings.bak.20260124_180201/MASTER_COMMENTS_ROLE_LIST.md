# MASTER_COMMENTS_ROLE_LIST - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated list of group ID's or "*" for all. Only members of these groups will be allowed to enter or delete master comments from a requisition.

**Common questions this answers:**
- What is MASTER_COMMENTS_ROLE_LIST?
- What does MASTER_COMMENTS_ROLE_LIST do?
- What is the default value for MASTER_COMMENTS_ROLE_LIST?
- How do I configure MASTER_COMMENTS_ROLE_LIST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MASTER_COMMENTS_ROLE_LIST |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MASTER_COMMENTS_ROLE_LIST'
```
