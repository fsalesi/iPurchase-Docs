# SHOW_GRAPH - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or group ID's that have access to the graphing functionality. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is SHOW_GRAPH?
- What does SHOW_GRAPH do?
- What is the default value for SHOW_GRAPH?
- How do I configure SHOW_GRAPH?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_GRAPH |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_GRAPH'
```
