# OOF_NOTIFY_OLD - iPurchase System Setting

**Category:** Email Configuration

Controls whether existing pending requisitions are emailed to a newly assigned delegate when Out of Office is enabled.

### How It Works

When TRUE, all requisitions currently pending the user's approval are sent via email to the newly assigned delegate. When FALSE, the delegate only receives notifications for requisitions submitted after the delegation was set.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Email existing pending reqs to delegate (DEFAULT) |
| `FALSE` | Only notify delegate of new submissions |

### Common Questions

- What is OOF_NOTIFY_OLD?
- Will my delegate see my pending approvals?
- How do I control delegate notifications?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_NOTIFY_OLD |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_NOTIFY_OLD'
```

### Related Settings

- [ALLOW_OOF](ALLOW_OOF.md) - Enable Out of Office functionality
