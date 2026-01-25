# RT_MEMO_ONLY_LIST - iPurchase System Setting

**Category:** Requisition Types

Comma-separated list of requisition types.

### How It Works

This setting configures requisition types behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_MEMO_ONLY_LIST |
| **Category** | Requisition Types |
| **Owner** | Finance |
| **Default Value** | Expense,Capital |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_MEMO_ONLY_LIST'
```

### Related Settings

- [RT_USE_LOCATION](RT_USE_LOCATION.md)