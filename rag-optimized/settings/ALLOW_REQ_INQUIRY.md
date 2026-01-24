# ALLOW_REQ_INQUIRY - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that are allowed to access the requisition inquiry screen Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_REQ_INQUIRY?
- What does ALLOW_REQ_INQUIRY do?
- What is the default value for ALLOW_REQ_INQUIRY?
- How do I configure ALLOW_REQ_INQUIRY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_REQ_INQUIRY |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_REQ_INQUIRY'
```
