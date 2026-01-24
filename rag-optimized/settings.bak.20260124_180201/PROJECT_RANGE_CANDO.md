# PROJECT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

Can-Do list. Valid project codes. Default * allows all.

**Common questions this answers:**
- What is PROJECT_RANGE_CANDO?
- What does PROJECT_RANGE_CANDO do?
- What is the default value for PROJECT_RANGE_CANDO?
- How do I configure PROJECT_RANGE_CANDO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PROJECT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PROJECT_RANGE_CANDO'
```
