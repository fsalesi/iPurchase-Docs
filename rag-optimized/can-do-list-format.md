# Can-Do List Format

### Overview

Can-Do lists are a pattern matching format used throughout iPurchase and iApprove for:
- **Permission lists** - Who can access features (e.g., `ALLOW_APPROVER_CHANGES_ROLES`)
- **Approval rule filters** - Which requisitions match a rule (e.g., Cost Center, Account filters)
- **User domain access** - Which domains a user can access (`wus_domains`)
- **Field validation** - Valid values for accounts, cost centers, etc.

### Format

A Can-Do list is a comma-separated string of patterns evaluated **left-to-right**. The first match wins.

| Pattern | Meaning |
|---------|---------|
| `*` | Match anything (wildcard) |
| `value` | Match exactly this value |
| `prefix*` | Match anything starting with prefix |
| `!value` | Exclude this value |
| `!prefix*` | Exclude anything starting with prefix |
| ` ` (blank) | Match nothing / deny all |

### Evaluation Rules

1. **Left-to-right** - Patterns are evaluated in order
2. **First match wins** - Once a value matches (include or exclude), evaluation stops
3. **No match = no access** - If nothing matches, the value is rejected
4. **Groups are expanded** - Group IDs are expanded to their member user IDs

### Examples

### Simple Examples

| Can-Do List | Input | Result | Why |
|-------------|-------|--------|-----|
| `*` | anything | ✅ Match | Wildcard matches all |
| `frank` | frank | ✅ Match | Exact match |
| `frank` | peter | ❌ No match | Not in list |
| `frank,peter` | peter | ✅ Match | Second value matches |
| `8100,8200` | 8100 | ✅ Match | First value matches |
| `81*` | 8100 | ✅ Match | Prefix match |
| `81*` | 8200 | ❌ No match | Doesn't start with 81 |

### Exclusion Examples

| Can-Do List | Input | Result | Why |
|-------------|-------|--------|-----|
| `!frank,*` | frank | ❌ Excluded | First pattern excludes frank |
| `!frank,*` | peter | ✅ Match | Not excluded, wildcard matches |
| `!8100,81*` | 8100 | ❌ Excluded | Exclusion comes first |
| `!8100,81*` | 8150 | ✅ Match | Not excluded, prefix matches |
| `!81*,*` | 8100 | ❌ Excluded | Prefix exclusion |
| `!81*,*` | 9000 | ✅ Match | Not excluded, wildcard matches |

### Complex Examples

| Can-Do List | Input | Result | Why |
|-------------|-------|--------|-----|
| `admin,!guest,users` | admin | ✅ Match | First pattern matches |
| `admin,!guest,users` | guest | ❌ Excluded | Second pattern excludes |
| `admin,!guest,users` | users | ✅ Match | Third pattern matches |
| `5521,!5622,56*,7*,!*` | 5521 | ✅ Match | Exact match first |
| `5521,!5622,56*,7*,!*` | 5622 | ❌ Excluded | Explicit exclusion |
| `5521,!5622,56*,7*,!*` | 5600 | ✅ Match | Prefix 56* matches |
| `5521,!5622,56*,7*,!*` | 7000 | ✅ Match | Prefix 7* matches |
| `5521,!5622,56*,7*,!*` | 8000 | ❌ Excluded | Falls through to !* |

### Order Matters!

| Can-Do List | Input | Result | Why |
|-------------|-------|--------|-----|
| `!8100,81*` | 8100 | ❌ Excluded | Exclusion checked first |
| `81*,!8100` | 8100 | ✅ Match | Prefix matches before exclusion checked |

**Key insight:** Put exclusions BEFORE the patterns they exclude from.

### Common Use Cases

### Allow Everyone
```
*
```

### Allow No One
```
(blank)
```

### Allow Specific Users
```
frank,peter,sarah
```

### Allow a Group
```
buyers,admin
```
(Group IDs are expanded to member users)

### Allow All Except Specific Values
```
!8100,*
```
(Everything except 8100)

### Allow Range with Exceptions
```
!8199,81*
```
(All 81xx except 8199)

### Multiple Prefixes
```
81*,82*,9*
```
(Anything starting with 81, 82, or 9)

### Where Can-Do Lists Are Used

### System Settings
- `ALLOW_*` settings (permissions)
- `*_ROLE_LIST` settings (role-based access)
- `RT_[type]_ACCOUNT_RANGE` (valid accounts by req type)
- `RT_[type]_CC_RANGE` (valid cost centers by req type)

### Approval Rules
- Orig/OBO filter
- Domain filter
- Req Type filter
- Dept/CC filter
- Account filter
- Sub Account filter
- Project filter
- UNSPSC filter

### User Configuration
- `wus_domains` - Which domains user can access
- `wus_sites` - Which sites user can access
- `wus_cc` - Which cost centers user can access

### Tips

1. **Test your patterns** - Use Approval Simulation to verify rule filters
2. **Start restrictive** - It's safer to start with specific values and expand
3. **Document complex lists** - Add notes explaining the business logic
4. **Remember order matters** - Exclusions must come before what they exclude from
5. **Blank means none** - An empty value denies all access

---

### Related Documentation

- [Users and Groups](../admin/screens/01-users-and-groups.md) - User domain/site/CC access
- [System Settings](../admin/screens/02-system-settings.md) - Permission settings
- [Approval Rules (Complex)](../admin/screens/ipurchase-01-approval-rules.md) - Rule filters
- [Approval Rules - Simple](../admin/screens/ipurchase-02-approval-rules-simple.md) - Rule filters
