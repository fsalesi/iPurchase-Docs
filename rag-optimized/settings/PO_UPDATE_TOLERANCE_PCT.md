# PO_UPDATE_TOLERANCE_PCT - iPurchase System Setting

**Category:** Change Orders

Defines the maximum percentage a change order can increase without requiring re-approval. If the change order increases the PO value by less than this percentage, it may bypass the approval workflow (subject to other tolerance settings).

### How It Works

When a user submits a change order, the system calculates the percentage increase from the original PO value. If the increase is within this tolerance percentage, the change order may skip re-routing for approval.

Works in conjunction with PO_UPDATE_TOLERANCE_AMOUNT - both conditions must be met for the change to be considered within tolerance.

### Valid Values

| Value | Behavior |
|-------|----------|
| Number | Maximum allowed increase as percentage (e.g., "10" for 10%) |
| 0 or blank | Any percentage increase requires re-approval |

### Example

```
Original PO: $1,000
PO_UPDATE_TOLERANCE_PCT: 10
PO_UPDATE_TOLERANCE_AMOUNT: 100

Change order to $1,080 (+$80, +8%) -> Within both tolerances, may skip approval
Change order to $1,150 (+$150, +15%) -> Exceeds 10%, requires approval
Change order to $1,050 (+$50, +5%) -> Within both tolerances
```

### Common Questions

- What is PO_UPDATE_TOLERANCE_PCT?
- How do I set change order percentage tolerance?
- Why did my small change require re-approval?
- How do tolerance amount and percentage work together?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_TOLERANCE_PCT |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_TOLERANCE_PCT'
```

### Related Settings

- [PO_UPDATE_TOLERANCE_AMOUNT](PO_UPDATE_TOLERANCE_AMOUNT.md) - Maximum dollar increase allowed
- [PO_UPDATE_CHECK_REROUTE](PO_UPDATE_CHECK_REROUTE.md) - Check if approvers changed regardless of tolerance
- [CO_HEADER_REROUTE_FIELDS](CO_HEADER_REROUTE_FIELDS.md) - Header fields that force re-routing
