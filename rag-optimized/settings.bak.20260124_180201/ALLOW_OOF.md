# ALLOW_OOF - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to set Out of office. Asterisk indicates everyone, a blank indicates no one. This setting determines whether the system will support...

**Common questions this answers:**
- What is ALLOW_OOF?
- What does ALLOW_OOF do?
- What is the default value for ALLOW_OOF?
- How do I configure ALLOW_OOF?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_OOF |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_OOF'
```
