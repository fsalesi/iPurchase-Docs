# xxreq_mstr - Requisition Header Table - Indexes

Database indexes for the xxreq_mstr table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxreq_mstr?
- How do I query xxreq_mstr efficiently?
- What is the primary key of xxreq_mstr?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `approvedidc` | - | `xxreq_approved` |
| `byblanket` | - | `xxreq_blanket_nbr` |
| `byconsnbr` | - | `xxreq_cons_nbr` |
| `cart_id` | - | `xxreq_cartid` |
| `entry_date` | - | `xxreq_date` |
| `ext_notes` | Word | `xxreq_ext_notes` |
| `field1` | - | `xxreq_sort_field1` |
| `field10` | - | `xxreq_sort_field10` |
| `field2` | - | `xxreq_sort_field2` |
| `field3` | - | `xxreq_sort_field3` |
| `field4` | - | `xxreq_sort_field4` |
| `field5` | - | `xxreq_sort_field5` |
| `field6` | - | `xxreq_sort_field6` |
| `field7` | - | `xxreq_sort_field7` |
| `field8` | - | `xxreq_sort_field9` |
| `field9` | - | `xxreq_sort_field9` |
| `int_notes` | Word | `xxreq_int_notes` |
| `nbr` | Primary | `xxreq_nbr` |
| `req-userid` | - | `xxreq_userid` |
| `req_stat` | - | `xxreq_status` |
| `submittedidx` | - | `xxreq_submitted` |
| `typeidx` | - | `xxreq_type` |
| `vend` | - | `xxreq_vendor` |
| `word_idx2` | Word | `xxreq_word_idx2` |
| `word_idx3` | Word | `xxreq_word_idx3` |
| `word_idx_bucket` | Word | `xxreq_word_idx` |
| `xxdomain` | - | `xxreq_domain` |
| `xxreq_buyer` | - | `xxreq_buyer` |
| `xxreq_copied_from` | - | `xxreq_domain`, `xxreq_copied_from` |
| `xxreq_cost` | - | `xxreq_cost` |
| `xxreq_po_nbr` | - | `xxreq_domain`, `xxreq_po_nbr` |