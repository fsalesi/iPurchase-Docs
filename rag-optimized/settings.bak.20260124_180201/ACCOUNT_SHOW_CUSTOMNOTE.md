# ACCOUNT_SHOW_CUSTOMNOTE - iPurchase System Setting

**Category:** GL Accounts & Finance

Show the value CustomNote Field on the GL record - only for EE

**Common questions this answers:**
- What is ACCOUNT_SHOW_CUSTOMNOTE?
- What does ACCOUNT_SHOW_CUSTOMNOTE do?
- What is the default value for ACCOUNT_SHOW_CUSTOMNOTE?
- How do I configure ACCOUNT_SHOW_CUSTOMNOTE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_SHOW_CUSTOMNOTE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_SHOW_CUSTOMNOTE'
```
