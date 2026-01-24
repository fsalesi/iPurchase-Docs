# DATE_FORMAT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator to globally change the format of the date fields in iPurchase.

**Common questions this answers:**
- What is DATE_FORMAT?
- What does DATE_FORMAT do?
- What is the default value for DATE_FORMAT?
- How do I configure DATE_FORMAT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DATE_FORMAT |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | mdy |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DATE_FORMAT'
```
