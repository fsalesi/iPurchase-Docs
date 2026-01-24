# EDIT_ANYTIME - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or Group ID's that are allowed to edit a Pending requisition at anytime. Asterisk indicates everyone, a blank indicates no one. There is currently a setting "ALWAY...

**Common questions this answers:**
- What is EDIT_ANYTIME?
- What does EDIT_ANYTIME do?
- What is the default value for EDIT_ANYTIME?
- How do I configure EDIT_ANYTIME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EDIT_ANYTIME |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EDIT_ANYTIME'
```
