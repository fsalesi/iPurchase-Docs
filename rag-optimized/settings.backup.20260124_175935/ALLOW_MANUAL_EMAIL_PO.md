# ALLOW_MANUAL_EMAIL_PO - iPurchase System Setting

**Category:** Email Configuration

Comma-Separated list of User ID's or Group ID's. that will have the "Email PO" option which would allow a user to email the PO through iPurchase. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_MANUAL_EMAIL_PO?
- What does ALLOW_MANUAL_EMAIL_PO do?
- What is the default value for ALLOW_MANUAL_EMAIL_PO?
- How do I configure ALLOW_MANUAL_EMAIL_PO?
- How does ALLOW_MANUAL_EMAIL_PO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_MANUAL_EMAIL_PO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_MANUAL_EMAIL_PO'
```
