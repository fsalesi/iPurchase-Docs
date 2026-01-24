# RT_MEMO_ONLY_LIST - iPurchase System Setting

**Category:** Requisition Types

Comma-separated list of requisition types. All line items created for the requisition types defined will be entered as Memo Items on the Purchase Order.

### How It Works

See the description above for details on how this setting affects system behavior.

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