# PO_UPDATE_TOLERANCE_AMOUNT - iPurchase System Setting

**Category:** Change Orders

Defines the maximum dollar amount a change order can increase without requiring re-approval. If the change order increases the PO value by less than this amount, it may bypass the approval workflow (subject to other tolerance settings).

### How It Works

When a user submits a change order (requisition updating an existing PO), the system compares the new total to the original. If the increase is within this tolerance amount, the change order may skip re-routing for approval.

Works in conjunction with PO_UPDATE_TOLERANCE_PCT - both conditions must be met for the change to be considered within tolerance.

### Valid Values

| Value | Behavior |
|-------|----------|
| Number | Maximum allowed increase in dollars (e.g., "100") |
| 0 or blank | Any increase requires re-approval |

### Example

```
Original PO: $1,000
PO_UPDATE_TOLERANCE_AMOUNT: 100
PO_UPDATE_TOLERANCE_PCT: 10

Change order to $1,050 (+$50, +5%) -> Within tolerance, may skip approval
Change order to $1,150 (+$150, +15%) -> Exceeds $100 amount, requires approval
Change order to $1,080 (+$80, +8%) -> Within tolerance
```

### Common Questions

- What is PO_UPDATE_TOLERANCE_AMOUNT?
- How do I set change order tolerance?
- Why did my change order require re-approval?
- How do tolerance amount and percentage work together?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_TOLERANCE_AMOUNT |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | 100 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_TOLERANCE_AMOUNT'
```

### Related Settings

- [PO_UPDATE_TOLERANCE_PCT](PO_UPDATE_TOLERANCE_PCT.md) - Maximum percentage increase allowed
- [PO_UPDATE_CHECK_REROUTE](PO_UPDATE_CHECK_REROUTE.md) - Check if approvers changed regardless of tolerance
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md) - Header fields that force re-routing
- [CO_ITEM_REROUTE_FIELDS](CO_ITEM_REROUTE_FIELDS.md) - Line fields that force re-routing
