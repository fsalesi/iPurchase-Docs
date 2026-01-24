# USE_APP_AMOUNT_OWN_REQS - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that indicates whether a user's requisition can be automatically converted to a PO if the user's approval amount exceeds the requisition amount. If t...

**Common questions this answers:**
- What is USE_APP_AMOUNT_OWN_REQS?
- What does USE_APP_AMOUNT_OWN_REQS do?
- What is the default value for USE_APP_AMOUNT_OWN_REQS?
- How do I configure USE_APP_AMOUNT_OWN_REQS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_APP_AMOUNT_OWN_REQS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_APP_AMOUNT_OWN_REQS'
```
