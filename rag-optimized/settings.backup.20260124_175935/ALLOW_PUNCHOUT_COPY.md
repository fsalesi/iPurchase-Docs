# ALLOW_PUNCHOUT_COPY - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to copy punchout requisitions (prices may no longer be valid). Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_PUNCHOUT_COPY?
- What does ALLOW_PUNCHOUT_COPY do?
- What is the default value for ALLOW_PUNCHOUT_COPY?
- How do I configure ALLOW_PUNCHOUT_COPY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_PUNCHOUT_COPY |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_PUNCHOUT_COPY'
```
