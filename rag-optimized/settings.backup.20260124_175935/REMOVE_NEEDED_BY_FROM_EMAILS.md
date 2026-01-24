# REMOVE_NEEDED_BY_FROM_EMAILS - iPurchase System Setting

**Category:** Email Configuration

Show 'Needed By 99/99/9999' in the approval email subject.

**Common questions this answers:**
- What is REMOVE_NEEDED_BY_FROM_EMAILS?
- What does REMOVE_NEEDED_BY_FROM_EMAILS do?
- What is the default value for REMOVE_NEEDED_BY_FROM_EMAILS?
- How do I configure REMOVE_NEEDED_BY_FROM_EMAILS?
- How does REMOVE_NEEDED_BY_FROM_EMAILS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_NEEDED_BY_FROM_EMAILS |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_NEEDED_BY_FROM_EMAILS'
```
