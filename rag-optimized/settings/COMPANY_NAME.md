# COMPANY_NAME - iPurchase System Setting

**Category:** System Configuration

Company name displayed on reports, purchase orders, and printed documents.

**Common questions this answers:**
- What is COMPANY_NAME?
- What does COMPANY_NAME do?
- What is the default value for COMPANY_NAME?
- How do I configure COMPANY_NAME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COMPANY_NAME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COMPANY_NAME'
```
