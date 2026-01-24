# IAEAMJE_MSTR_REQ_PREFIX - iPurchase System Setting

**Category:** iApprove Integration

Prefix for requisition numbers in iApprove EAM JE integration.

**Common questions this answers:**
- What is IAEAMJE_MSTR_REQ_PREFIX?
- What does IAEAMJE_MSTR_REQ_PREFIX do?
- What is the default value for IAEAMJE_MSTR_REQ_PREFIX?
- How do I configure IAEAMJE_MSTR_REQ_PREFIX?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IAEAMJE_MSTR_REQ_PREFIX |
| **Category** | iApprove Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IAEAMJE_MSTR_REQ_PREFIX'
```
