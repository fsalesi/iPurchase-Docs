# PRINT_COMMAND - iPurchase System Setting

**Category:** System Configuration

OS command for printing documents (e.g., lp, lpr).

**Common questions this answers:**
- What is PRINT_COMMAND?
- What does PRINT_COMMAND do?
- What is the default value for PRINT_COMMAND?
- How do I configure PRINT_COMMAND?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PRINT_COMMAND |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PRINT_COMMAND'
```
