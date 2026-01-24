# RT_MEMO_ONLY_LIST - iPurchase System Setting

**Category:** Requisition Types

Comma-separated list of requisition types. All line items created for the requisition types defined will be entered as Memo Items on the Purchase Order.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

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
