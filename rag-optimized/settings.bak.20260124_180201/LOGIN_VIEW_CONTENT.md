# LOGIN_VIEW_CONTENT - iPurchase System Setting

**Category:** Security & Authentication

This setting allows the administrator to turn off the recent news, events, and video sections from the login page.  To turn these functions off the administrator would need to change the default se...

**Common questions this answers:**
- What is LOGIN_VIEW_CONTENT?
- What does LOGIN_VIEW_CONTENT do?
- What is the default value for LOGIN_VIEW_CONTENT?
- How do I configure LOGIN_VIEW_CONTENT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_VIEW_CONTENT |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | 1,0,1 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_VIEW_CONTENT'
```
