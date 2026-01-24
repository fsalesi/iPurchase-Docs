# REMINDER_DAYS - iPurchase System Setting

**Category:** Approval Workflow

Numeric. Days before sending reminder emails to pending approvers.

**Common questions this answers:**
- What is REMINDER_DAYS?
- What does REMINDER_DAYS do?
- What is the default value for REMINDER_DAYS?
- How do I configure REMINDER_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMINDER_DAYS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMINDER_DAYS'
```
