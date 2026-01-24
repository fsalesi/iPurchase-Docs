# ALLOW_BLANKET_RELEASE - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's who are allowed to create releases against blanket POs.

**Common questions this answers:**
- What is ALLOW_BLANKET_RELEASE?
- What does ALLOW_BLANKET_RELEASE do?
- What is the default value for ALLOW_BLANKET_RELEASE?
- How do I configure ALLOW_BLANKET_RELEASE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_BLANKET_RELEASE |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_BLANKET_RELEASE'
```
