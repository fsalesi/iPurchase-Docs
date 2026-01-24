# PUNCHOUT_NOFRAMES - iPurchase System Setting

**Category:** Catalog & Vendors

iPurchase uses an HTML FRAMESET to display the Punchout website as well as the Return to iPurchase button at the top left. Some suppliers, like Amazon, will not allow the Return to iPurchase button...

**Common questions this answers:**
- What is PUNCHOUT_NOFRAMES?
- What does PUNCHOUT_NOFRAMES do?
- What is the default value for PUNCHOUT_NOFRAMES?
- How do I configure PUNCHOUT_NOFRAMES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_NOFRAMES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_NOFRAMES'
```
