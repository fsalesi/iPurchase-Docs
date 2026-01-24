# CODE_LIST_TAX_ENVIRONMENT - iPurchase System Setting

**Category:** GL Accounts & Finance

LIST format. Dropdown values for tax environment field. Format: LIST:code:description,code:description

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_ENVIRONMENT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_ENVIRONMENT'
```