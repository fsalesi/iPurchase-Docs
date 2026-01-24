# RT_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

List of requisition typles that require a project code.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | Capital |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_REQUIRE_PROJECT'
```