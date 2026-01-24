# BATCH_APPROVE_GROUPS_ALWAYS - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated list of User ID's or Group ID's. By default, the setting BATCH_APPROVE_GROUPS will only allow you to batch approve for requisitions that specifically include yourself. Batch approva...

**Common questions this answers:**
- What is BATCH_APPROVE_GROUPS_ALWAYS?
- What does BATCH_APPROVE_GROUPS_ALWAYS do?
- What is the default value for BATCH_APPROVE_GROUPS_ALWAYS?
- How do I configure BATCH_APPROVE_GROUPS_ALWAYS?
- How does BATCH_APPROVE_GROUPS_ALWAYS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_APPROVE_GROUPS_ALWAYS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_APPROVE_GROUPS_ALWAYS'
```

**Related settings:** BATCH_APPROVE_GROUPS