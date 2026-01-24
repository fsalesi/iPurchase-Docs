# QX_VERSION - iPurchase System Setting

**Category:** Qxtend Integration

Qxtend version number.

**Common questions this answers:**
- What is QX_VERSION?
- What does QX_VERSION do?
- What is the default value for QX_VERSION?
- How do I configure QX_VERSION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_VERSION |
| **Category** | Qxtend Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_VERSION'
```
