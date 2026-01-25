# xxAppRule - Complex Approval Rules Table - Fields

Stores complex approval rules with nested AND/OR logic. Used for advanced routing scenarios that simple rules cannot handle. Rule conditions are stored in xxAppField.

**Common questions this answers:**
- What fields are in the xxAppRule table?
- What fields are in the complex approval rules table?
- What is xxAR_Approver?

**Related tables:** xxAppField (conditions), xxapp_mstr (simple rules)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxAR_Domain` | char | i | Domain filter |
| `xxAR_RuleName` | char | i | Rule name (primary key) |
| `xxAR_AppLevel` | deci-2 |  | Approval sequence number |
| `xxAR_Approver` | char |  | Approver (supports $variables) |
| `xxAR_AmtType` | char |  | Header or Line |
| `xxAR_MinAmt` | deci-2 |  | Minimum amount |
| `xxAR_MaxAmt` | deci-2 |  | Maximum amount |
| `xxAR_Active` | logi |  | TRUE = rule active |
| `xxAR_stop` | logi |  | TRUE = stop after match |
| `xxAR_Eval_Lines` | logi |  | TRUE = evaluate per line |
| `xxAR_notify` | logi |  | TRUE = notification only |