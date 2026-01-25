# Approval Groups and Approver Lists - iPurchase

**Purpose:** Understanding how approver fields work with groups, lists, and dynamic variables.

### Critical Rule: Comma-Separated Lists Require ALL to Approve

**This is commonly misunderstood:**

When the Approver field contains a comma-separated list, **ALL entities in the list must approve**.

| Approver Value | Behavior |
|----------------|----------|
| `finance` | Any ONE member of the "finance" group can approve |
| `$xxreq_userid,finance` | The originator AND someone from finance must BOTH approve |
| `frank,peter,mary` | Frank AND Peter AND Mary must ALL approve |
| `finance,purchasing` | Someone from finance AND someone from purchasing must BOTH approve |

### Single Group = Any Member

When the Approver is a single group, only ONE member needs to approve:

```
Approver: "ap_approvers"
→ Anyone in the ap_approvers group can approve
```

### Multiple Groups = One from Each

When multiple groups are listed, you need ONE approver from EACH group:

```
Approver: "finance,legal"
→ Need approval from someone in finance AND someone in legal
```

### Dynamic Variables in Lists

```
Approver: "$xxreq_userid,$FIRST_SUPERVISOR"
→ The originator AND their supervisor must both approve
```

### Why Always Use Groups (Even with One Member)

**Always use a group in the Approver field, even if it only has one member.**

**Benefits:**
- **Easy Personnel Changes:** When Bob retires and Jane takes over, just update group membership—no rule changes
- **Vacation Coverage:** Add a backup approver to the group temporarily
- **Audit Trail:** Group membership changes tracked separately from rule changes
- **Future Flexibility:** Easy to add members later

**Instead of:**
```
Approver: "bob.wilson"  ❌ Bad - hardcoded user
```

**Use:**
```
Approver: "cc8100_director"  ✅ Good - group with Bob as member
```

### Group Naming Conventions

| Pattern | Example | Use Case |
|---------|---------|----------|
| `cc[number]_[role]` | cc8100_manager | Cost center-specific roles |
| `[function]_approvers` | ap_approvers | Functional approvers |
| `[level]_approval` | executive_approval | Level-based groups |

### Common Questions

- Why do I need multiple approvals when I only listed one group?
- How do comma-separated approvers work?
- Should I use user IDs or groups in approval rules?
- How do I set up vacation coverage for approvers?

### Related Tables

- `wgr_mstr` - Group definitions
- `wugr_mstr` - User-to-group membership
