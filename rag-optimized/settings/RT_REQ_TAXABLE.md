# RT_REQ_TAXABLE - iPurchase System Setting

**Category:** GL Accounts & Finance

Comma-separated req types.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_REQ_TAXABLE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_REQ_TAXABLE'
```

### Related Settings

- [RT_REQUIRE_PROJECT](RT_REQUIRE_PROJECT.md)
