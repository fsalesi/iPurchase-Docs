# DEFAULT_SUB_ACCOUNT - iPurchase System Setting

**Category:** GL Accounts & Finance

The default sub account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the sub account for a requisition created from a Punchout or Catalog i...

**Common questions this answers:**
- What is DEFAULT_SUB_ACCOUNT?
- What does DEFAULT_SUB_ACCOUNT do?
- What is the default value for DEFAULT_SUB_ACCOUNT?
- How do I configure DEFAULT_SUB_ACCOUNT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SUB_ACCOUNT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SUB_ACCOUNT'
```
