# QX_CODEPAGE - iPurchase System Setting

**Category:** Qxtend Integration

Character encoding for Qxtend communication.

**Common questions this answers:**
- What is QX_CODEPAGE?
- What does QX_CODEPAGE do?
- What is the default value for QX_CODEPAGE?
- How do I configure QX_CODEPAGE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_CODEPAGE |
| **Category** | Qxtend Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_CODEPAGE'
```
