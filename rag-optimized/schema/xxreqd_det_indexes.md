# xxreqd_det - Requisition Detail/Line Items Table - Indexes

Database indexes for the xxreqd_det table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxreqd_det?
- How do I query xxreqd_det efficiently?
- What is the primary key of xxreqd_det?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `account` | - | `xxreqd_acct` |
| `cc` | - | `xxreqd_cc` |
| `ext_notes` | Word | `xxreqd_ext_notes` |
| `int_notes` | Word | `xxreqd_int_notes` |
| `item` | - | `xxreqd_item` |
| `po` | - | `xxreqd_domain`, `xxreqd_po_nbr` |
| `pri` | Primary + Unique | `xxreqd_domain`, `xxreqd_nbr`, `xxreqd_line` |
| `vendor` | - | `xxreqd_domain`, `xxreqd_vendor` |
| `xxreqd_u_code` | - | `xxreqd_u_code` |
| `xxreqd_word_idx` | Word | `xxreqd_word_idx` |