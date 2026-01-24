# PO_DO_NOT_EMAIL - iPurchase System Setting

**Category:** Email Configuration

If set to true the PO will not be emailed.

**Common questions this answers:**
- What is PO_DO_NOT_EMAIL?
- What does PO_DO_NOT_EMAIL do?
- What is the default value for PO_DO_NOT_EMAIL?
- How do I configure PO_DO_NOT_EMAIL?
- How does PO_DO_NOT_EMAIL affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_DO_NOT_EMAIL |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_DO_NOT_EMAIL'
```
