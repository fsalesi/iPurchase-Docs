# REOPEN_PO - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of User ID's or Group ID's that are allowed to re-open a closed or cancelled PO via a change order. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is REOPEN_PO?
- What does REOPEN_PO do?
- What is the default value for REOPEN_PO?
- How do I configure REOPEN_PO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REOPEN_PO |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REOPEN_PO'
```
