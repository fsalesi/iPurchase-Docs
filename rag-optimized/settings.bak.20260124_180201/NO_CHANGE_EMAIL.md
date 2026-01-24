# NO_CHANGE_EMAIL - iPurchase System Setting

**Category:** Email Configuration

If an approver changes a requisition and this is set to true, then the originator will not be notified.

**Common questions this answers:**
- What is NO_CHANGE_EMAIL?
- What does NO_CHANGE_EMAIL do?
- What is the default value for NO_CHANGE_EMAIL?
- How do I configure NO_CHANGE_EMAIL?
- How does NO_CHANGE_EMAIL affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_CHANGE_EMAIL |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_CHANGE_EMAIL'
```
