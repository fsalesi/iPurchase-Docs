# USE_SUPERVISORS_TO_APPROVE - iPurchase System Setting

**Category:** Approval Workflow

**⚠️ DEPRECATED** - Global switch for supervisor-based approvals. Use `$SUPERVISORS` variables in approval rules instead.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enable supervisor chain approvals globally |
| **FALSE** | Disable supervisor chain approvals (DEFAULT) |

### How It Works

This is an **older, deprecated setting** that acts as a global on/off switch for supervisor-based approval routing.

**Why it's deprecated:**
The modern approach uses `$SUPERVISORS`, `$FIRST_SUPERVISOR`, or `$LAST_SUPERVISOR` variables directly in approval rules with conditions. This provides much more flexibility:

**Old way (this setting):**
```sql
USE_SUPERVISORS_TO_APPROVE = "TRUE"  -- All reqs use supervisor chain
```

**New way (approval rules):**
```sql
-- Only expense reqs over $5K use supervisor chain
Approver: $SUPERVISORS
Condition: Type = "Expense" AND Amount >= 5000
```

The new approach allows:
- Supervisor routing only for certain requisition types
- Different supervisor logic based on amount thresholds
- Combining supervisor approval with other approval methods

### Common Questions

- How do I enable supervisor approvals?
- What's the difference between USE_SUPERVISORS_TO_APPROVE and $SUPERVISORS?
- Should I use this setting or approval rules?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_SUPERVISORS_TO_APPROVE |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_SUPERVISORS_TO_APPROVE'
```

### Related Settings

- [USE_APP_AMOUNT_OWN_REQS](USE_APP_AMOUNT_OWN_REQS.md)
- [USE_LINE_APPROVALS](USE_LINE_APPROVALS.md)
