# PUNCHOUT_RETRY - iPurchase System Setting

**Category:** Catalog & Vendors

Numeric. Number of retry attempts for failed punchout connections.

**Common questions this answers:**
- What is PUNCHOUT_RETRY?
- What does PUNCHOUT_RETRY do?
- What is the default value for PUNCHOUT_RETRY?
- How do I configure PUNCHOUT_RETRY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_RETRY |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_RETRY'
```
