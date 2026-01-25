# REQUISITION_TYPES - iPurchase System Setting

**Category:** Requisitions

Defines the list of requisition types available in the system. Requisition types allow organizations to categorize purchases and apply different approval rules, default values, and behaviors to each type.

### How It Works

The value uses a special LIST format with a default type specified:
`LIST:default_code:Code1,Code2,Code3,...`

The first code after LIST: is the default type for new requisitions. The remaining codes are the available options users can select.

### Format

```
LIST:default:type1,type2,type3,...
```

- `LIST:` - Required prefix
- `default` - The default type code for new requisitions
- Comma-separated list of type codes

### Example

```
LIST:Expense:Expense,Capital,Contract,Tooling,Other
```

This creates 5 types with "Expense" as the default:
- Expense (default)
- Capital
- Contract
- Tooling
- Other

### Important Notes

- Approval rules use the CODE (e.g., "Expense") not the display name
- Type-specific settings use prefix RT_[TYPE]_ (e.g., RT_EXPENSE_ACCOUNT_RANGE)
- Changing type codes may affect existing approval rules

### Common Questions

- What is REQUISITION_TYPES?
- How do I add a new requisition type?
- How do I set the default requisition type?
- How do approval rules use requisition types?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQUISITION_TYPES |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | LIST:Expense:Expense,Capital,Contract,Tooling,Other |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQUISITION_TYPES'
```

### Related Settings

- [REQUISITION_PREFIX](REQUISITION_PREFIX.md)
