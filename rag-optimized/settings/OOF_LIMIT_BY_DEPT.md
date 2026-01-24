# OOF_LIMIT_BY_DEPT - iPurchase System Setting

**Category:** Approval Workflow

Restricts Out of Office delegation to users within the same department. Ensures delegates understand the business context of what they're approving.

### How It Works

When TRUE, users can only select delegates who share at least one department with them. When set to FIRST, delegates must share the user's primary (first listed) department.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Delegate must share any department |
| `FIRST` | Delegate must share user's primary department |
| `FALSE` | No department restriction (DEFAULT) |

### Common Questions

- What is OOF_LIMIT_BY_DEPT?
- Why can't I delegate to someone in another department?
- How do I restrict delegation within departments?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_BY_DEPT |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_BY_DEPT'
```

### Related Settings

- [ALLOW_OOF](ALLOW_OOF.md) - Enable Out of Office functionality
- [OOF_LIMIT_TO_APPROVERS](OOF_LIMIT_TO_APPROVERS.md) - Restrict delegates to approvers
- [OOF_LIMIT_BY_DOLLARS](OOF_LIMIT_BY_DOLLARS.md) - Restrict delegates by approval limit
