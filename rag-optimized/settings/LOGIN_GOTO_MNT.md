# LOGIN_GOTO_MNT - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User ID's or Group ID's that will always be logged into the requisition workbench. This only applies to non-approvers. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is LOGIN_GOTO_MNT?
- What does LOGIN_GOTO_MNT do?
- What is the default value for LOGIN_GOTO_MNT?
- How do I configure LOGIN_GOTO_MNT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_GOTO_MNT |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_GOTO_MNT'
```
