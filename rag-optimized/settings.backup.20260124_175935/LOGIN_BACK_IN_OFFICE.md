# LOGIN_BACK_IN_OFFICE - iPurchase System Setting

**Category:** Security & Authentication

If you currently have the Out-Of-Office setting on, this setting can automatically turn it off when you login. A setting of "ASK" will prompt the user if they want to turn off OOF, but only once ev...

**Common questions this answers:**
- What is LOGIN_BACK_IN_OFFICE?
- What does LOGIN_BACK_IN_OFFICE do?
- What is the default value for LOGIN_BACK_IN_OFFICE?
- How do I configure LOGIN_BACK_IN_OFFICE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_BACK_IN_OFFICE |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | ASK |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_BACK_IN_OFFICE'
```
