# EMAILFROM - iPurchase System Setting

**Category:** Email Configuration

AD Email Address This is a valid email address for which all iPurchase emails will be sent from.

**Common questions this answers:**
- What is EMAILFROM?
- What does EMAILFROM do?
- What is the default value for EMAILFROM?
- How do I configure EMAILFROM?
- How does EMAILFROM affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILFROM |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILFROM'
```
