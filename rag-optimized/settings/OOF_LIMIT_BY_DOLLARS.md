# OOF_LIMIT_BY_DOLLARS - iPurchase System Setting

**Category:** Approval Workflow

Restricts Out of Office delegation to users with equal or higher approval limits. Prevents delegation to someone with less approval authority.

### How It Works

When TRUE, users can only select delegates whose approval amount (wus_app_amt) is greater than or equal to their own. This ensures the delegate has sufficient authority to approve the same requisitions.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Delegate must have >= approval limit |
| `FALSE` | No approval limit restriction (DEFAULT) |

### Common Questions

- What is OOF_LIMIT_BY_DOLLARS?
- Why can't I delegate to a specific user?
- How do I ensure delegates have proper authority?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_BY_DOLLARS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_BY_DOLLARS'
```

### Related Settings

- [ALLOW_OOF](ALLOW_OOF.md) - Enable Out of Office functionality
- [OOF_LIMIT_TO_APPROVERS](OOF_LIMIT_TO_APPROVERS.md) - Restrict delegates to approvers
- [OOF_LIMIT_BY_DEPT](OOF_LIMIT_BY_DEPT.md) - Restrict delegates to same department
