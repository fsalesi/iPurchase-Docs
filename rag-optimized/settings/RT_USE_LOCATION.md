# RT_USE_LOCATION - iPurchase System Setting

**Category:** Requisition Types

List of requisition types which will allow a Item Location to be entered during line item entry

### How It Works

This setting configures requisition types behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_USE_LOCATION |
| **Category** | Requisition Types |
| **Owner** | Purchasing |
| **Default Value** | Inventory |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_USE_LOCATION'
```

### Related Settings

- [RT_MEMO_ONLY_LIST](RT_MEMO_ONLY_LIST.md)
