# NO_PO_EMAIL - iPurchase System Setting

**Category:** Email Configuration

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is NO_PO_EMAIL?
- What does NO_PO_EMAIL do?
- What is the default value for NO_PO_EMAIL?
- How do I configure NO_PO_EMAIL?
- How does NO_PO_EMAIL affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PO_EMAIL |
| **Category** | Email Configuration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PO_EMAIL'
```
