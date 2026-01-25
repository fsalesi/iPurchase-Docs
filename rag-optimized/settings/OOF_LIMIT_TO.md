# OOF_LIMIT_TO - iPurchase System Setting

**Category:** Out of Office / Delegation

Restricts who can be selected as a delegate when users set up Out of Office (OOF) delegation.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) to specify which users or groups can be chosen as delegates.

When a user goes on vacation and wants to delegate their approval authority, this setting controls who appears in the delegate selection list.

**Common configurations:**

```sql
OOF_LIMIT_TO = "*"           -- Anyone can be a delegate
OOF_LIMIT_TO = "approvers"   -- Only members of 'approvers' group
OOF_LIMIT_TO = ""            -- No one (delegation feature disabled)
OOF_LIMIT_TO = "mgrs,leads"  -- Only managers and leads groups
```

### Valid Values

- `*` - Any user can be selected as delegate
- (blank) - Delegation is disabled, no one can be selected
- Comma-separated list of user IDs or group IDs

### Common Questions

- How do I restrict who can be a delegate?
- How do I disable the delegation feature?
- Why can't I find certain users in the delegate dropdown?
- How do I limit delegates to managers only?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_TO |
| **Category** | Out of Office / Delegation |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_TO'
```
