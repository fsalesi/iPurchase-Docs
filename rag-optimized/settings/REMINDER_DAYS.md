# REMINDER_DAYS - iPurchase System Setting

**Category:** Approval Workflow

Numeric.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMINDER_DAYS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMINDER_DAYS'
```