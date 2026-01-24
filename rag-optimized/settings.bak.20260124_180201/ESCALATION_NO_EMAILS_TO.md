# ESCALATION_NO_EMAILS_TO - iPurchase System Setting

**Category:** Approval Workflow

Can-Do list. Users/groups who do not receive approval escalation notification emails.

**Common questions this answers:**
- What is ESCALATION_NO_EMAILS_TO?
- What does ESCALATION_NO_EMAILS_TO do?
- What is the default value for ESCALATION_NO_EMAILS_TO?
- How do I configure ESCALATION_NO_EMAILS_TO?
- How does ESCALATION_NO_EMAILS_TO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ESCALATION_NO_EMAILS_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ESCALATION_NO_EMAILS_TO'
```
