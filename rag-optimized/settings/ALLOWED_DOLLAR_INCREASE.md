# ALLOWED_DOLLAR_INCREASE - iPurchase System Setting

**Category:** Approval Workflow

Controls how much an approver can increase a requisition's value before it gets automatically re-routed for approval. This prevents approvers from significantly inflating requisition amounts without proper oversight.

### How It Works

When an approver who has edit permissions makes changes that increase the requisition total, the system compares the increase to this threshold. If the increase exceeds the allowed amount, the requisition is automatically re-routed for approval when they click Approve.

This only applies to approvers who have permission to edit requisitions after submission.

### Valid Values

| Value | Behavior |
|-------|----------|
| Number | Maximum dollar increase allowed (e.g., "100") |
| 0 | Any increase is allowed without re-routing |
| 0.01 | Any dollar increase triggers re-routing |

### Example

```
ALLOWED_DOLLAR_INCREASE: 100

Approver increases requisition from $500 to $550 (+$50)
-> Within tolerance, approval proceeds normally

Approver increases requisition from $500 to $650 (+$150)
-> Exceeds $100 tolerance, requisition re-routes for approval
```

### Common Questions

- What is ALLOWED_DOLLAR_INCREASE?
- Why did the requisition re-route when I approved it?
- How do I prevent approvers from inflating requisition amounts?
- Can I allow unlimited increases?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_DOLLAR_INCREASE |
| **Category** | Approval Workflow |
| **Owner** | Finance |
| **Default Value** | 100 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_DOLLAR_INCREASE'
```

### Related Settings

- [ALLOWED_PERCENT_INCREASE](ALLOWED_PERCENT_INCREASE.md)
