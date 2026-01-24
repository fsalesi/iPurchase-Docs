# ACCOUNT_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

A list of accounts which will always require a Project Code

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_REQUIRE_PROJECT'
```