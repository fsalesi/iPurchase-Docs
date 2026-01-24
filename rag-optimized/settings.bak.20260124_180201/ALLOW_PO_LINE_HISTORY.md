# ALLOW_PO_LINE_HISTORY - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to view PO Line history. Use an asterisk for everyone. Leave blank for no one.

**Common questions this answers:**
- What is ALLOW_PO_LINE_HISTORY?
- What does ALLOW_PO_LINE_HISTORY do?
- What is the default value for ALLOW_PO_LINE_HISTORY?
- How do I configure ALLOW_PO_LINE_HISTORY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_PO_LINE_HISTORY |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_PO_LINE_HISTORY'
```
