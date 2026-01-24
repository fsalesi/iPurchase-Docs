# APPROVAL_EMAIL_REPLY_TO - iPurchase System Setting

**Category:** Approval Workflow

Replies to approval email should go to who? Leave blank for originator. Set to 'OBO' for On behalf of. Set to any single email address.

**Common questions this answers:**
- What is APPROVAL_EMAIL_REPLY_TO?
- What does APPROVAL_EMAIL_REPLY_TO do?
- What is the default value for APPROVAL_EMAIL_REPLY_TO?
- How do I configure APPROVAL_EMAIL_REPLY_TO?
- How does APPROVAL_EMAIL_REPLY_TO affect approval routing?
- How does APPROVAL_EMAIL_REPLY_TO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_EMAIL_REPLY_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_EMAIL_REPLY_TO'
```
