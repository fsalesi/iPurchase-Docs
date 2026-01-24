# DEFAULT_ACCT - iPurchase System Setting

**Category:** System Configuration

The Default Account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the account for a requisition created from a Punchout or Catalog is as fol...

**Common questions this answers:**
- What is DEFAULT_ACCT?
- What does DEFAULT_ACCT do?
- What is the default value for DEFAULT_ACCT?
- How do I configure DEFAULT_ACCT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_ACCT |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_ACCT'
```
