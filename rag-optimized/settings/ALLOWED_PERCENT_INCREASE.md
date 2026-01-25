# ALLOWED_PERCENT_INCREASE - iPurchase System Setting

**Category:** Approval Workflow

Controls the maximum percentage an approver can increase a requisition's value before it gets automatically re-routed for approval. Works alongside ALLOWED_DOLLAR_INCREASE.

### How It Works

When an approver with edit permissions makes changes that increase the requisition total by more than this percentage, the requisition is automatically re-routed for approval when they click Approve.

### Valid Values

| Value | Behavior |
|-------|----------|
| Number | Maximum percentage increase allowed (e.g., "10" for 10%) |
| 0 | Any increase is allowed without re-routing |
| 0.01 | Any percentage increase triggers re-routing |

### Common Questions

- What is ALLOWED_PERCENT_INCREASE?
- Why did my requisition re-route when I approved it?
- How do I limit approver changes by percentage?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_PERCENT_INCREASE |
| **Category** | Approval Workflow |
| **Owner** | Finance |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_PERCENT_INCREASE'
```

### Related Settings

- [ALLOWED_DOLLAR_INCREASE](ALLOWED_DOLLAR_INCREASE.md)
