# APPROVAL_METRICS_RED - iPurchase System Setting

**Category:** Approval Workflow

This setting allows the administrator to set how long the approval time should take before it will turn red on the approval metrics.  MINUTES

**Common questions this answers:**
- What is APPROVAL_METRICS_RED?
- What does APPROVAL_METRICS_RED do?
- What is the default value for APPROVAL_METRICS_RED?
- How do I configure APPROVAL_METRICS_RED?
- How does APPROVAL_METRICS_RED affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_METRICS_RED |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 90 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_METRICS_RED'
```
