# GL_OVERRIDE - iPurchase System Setting

**Category:** GL Accounts & Finance

If you set this setting to true, then all items entered in the line entry screen will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor an...

**Common questions this answers:**
- What is GL_OVERRIDE?
- What does GL_OVERRIDE do?
- What is the default value for GL_OVERRIDE?
- How do I configure GL_OVERRIDE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | GL_OVERRIDE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'GL_OVERRIDE'
```
