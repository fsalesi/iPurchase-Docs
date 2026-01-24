# DEFAULT_CC - iPurchase System Setting

**Category:** System Configuration

Administrator can set the default Cost Center or Departments for Punchouts and Catalog orders.

**Common questions this answers:**
- What is DEFAULT_CC?
- What does DEFAULT_CC do?
- What is the default value for DEFAULT_CC?
- How do I configure DEFAULT_CC?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_CC |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_CC'
```
