# IGNORE_SPVSR_LOAD - iPurchase System Setting

**Category:** Approval Workflow

Can-Do list. Users to ignore when calculating supervisor approval workload in load balancing.

**Common questions this answers:**
- What is IGNORE_SPVSR_LOAD?
- What does IGNORE_SPVSR_LOAD do?
- What is the default value for IGNORE_SPVSR_LOAD?
- How do I configure IGNORE_SPVSR_LOAD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IGNORE_SPVSR_LOAD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IGNORE_SPVSR_LOAD'
```
