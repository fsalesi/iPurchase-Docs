# QAD_REQUESTED_BY - iPurchase System Setting

**Category:** QAD Integration

This setting will use OBO as the Requested By. If you set QAD_REQUESTED_BY to "ORIGINATOR" then the req originator (xxreq_userid) will be used.

**Common questions this answers:**
- What is QAD_REQUESTED_BY?
- What does QAD_REQUESTED_BY do?
- What is the default value for QAD_REQUESTED_BY?
- How do I configure QAD_REQUESTED_BY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_REQUESTED_BY |
| **Category** | QAD Integration |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_REQUESTED_BY'
```
