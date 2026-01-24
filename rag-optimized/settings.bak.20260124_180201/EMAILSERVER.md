# EMAILSERVER - iPurchase System Setting

**Category:** Email Configuration

IP Address of SMTP Server. This is the IP Address of the SMTP Server from which iPurchase sends all emails.

**Common questions this answers:**
- What is EMAILSERVER?
- What does EMAILSERVER do?
- What is the default value for EMAILSERVER?
- How do I configure EMAILSERVER?
- How does EMAILSERVER affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILSERVER |
| **Category** | Email Configuration |
| **Owner** | IT |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILSERVER'
```
