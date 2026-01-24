# PUNCHOUT_LEADTIME - iPurchase System Setting

**Category:** Catalog & Vendors

The number of days to add to today's date in order to calculate the Need Date for the requisition header. Can change by supplier in Supplier Maintenance (iPurchase)

**Common questions this answers:**
- What is PUNCHOUT_LEADTIME?
- What does PUNCHOUT_LEADTIME do?
- What is the default value for PUNCHOUT_LEADTIME?
- How do I configure PUNCHOUT_LEADTIME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_LEADTIME |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_LEADTIME'
```
