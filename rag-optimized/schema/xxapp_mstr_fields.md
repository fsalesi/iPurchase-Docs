# xxapp_mstr - Simple Approval Rules Table - Fields

Stores simple approval rules using AND logic. The primary table for configuring approval routing based on amount, cost center, account, and other criteria. Recommended for most approval routing scenarios.

**Common questions this answers:**
- What fields are in the xxapp_mstr table?
- What fields are in the simple approval rules table?
- What is xxapp_seq (sequence)?
- What is xxapp_id?

**Related tables:** xxAppRule (complex rules), xxAppField (conditions), xxreq_audit (history)

## Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxapp_type` | char | i | Req type filter (* = all) |
| `xxapp_po_site` | char | i |  |
| `xxapp_cc` | char | i | Cost center filter (Can-Do) |
| `xxapp_amount` | deci-2 | i | Minimum amount threshold |
| `xxapp_id` | char | i | Approver (user/group/variable) |
| `xxapp_seq` | inte | i | Approval sequence (routing order) |
| `xxapp_domain` | char | i | Domain filter (* = all) |
| `xxapp_acct` | char | i | Account filter (Can-Do) |
| `xxapp_sub` | char | i | Sub-account filter (Can-Do) |
| `xxapp_project` | char | i | Project filter (Can-Do) |
| `oid_xxapp_mstr` | deci-2 | i |  |
| `xxapp_has_notes` | logi |  |  |
| `xxapp_has_attachments` | logi |  |  |
| `xxapp_max_amount` | deci-2 | i | Maximum amount threshold |
| `xxapp_description` | char | i | Rule description |
| `xxapp_active` | logi | i | TRUE = rule active |
| `xxapp_orig` | char |  | Originator filter (Can-Do) |
| `xxapp_notify` | logi | i | TRUE = notification only |
| `xxapp_line_site` | char |  |  |
| `xxapp_stop` | logi |  | TRUE = stop after this rule |
| `xxapp_which_cost` | char |  | Header or Line cost |
| `xxapp_unspsc` | char | i |  |