# xxAppField - Complex Rule Conditions Table - Fields

Stores the conditions for complex approval rules. Forms a hierarchical tree structure with AND/OR operators linking field comparisons.

**Common questions this answers:**
- What fields are in the xxAppField table?
- What fields are in the rule conditions table?
- What is xxAF_Parent?

**Related tables:** xxAppRule (rule header)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxAF_Domain` | char | i |  |
| `xxAF_RuleName` | char | i | Rule name (FK to xxAppRule) |
| `xxAF_Seq` | inte | i | Condition sequence |
| `xxAF_Table` | char |  | Table name (empty for operator) |
| `xxAF_Field` | char |  | Field name (empty for operator) |
| `xxAF_Value` | char |  | Comparison value ($var supported) |
| `xxAF_Operand` | char |  | AND/OR or comparison operator |
| `xxAF_Group` | inte |  | This node group (0 = leaf) |
| `xxAF_Parent` | inte |  | Parent group number |