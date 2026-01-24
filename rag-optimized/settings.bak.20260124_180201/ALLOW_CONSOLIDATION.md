# ALLOW_CONSOLIDATION - iPurchase System Setting

**Category:** User Management

This setting allows the administrator to turn On or Off the consolidation feature.

**Common questions this answers:**
- What is ALLOW_CONSOLIDATION?
- What does ALLOW_CONSOLIDATION do?
- What is the default value for ALLOW_CONSOLIDATION?
- How do I configure ALLOW_CONSOLIDATION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CONSOLIDATION |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CONSOLIDATION'
```
