# CODE_LIST_TAX_ENVIRONMENT - iPurchase System Setting

**Category:** GL Accounts & Finance

LIST format. Dropdown values for tax environment field. Format: LIST:code:description,code:description

**Common questions this answers:**
- What is CODE_LIST_TAX_ENVIRONMENT?
- What does CODE_LIST_TAX_ENVIRONMENT do?
- What is the default value for CODE_LIST_TAX_ENVIRONMENT?
- How do I configure CODE_LIST_TAX_ENVIRONMENT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_ENVIRONMENT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_ENVIRONMENT'
```
