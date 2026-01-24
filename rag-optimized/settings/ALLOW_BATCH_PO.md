# ALLOW_BATCH_PO - iPurchase System Setting

**Category:** Purchase Orders

Controls whether purchase orders are created immediately upon final approval or batched for later processing. Also controls PO consolidation behavior.

### How It Works

When a requisition receives final approval, this setting determines whether the PO is created immediately or queued for batch processing. It also affects whether the last approver can change this behavior.

### Valid Values

| Value | Create PO Now Default | Can Approver Change? |
|-------|----------------------|---------------------|
| `FALSE` | Yes (checked) | Yes |
| `FALSE-ALWAYS` | Yes (checked) | No |
| `TRUE` | No (unchecked) | Yes |
| `TRUE-ALWAYS` | No (unchecked) | No |
| `TRUE-SUPPLIER` | Per supplier setting | Yes |

### Consolidation Options

Add `-CONSOLIDATE` suffix to enable PO consolidation by default:
- `FALSE-CONSOLIDATE`
- `TRUE-CONSOLIDATE`
- `FALSE-ALWAYS-CONSOLIDATE`
- `TRUE-ALWAYS-CONSOLIDATE`

### Common Questions

- What is ALLOW_BATCH_PO?
- How do I enable immediate PO creation?
- How do I prevent approvers from batching POs?
- How does PO consolidation work?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_BATCH_PO |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | FALSE-ALWAYS |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_BATCH_PO'
```

### Related Settings

- **BATCH_CREATE_PO_GROUPS** - Groups allowed to run batch PO creation
