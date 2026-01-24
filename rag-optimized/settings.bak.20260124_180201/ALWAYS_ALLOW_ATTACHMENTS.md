# ALWAYS_ALLOW_ATTACHMENTS - iPurchase System Setting

**Category:** User Management

Comma-Separated list of groups. Any member of these groups will be allowed to add attachments to any req at any time, even after the req is converted to a PO.

**Common questions this answers:**
- What is ALWAYS_ALLOW_ATTACHMENTS?
- What does ALWAYS_ALLOW_ATTACHMENTS do?
- What is the default value for ALWAYS_ALLOW_ATTACHMENTS?
- How do I configure ALWAYS_ALLOW_ATTACHMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALWAYS_ALLOW_ATTACHMENTS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALWAYS_ALLOW_ATTACHMENTS'
```
