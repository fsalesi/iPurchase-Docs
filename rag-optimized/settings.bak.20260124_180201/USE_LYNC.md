# USE_LYNC - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator to allow the use of Lync within the iPurchase solution. Requirements: Office 2010+ with Lync installed on desktop. iPurchase website must be in the "TRUSTED SI...

**Common questions this answers:**
- What is USE_LYNC?
- What does USE_LYNC do?
- What is the default value for USE_LYNC?
- How do I configure USE_LYNC?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_LYNC |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_LYNC'
```
