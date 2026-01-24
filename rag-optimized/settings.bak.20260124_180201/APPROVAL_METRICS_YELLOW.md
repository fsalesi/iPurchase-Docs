# APPROVAL_METRICS_YELLOW - iPurchase System Setting

**Category:** Approval Workflow

This setting allows the administrator to set how long the approval time should take before it will turn yellow on the approval metrics. MINUTES

**Common questions this answers:**
- What is APPROVAL_METRICS_YELLOW?
- What does APPROVAL_METRICS_YELLOW do?
- What is the default value for APPROVAL_METRICS_YELLOW?
- How do I configure APPROVAL_METRICS_YELLOW?
- How does APPROVAL_METRICS_YELLOW affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_METRICS_YELLOW |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 30 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_METRICS_YELLOW'
```
