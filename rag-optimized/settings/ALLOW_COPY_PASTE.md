# ALLOW_COPY_PASTE - iPurchase System Setting

**Category:** User Management

This settings controls if users can copy paste in the requisition workbench. Sometimes copying from internet or PDF files cause item number

**Common questions this answers:**
- What is ALLOW_COPY_PASTE?
- What does ALLOW_COPY_PASTE do?
- What is the default value for ALLOW_COPY_PASTE?
- How do I configure ALLOW_COPY_PASTE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_COPY_PASTE |
| **Category** | User Management |
| **Owner** | description |
| **Default Value** | true |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_COPY_PASTE'
```
